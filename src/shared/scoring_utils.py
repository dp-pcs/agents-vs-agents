import boto3
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

SCORING_PROMPT = """
Benchmark 2 Scoring Prompt

You are an expert business plan evaluator. Given the following business plan, score it on a scale of 1–5 for each category below using the rubric provided.

Use the following rubric:

- **Completeness**
  - 1: Critically incomplete or missing most expected sections.
  - 2: Major sections missing or present but extremely shallow.
  - 3: Most required sections included with moderate detail.
  - 4: All major sections present with good depth and coherence.
  - 5: Fully complete, includes all expected content with exceptional detail and thoughtfulness.

- **Rationale Quality**
  - 1: No rationale or explanation of decisions provided.
  - 2: Minimal or unclear rationale with vague justifications.
  - 3: Basic reasoning provided for agent choices, but lacks clarity or depth.
  - 4: Good explanation of agent use and exclusions, with mostly clear reasoning.
  - 5: Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

- **Structure Quality**
  - 1: Chaotic, difficult to follow, little to no formatting.
  - 2: Basic structure but poorly formatted or disorganized.
  - 3: Adequate formatting and logical flow, but may lack polish.
  - 4: Well-structured, readable, and professionally formatted.
  - 5: Impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

Before assigning each score, provide a brief explanation based on the content provided.

Respond in the following JSON format:
{
  "completeness": <score>,
  "completeness_explanation": "...",
  "rationale_quality": <score>,
  "rationale_explanation": "...",
  "structure_quality": <score>,
  "structure_explanation": "..."
}
"""

def score_with_anthropic(plan_md):
    # existing Anthropic logic (or OpenAI proxy)
    ...

def score_with_openai(plan_md, model="gpt-4o", max_tokens=1024, max_retries=3):
    """
    Score a business plan using OpenAI GPT models. Truncates input to fit within token limits.
    """
    import os
    import json
    import time
    import requests
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not set in environment"}
    try:
        import tiktoken
        enc = tiktoken.encoding_for_model(model)
        def num_tokens(text):
            return len(enc.encode(text))
    except ImportError:
        # Fallback: estimate 1 token per 4 chars (very rough)
        def num_tokens(text):
            return max(1, len(text) // 4)

    # Truncation logic
    prompt = SCORING_PROMPT + "\n\n" + plan_md
    max_prompt_tokens = 8192 if model.startswith("gpt-4") else 4096
    # Reserve space for response
    max_prompt_tokens -= max_tokens
    if num_tokens(prompt) > max_prompt_tokens:
        # Truncate plan_md to fit
        allowed = max_prompt_tokens - num_tokens(SCORING_PROMPT + "\n\n")
        # Truncate by tokens if possible, else by words
        try:
            enc = tiktoken.encoding_for_model(model)
            plan_tokens = enc.encode(plan_md)
            truncated_plan = enc.decode(plan_tokens[:allowed])
        except Exception:
            words = plan_md.split()
            truncated_plan = " ".join(words[:allowed])
        prompt = SCORING_PROMPT + "\n\n" + truncated_plan
    # Compose OpenAI API payload
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert business plan evaluator."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.0
    }
    last_exception = None
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code == 200:
                content = resp.json()["choices"][0]["message"]["content"]
                # Strip markdown fences if present
                if content.startswith("```json"):
                    content = content.removeprefix("```json").strip()
                if content.endswith("```"):
                    content = content.removesuffix("```").strip()
                
                try:
                    result = json.loads(content)


                    
                    return result
                except Exception as parse_exc:
                    # It's possible the stripping still didn't result in valid JSON
                    return {"error": f"OpenAI returned non-JSON or malformed JSON after stripping: {content[:200]}..."}
            else:
                last_exception = resp.text
        except Exception as e:
            last_exception = str(e)
        time.sleep(2 ** attempt)
    return {"error": f"OpenAI API failed after {max_retries} attempts: {str(last_exception)}"}


import json

def score_with_bedrock(plan_md, model_info, headers=None, body=None, max_tokens=None):
    try:
        model_id, model_name = model_info
        prompt_text = f"{SCORING_PROMPT}\n\n{plan_md}"
        # If body is not provided, build it based on model type
        if body is None:
            if "claude" in model_id.lower():
                body = {
                    "anthropic_version": "bedrock-2023-05-31",
                    "messages": [{"role": "user", "content": prompt_text}],
                    "max_tokens": max_tokens if max_tokens is not None else 512
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
                    "max_tokens": max_tokens if max_tokens is not None else 1024
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
        # Ensure body is bytes for Bedrock
        if not isinstance(body, (bytes, bytearray)):
            body_bytes = json.dumps(body).encode("utf-8")
        else:
            body_bytes = body
        # Bedrock content type
        content_type = headers.get("content-type") if headers and "content-type" in headers else "application/json"
        accept = headers.get("accept") if headers and "accept" in headers else "application/json"

        response = bedrock_client.invoke_model(
            modelId=model_id,
            contentType=content_type,
            accept=accept,
            body=body_bytes
        )
        response_body = response["body"].read()
        result_raw = json.loads(response_body)

        # Extract the actual JSON content string, which might be nested
        content_str = None
        if "completion" in result_raw and isinstance(result_raw["completion"], str): # Common for some Claude versions
            content_str = result_raw["completion"]
        elif "content" in result_raw and isinstance(result_raw["content"], list) and len(result_raw["content"]) > 0 and "text" in result_raw["content"][0]: # Claude 3 messages format
             content_str = result_raw["content"][0]["text"]
        elif isinstance(result_raw, dict) and ('completeness' in result_raw or 'baseball_coach_handling' in result_raw): # Check if result_raw is already the score dict
            # This means result_raw is already the parsed score dictionary.
            # We will re-assign 'result' after normalization if this path is taken.
            pass # content_str remains None, result_raw will be used directly

        if content_str:
            # Strip markdown fences if present
            if content_str.startswith("```json"):
                content_str = content_str.removeprefix("```json").strip()
            if content_str.endswith("```"):
                content_str = content_str.removesuffix("```").strip()
            try:
                result = json.loads(content_str) # This is the actual score dictionary
            except json.JSONDecodeError as e:
                return {"error": f"Failed to parse JSON from Bedrock Claude response after stripping: {content_str[:200]}... Error: {e}"}
        elif isinstance(result_raw, dict) and ('completeness' in result_raw or 'baseball_coach_handling' in result_raw):
            result = result_raw # Use raw result if it looks like the score dict and content_str was not set
        else:
            return {"error": f"Could not extract recognizable JSON score from Bedrock response: {str(result_raw)[:200]}"}


        return result
    except Exception as e:
        return {"error": str(e)}