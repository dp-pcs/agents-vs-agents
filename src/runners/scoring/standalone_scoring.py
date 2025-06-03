import json
import time
import argparse
import re
import openai
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../benchmark2")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
# Add tools directory to sys.path for bedrock_models_validated import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../tools")))
from shared.scoring_utils import SCORING_PROMPT, score_with_anthropic, score_with_bedrock
from bedrock_models_validated import LLM_MODELS

def load_plan_md(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r") as f:
        return f.read()

def parse_scores(text):
    scores = {}
    try:
        # Define regex patterns for each score
        patterns = {
            "completeness": r"completeness\s*[:\-]?\s*(\d)",
            "rationale_quality": r"rationale\s*quality\s*[:\-]?\s*(\d)",
            "structure_quality": r"structure\s*quality\s*[:\-]?\s*(\d)",
            "baseball_coach_handling": r"baseball\s*coach\s*handling\s*[:\-]?\s*(\d)",
        }
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                score = int(match.group(1))
                if 1 <= score <= 5:
                    scores[key] = score
                else:
                    # Score out of expected range
                    scores[key] = None
            else:
                scores[key] = None
        # Check if all scores were found
        if all(v is not None for v in scores.values()):
            return scores
        else:
            return None
    except Exception:
        return None

def score_with_bedrock(plan_md, model_info, headers=None, body=None, max_tokens=None):
    """
    Sends a prompt to an AWS Bedrock model using boto3 and returns the parsed response or error.
    """
    import boto3
    import botocore
    model_id, model_name = model_info
    try:
        # Prepare the client
        bedrock = boto3.client("bedrock-runtime")

        # If body is not provided, build it based on model type
        if body is None:
            prompt_text = f"{SCORING_PROMPT}\n\n{plan_md}"

            if "claude" in model_id.lower():
                # Claude via Bedrock expects only "user" and "assistant" roles, and requires anthropic_version
                body = {
                    "anthropic_version": "bedrock-2023-05-31",
                    "messages": [
                        {"role": "user", "content": f"{SCORING_PROMPT}\n\n{plan_md}"}
                    ],
                    "max_tokens": 512
                }
            elif "titan" in model_id.lower():
                body = {
                    "inputText": prompt_text,
                    "textGenerationConfig": {
                        "temperature": 0.7,
                        "maxTokenCount": 1024,
                        "topP": 0.9
                    }
                }
            elif "cohere" in model_id.lower():
                body = {
                    "chat_history": [],
                    "message": prompt_text
                }
            elif "mistral" in model_id.lower():
                body = {
                    "prompt": prompt_text,
                    "temperature": 0.7,
                    "max_tokens": 1024
                }
            else:
                # Default generic body
                body = {
                    "inputs": prompt_text,
                    "parameters": {
                        "max_new_tokens": max_tokens if max_tokens is not None else 512,
                        "temperature": 0,
                        "return_full_text": False,
                    },
                }
        # Bedrock expects a JSON string for body
        body_bytes = json.dumps(body).encode("utf-8")

        # Bedrock content type
        content_type = headers.get("content-type") if headers and "content-type" in headers else "application/json"
        accept = headers.get("accept") if headers and "accept" in headers else "application/json"

        # Retry logic for ModelErrorException
        max_retries = 3
        retry_delay = 2
        for attempt in range(max_retries):
            try:
                response = bedrock.invoke_model(
                    modelId=model_id,
                    body=body_bytes,
                    contentType=content_type,
                    accept=accept
                )
                break  # Success, break out of retry loop
            except botocore.exceptions.ClientError as e:
                # Only retry on ModelErrorException
                error_code = e.response.get("Error", {}).get("Code", "")
                if error_code == "ModelErrorException":
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                    else:
                        return {"error": f"ModelErrorException after {max_retries} attempts: {str(e)}"}
                else:
                    raise
        # The response body is a StreamingBody
        response_body = response.get("body")
        if hasattr(response_body, "read"):
            response_str = response_body.read().decode("utf-8")
        else:
            response_str = response_body

        # Try to parse the response as JSON, else as text
        try:
            response_json = json.loads(response_str)
            # Try to extract completion text
            completion_text = None
            # Bedrock responses may differ by model
            # Cohere: {'generations': [{'text': ...}]}
            if "generations" in response_json and isinstance(response_json["generations"], list):
                completion_text = response_json["generations"][0].get("text", "")
            # Mistral: {'outputs': [{'text': ...}]}
            elif "outputs" in response_json and isinstance(response_json["outputs"], list):
                completion_text = response_json["outputs"][0].get("text", "")
            # Claude: {'completion': ...}
            elif "completion" in response_json:
                completion_text = response_json["completion"]
            # Titan: {'results': [{'outputText': ...}]}
            elif "results" in response_json and isinstance(response_json["results"], list):
                completion_text = response_json["results"][0].get("outputText", "")
            # Fallback: whole response
            if completion_text is None:
                completion_text = response_str
        except Exception:
            completion_text = response_str

        result = {
            "completion_text": completion_text
        }
        # Try to parse as JSON if possible, including extracting JSON block from messy text
        try:
            # Attempt direct parse if starts with {
            if completion_text.strip().startswith("{"):
                parsed = json.loads(completion_text)
                if isinstance(parsed, dict):
                    result.update(parsed)
            else:
                # Attempt to extract JSON block from text using improved regex
                json_match = re.search(r"\{[\s\S]+?\}", completion_text, re.DOTALL)
                if json_match:
                    extracted_json_str = json_match.group(0)
                    try:
                        parsed = json.loads(extracted_json_str)
                        if isinstance(parsed, dict):
                            result.update(parsed)
                        else:
                            parsed_scores = parse_scores(completion_text)
                            if parsed_scores:
                                result.update(parsed_scores)
                            else:
                                result["parsing_failed"] = True
                    except Exception:
                        parsed_scores = parse_scores(completion_text)
                        if parsed_scores:
                            result.update(parsed_scores)
                        else:
                            result["parsing_failed"] = True
                else:
                    parsed_scores = parse_scores(completion_text)
                    if parsed_scores:
                        result.update(parsed_scores)
                    else:
                        result["parsing_failed"] = True
        except Exception:
            result["parsing_failed"] = True
        return result
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Score a single agentic benchmark output using Anthropic and Bedrock models.")
    parser.add_argument("--file", required=True, help="Path to the markdown file (e.g. b2_crewai_dynamic_orchestration.md)")
    args = parser.parse_args()

    plan_md = load_plan_md(args.file)

    print(f"📄 Scoring: {args.file}")
    results = []

    # === OpenAI Chat Completion (via OPENAI_API_KEY) ===
    if os.getenv("OPENAI_API_KEY"):
        print("🧠 Scoring with OpenAI Chat Completion...")
        try:
            from openai import OpenAI
            client = OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SCORING_PROMPT},
                    {"role": "user", "content": plan_md}
                ],
                temperature=0,
            )
            completion_text = response.choices[0].message.content
            result = {
                "model": "gpt-4o",
                "completion_text": completion_text
            }
            try:
                if completion_text.strip().startswith("{"):
                    parsed = json.loads(completion_text)
                    if isinstance(parsed, dict):
                        result.update(parsed)
                else:
                    parsed_scores = parse_scores(completion_text)
                    if parsed_scores:
                        result.update(parsed_scores)
                    else:
                        result["parsing_failed"] = True
            except Exception:
                result["parsing_failed"] = True
            results.append(result)
            print("✅ OpenAI scoring complete.")
        except Exception as e:
            print(f"❌ OpenAI scoring failed: {e}")
            results.append({"error": str(e), "model": "gpt-4o"})
    else:
        print("⚠️ OPENAI_API_KEY not detected. Skipping OpenAI scoring.")

    # === Bedrock Models ===
    if os.getenv("AWS_ACCESS_KEY_ID"):
        print("🔧 Bedrock enabled — scoring with available models...\n")
        for model in LLM_MODELS:
            model_id = model["id"]
            model_name = model["name"]
            print(f"🧪 {model_name}")
            try:
                # Adjust prompt and parameters for specific models
                prompt_to_score = plan_md
                max_tokens = None
                headers = {}
                body = {}

                # For Claude models, explicitly add max_tokens
                if "claude" in model_id.lower():
                    max_tokens = 512

                # For Titan, truncate prompt to avoid token overflow
                if "titan" in model_id.lower():
                    if len(plan_md) > 3000:
                        prompt_to_score = plan_md[:3000]

                # For Cohere Command R+ models, update headers and body structure
                if "cohere-command" in model_id.lower():
                    headers = {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    }
                    body = {
                        "inputs": prompt_to_score,
                        "model": model_id,
                        "max_tokens": 512,
                        "temperature": 0.0,
                        "k": 0,
                        "p": 1,
                        "stop_sequences": [],
                    }
                    res = score_with_bedrock(prompt_to_score, (model_id, model_name), headers=headers, body=body)
                # For Mistral, update body structure to match Bedrock JSON format
                elif "mistral" in model_id.lower():
                    headers = {
                        "content-type": "application/json",
                        "accept": "application/json",
                    }
                    body = {
                        "prompt": prompt_to_score,
                        "temperature": 0.7,
                        "max_tokens": 512
                    }
                    res = score_with_bedrock(prompt_to_score, (model_id, model_name), headers=headers, body=body)
                else:
                    # For other models, pass max_tokens if set
                    res = score_with_bedrock(prompt_to_score, (model_id, model_name), max_tokens=max_tokens)

                if res is None:
                    results.append({"error": "Model returned no response", "model": model_name})
                    print(f"❌ {model_name}: No response (None returned)")
                else:
                    res["model"] = model_name
                    results.append(res)
                    if "error" in res:
                        print(f"⚠️  Error: {res['error']}")
                    else:
                        print("✅ Success.")
            except Exception as e:
                results.append({"error": str(e), "model": model_name})
                print(f"❌ Failed: {e}")
            time.sleep(1.5)
    else:
        print("⚠️ AWS credentials not detected. Skipping Bedrock scoring.")

    # === Output Results ===
    print("\n📊 Score Summary:\n")
    # Prepare Markdown table
    table_headers = [
        "Model",
        "Completeness",
        "Rationale",
        "Structure",
        "BaseballCoach",
        "Total"
    ]
    table_rows = []
    failed_rows = []
    for result in results:
        model = result.get("model", "?")
        if "error" in result or "parsing_failed" in result:
            failed_rows.append(result)
            continue
        completeness = result.get("completeness", "?")
        rationale = result.get("rationale_quality", "?")
        structure = result.get("structure_quality", "?")
        baseball = result.get("baseball_coach_handling", "?")
        # Compute total if possible
        try:
            total = (
                int(completeness)
                + int(rationale)
                + int(structure)
                + int(baseball)
            )
        except Exception:
            total = "?"
        table_rows.append([
            str(model),
            str(completeness),
            str(rationale),
            str(structure),
            str(baseball),
            str(total)
        ])
    # Print table
    # Markdown header
    header_row = "| " + " | ".join(table_headers) + " |"
    sep_row = "| " + " | ".join(["---"] * len(table_headers)) + " |"
    print(header_row)
    print(sep_row)
    for row in table_rows:
        print("| " + " | ".join(row) + " |")
    # Print failures at the end
    if failed_rows:
        print("\n❌ Failure Summary:")
        for result in failed_rows:
            model = result.get("model", "?")
            if "error" in result:
                print(f"❌ {model}: {result['error']}")
            elif "parsing_failed" in result:
                print(f"⚠️ {model}: Parsing of completion text failed. Raw text:\n{result.get('completion_text','')}")

    # Optional: save to disk
    output_json = args.file.replace(".md", "_scores.json")
    with open(output_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n📝 Scores saved to: {output_json}")

if __name__ == "__main__":
    main()