import os
import matplotlib.pyplot as plt
import sys
import time
import json
import re
import requests
from glob import glob
from datetime import datetime

# Add paths to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Test2'))

# Import the testing functions from each framework
from src.runners.benchmark2.v2_runner_autogen import run_autogen_test
from src.runners.benchmark2.v2_runner_crewai import run_crewai_test
from src.runners.benchmark2.v2_runner_langgraph import run_langgraph_test

# === CONFIG ===
import argparse

# Parse optional output directory argument
parser = argparse.ArgumentParser(description='Benchmark2 Full Pipeline Run')
parser.add_argument('output_dir', nargs='?', default=None, help='Output directory for this run')
parser.add_argument('--score-only', action='store_true', help='Only run scoring/evaluation on existing outputs in the output_dir')
args = parser.parse_args()

if args.output_dir:
    RESULTS_DIR = os.path.abspath(args.output_dir)
else:
    # Always create results under the project root /results/benchmark2
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
    run_dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    RESULTS_PARENT = os.path.join(PROJECT_ROOT, 'results', 'benchmark2')
    os.makedirs(RESULTS_PARENT, exist_ok=True)
    RESULTS_DIR = os.path.join(RESULTS_PARENT, f'benchmark2_{run_dt_str}')
    os.makedirs(RESULTS_DIR, exist_ok=True)
    # Symlink latest_run to this run folder
    latest_symlink = os.path.join(RESULTS_PARENT, 'latest_run')
    if os.path.islink(latest_symlink) or os.path.exists(latest_symlink):
        os.remove(latest_symlink)
    os.symlink(RESULTS_DIR, latest_symlink)

NORMALIZED_DIR = os.path.join(RESULTS_DIR, 'normalized')
SUMMARY_REPORT = os.path.join(RESULTS_DIR, 'benchmark_report.md')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_MODEL = 'claude-3-sonnet-20240229'

# Bedrock config for multi-model scoring

BEDROCK_ENABLED = os.getenv('AWS_ACCESS_KEY_ID') is not None
BEDROCK_MODEL_REGISTRY = {
    "claude_opus": ("anthropic.claude-3-opus-20240229-v1:0", "Claude 3 Opus"),
    "claude_sonnet": ("anthropic.claude-3-sonnet-20240229-v1:0", "Claude 3 Sonnet"),
    "claude_haiku": ("anthropic.claude-3-haiku-20240307-v1:0", "Claude 3 Haiku"),
    "titan_express": ("amazon.titan-text-express-v1", "Titan Text Express"),
    "titan_lite": ("amazon.titan-text-lite-v1", "Titan Text Lite"),
    "mistral_7b": ("mistral.mistral-7b-instruct-v0:0", "Mistral 7B Instruct"),
    "deepseek_coder": ("deepseek.deepseek-coder-v1:0", "DeepSeek Coder"),
}

BEDROCK_MODELS = list(BEDROCK_MODEL_REGISTRY.values())

SCORING_PROMPT = '''
You are an expert business plan evaluator. Given the following business plan, score it on a scale of 1–5 for each category below.

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

Before assigning a score, explain briefly why you gave that score based on the content provided.

Also, assess how the BaseballCoachAgent is handled:
- 0 = Not mentioned at all
- 1 = Mentioned but not clearly explained
- 2 = Mentioned and explicitly excluded or explained as irrelevant

Respond in the following JSON format:
{
  "completeness": <score>,
  "completeness_explanation": "...",
  "rationale_quality": <score>,
  "rationale_explanation": "...",
  "structure_quality": <score>,
  "structure_explanation": "...",
  "baseball_coach_handling": <0, 1, or 2>
}
'''

HEADERS = {
    'x-api-key': ANTHROPIC_API_KEY,
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
}

# === FRAMEWORK TESTING ===
def run_all_framework_tests():
    """Run all framework tests and gather metrics"""
    print("=" * 50)
    print("RUNNING STANDARDIZED AGENT FRAMEWORK COMPARISON")
    print("=" * 50)
    
    # Run all tests and collect results
    results = {}
    
    print("\n\n=== AUTOGEN TEST ===\n")
    autogen_output, autogen_duration, autogen_turns, autogen_messages = run_autogen_test()
    results["autogen"] = {
        "duration": autogen_duration,
        "agent_turns": autogen_turns,
        "output_length": len(autogen_output) if autogen_output else 0,
        "output": autogen_output,  # Store the actual output for analysis
        "messages": autogen_messages  # Store full message history for analysis
    }
    
    # Analyze BaseballCoachAgent handling for AutoGen
    autogen_baseball_messages = [m for m in autogen_messages if m.get("name") == "BaseballCoachAgent"]
    if autogen_baseball_messages:
        results["autogen"]["filtered_irrelevant_agents"] = "No"
        results["autogen"]["agent_filtering_details"] = (
            "Detection method: Message-level analysis.\n"
            "BaseballCoachAgent appears to have been used despite being irrelevant ("
            f"{len(autogen_baseball_messages)} messages)."
        )
    else:
        results["autogen"]["filtered_irrelevant_agents"] = "Yes"
        results["autogen"]["agent_filtering_details"] = (
            "Detection method: Message-level analysis.\n"
            "BaseballCoachAgent was not used, suggesting it was filtered out."
        )
    
    print("\n\n=== CREWAI TEST ===\n")
    crewai_output, crewai_duration, crewai_turns = run_crewai_test()
    # Fix for CrewAI agent turns - count major sections as a proxy for agent contributions
    crewai_section_count = len(re.findall(r'##? [A-Za-z\s\u0026]+\n', str(crewai_output)))
    if crewai_turns == 0 and crewai_section_count > 0:
        crewai_turns = crewai_section_count
        print(f"[INFO] CrewAI agent turns updated from 0 to {crewai_turns} based on section count")
    
    results["crewai"] = {
        "duration": crewai_duration,
        "agent_turns": crewai_turns,
        "output_length": len(crewai_output) if crewai_output else 0,
        "output": crewai_output  # Store the actual output for analysis
    }

    # Analyze BaseballCoachAgent handling for CrewAI
    crewai_baseball_filtered = True
    if "Baseball Coach" in str(crewai_output):
        baseball_context = re.search(r'([^.]*?Baseball Coach[^.]*\.)', str(crewai_output), re.IGNORECASE)
        if baseball_context:
            context = baseball_context.group(1).lower()
            negative_phrases = ["was used", "contributed", "provided input", "included"]
            positive_phrases = ["not used", "not involve", "irrelevant", "excluded", "did not use", "was not involved"]
            if any(phrase in context for phrase in negative_phrases) and not any(phrase in context for phrase in positive_phrases):
                crewai_baseball_filtered = False
    results["crewai"]["filtered_irrelevant_agents"] = "Yes" if crewai_baseball_filtered else "No"
    results["crewai"]["agent_filtering_details"] = (
        "Detection method: Context-aware text analysis.\n"
        f"BaseballCoachAgent {'was mentioned but in context of being excluded' if crewai_baseball_filtered else 'appears to have been used'} in the output."
    )

    print("\n\n=== LANGGRAPH TEST ===\n")
    langgraph_output, langgraph_duration, langgraph_turns = run_langgraph_test()
    results["langgraph"] = {
        "duration": langgraph_duration,
        "agent_turns": langgraph_turns,
        "output_length": len(langgraph_output) if langgraph_output else 0,
        "output": langgraph_output  # Store the actual output for analysis
    }

    # Analyze BaseballCoachAgent handling for LangGraph
    langgraph_baseball_filtered = True
    if "BaseballCoachAgent" in str(langgraph_output):
        positive_phrases = ["chose not to involve", "not relevant", "irrelevant", "not used", "did not involve", "excluded"]
        baseball_context = re.search(r'([^.]*?BaseballCoachAgent[^.]*\.)', str(langgraph_output), re.IGNORECASE)
        if baseball_context:
            context = baseball_context.group(1).lower()
            if not any(phrase in context for phrase in positive_phrases):
                langgraph_baseball_filtered = False
    results["langgraph"]["filtered_irrelevant_agents"] = "Yes" if langgraph_baseball_filtered else "No"
    results["langgraph"]["agent_filtering_details"] = (
        "Detection method: Context-aware text analysis.\n"
        f"BaseballCoachAgent {'was mentioned but in context of being excluded' if langgraph_baseball_filtered else 'appears to have been used'} in the output."
    )

    
    # For CrewAI - Context-aware check for baseball mentions
    crewai_baseball_filtered = True
    if "Baseball Coach" in str(crewai_output):
        # Check if it mentions being excluded/irrelevant vs being used
        baseball_context = re.search(r'([^.]*?Baseball Coach[^.]*\.)', str(crewai_output), re.IGNORECASE)
        if baseball_context:
            context = baseball_context.group(1).lower()
            negative_phrases = ["was used", "contributed", "provided input", "included"]
            positive_phrases = ["not used", "not involve", "irrelevant", "excluded", "did not use", "was not involved"]
            
            # If it mentions being used in a positive way without exclusion context
            if any(phrase in context for phrase in negative_phrases) and not any(phrase in context for phrase in positive_phrases):
                crewai_baseball_filtered = False
    results["crewai"]["filtered_irrelevant_agents"] = "Yes" if crewai_baseball_filtered else "No"
    results["crewai"]["agent_filtering_details"] = (
        "Detection method: Context-aware text analysis.\n"
        f"BaseballCoachAgent {'was mentioned but in context of being excluded' if crewai_baseball_filtered else 'appears to have been used'} in the output."
    )
    
    # For LangGraph - Context-aware check
    langgraph_baseball_filtered = True
    if "BaseballCoachAgent" in str(langgraph_output):
        # Look for phrases that indicate the agent was intentionally NOT used
        positive_phrases = ["chose not to involve", "not relevant", "irrelevant", "not used", "did not involve", "excluded"]
        
        # Extract context around baseball mentions
        baseball_context = re.search(r'([^.]*?BaseballCoachAgent[^.]*\.)', str(langgraph_output), re.IGNORECASE)
        if baseball_context:
            context = baseball_context.group(1).lower()
            # If none of these phrases are found near the baseball mention, then it was likely used
            if not any(phrase in context for phrase in positive_phrases):
                langgraph_baseball_filtered = False
    results["langgraph"]["filtered_irrelevant_agents"] = "Yes" if langgraph_baseball_filtered else "No"
    results["langgraph"]["agent_filtering_details"] = (
        "Detection method: Context-aware text analysis.\n"
        f"BaseballCoachAgent {'was mentioned but in context of being excluded' if langgraph_baseball_filtered else 'appears to have been used'} in the output."
    )
    
    # Save raw outputs for each framework in results directory
    os.makedirs(RESULTS_DIR, exist_ok=True)
    for framework, data in results.items():
        output_path = os.path.join(RESULTS_DIR, f"b2_{framework}_dynamic_orchestration.md")
        with open(output_path, "w") as f:
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"# {framework.capitalize()} Dynamic Orchestration Output\n\n")
            f.write(data["output"])
            f.write(f"\n\n**Time to complete:** {data['duration']} seconds\n")
            f.write(f"\n**Agent turns:** {data['agent_turns']}\n")
    
    return results

# === SCORING ===

def score_with_anthropic(plan_md, max_retries=3):
    """Score plan using Anthropic Claude API with retry logic for network errors."""
    import httpx
    from requests.exceptions import RequestException
    import time
    # Extract any mentions of BaseballCoachAgent before truncating
    baseball_mentions = re.findall(r'(?i)baseball\s*coach\s*agent', plan_md)
    baseball_context = "BaseballCoachAgent mentioned" if baseball_mentions else "BaseballCoachAgent not mentioned"
    
    # Check if BaseballCoachAgent is explicitly excluded
    baseball_excluded = bool(re.search(r'(?i)(?:not\s+us(?:ed|ing)|exclud(?:ed|ing)|irrelevant)[^.]*?baseball', plan_md))
    
    # Truncate content but ensure we keep important parts (rationale + beginning)
    prompt = SCORING_PROMPT + '\n---\nImportant context: ' + baseball_context
    
    # Try to extract and keep the rationale section
    rationale_match = re.search(r'(?:#+ *Rationale[^\n]*\n+|\*\*Rationale[^\n]*\n+|Rationale:)([^\n].*?)(?=\n#|\n\*\*|\Z)', plan_md, re.DOTALL)
    
    if rationale_match:
        rationale = rationale_match.group(1).strip()
        # Keep first 3000 chars of plan with rationale at beginning
        plan_content = f"RATIONALE SECTION:\n{rationale}\n\nREST OF DOCUMENT (truncated):\n{plan_md[:6000]}"
    else:
        # Just send first part of document
        plan_content = plan_md[:8000]
    
    prompt += '\n\n' + plan_content
    
    data = {
        "model": ANTHROPIC_MODEL,
        "max_tokens": 1024,  # Increased for more detailed explanations
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    last_exception = None
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=HEADERS,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            content = response.json()["content"]

            if isinstance(content, list):
                text = "\n".join([block.get("text", "") for block in content])
            else:
                text = str(content)

            # Try to extract JSON
            try:
                start_idx = text.find('{')
                end_idx = text.rfind('}') + 1
                if start_idx >= 0 and end_idx > start_idx:
                    json_str = text[start_idx:end_idx]
                    j = json.loads(json_str)

                    # Add our own assessment of BaseballCoachAgent handling if not provided
                    explicit_exclusion_phrases = [
                        "not needed", "not used", "excluded", "irrelevant", "did not use", "was not involved"
                    ]
                    if any(p in plan_md.lower() for p in explicit_exclusion_phrases):
                        j["baseball_coach_handling"] = 2
                    elif "baseball_coach_handling" not in j:
                        if baseball_excluded:
                            j["baseball_coach_handling"] = 2  # Explicitly excluded with explanation
                        elif baseball_mentions:
                            j["baseball_coach_handling"] = 1  # Mentioned but not explained
                        else:
                            j["baseball_coach_handling"] = 0  # Not mentioned

                    return j
                else:
                    return {"error": "Could not find JSON brackets", "raw": text}

            except Exception as e:
                return {"error": f"Could not parse score JSON: {str(e)}", "raw": text}

        except (httpx.RemoteProtocolError, RequestException) as e:
            last_exception = e
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
                continue
            else:
                return {"error": f"Anthropic API connection failed after {max_retries} attempts: {str(e)}"}
        except Exception as e:
            return {"error": f"API request failed: {str(e)}"}

    # If all retries failed
    return {"error": f"Anthropic API request repeatedly failed: {str(last_exception)}"}

# === NORMALIZATION AND EVALUATION ===

def score_with_bedrock(plan_md, model_id):
    """Score plan using AWS Bedrock models"""
    if not BEDROCK_ENABLED:
        return {"error": "AWS credentials not configured"}
    
    try:
        import boto3
        
        # Truncate content to fit model limits
        truncated_plan = plan_md[:10000]  # Adjust depending on model token limits
        
        # Prepare prompt
        prompt = SCORING_PROMPT + "\n\nBusiness Plan:\n" + truncated_plan
        
        # Route Anthropic models to Anthropic API, not Bedrock
        if "anthropic" in model_id:
            return score_with_anthropic(plan_md)
        elif "amazon.titan" in model_id:
            body = {
                "inputText": prompt,
                "textGenerationConfig": {
                    "maxTokenCount": 1000,
                    "temperature": 0.2
                }
            }
        elif "mistral.mistral-7b-instruct" in model_id:
            body = {
                "prompt": prompt,
                "max_tokens": 1000,
                "temperature": 0.2
            }
        elif "deepseek.deepseek-coder" in model_id:
            body = {
                "prompt": prompt,
                "max_tokens": 1000,
                "temperature": 0.2
            }
        else:
            return {"error": f"Unsupported or misconfigured model: {model_id}. Please check BEDROCK_MODEL_REGISTRY or token limits."}
        
        # Get inference profile ARN from environment variable (robust lookup)
        def model_id_to_env_var(model_id):
            return "BEDROCK_INFERENCE_PROFILE_ARN_" + re.sub(r'[^A-Za-z0-9]', '_', model_id).upper()
        env_var_name = model_id_to_env_var(model_id)
        inference_profile_arn = os.environ.get(env_var_name)

        # Only require and inject inferenceProfileArn for models that need it
        needs_inference_profile = ("meta" in model_id)

        if needs_inference_profile:
            if inference_profile_arn:
                body["inferenceProfileArn"] = inference_profile_arn
            else:
                print(f"⚠️ No inference profile ARN found for {model_id}, skipping injection.")
        
        # Make Bedrock request
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        response = bedrock.invoke_model(
            modelId=model_id,
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )
        
        # Extract result
        response_body = json.loads(response["body"].read())

        if "amazon.titan" in model_id:
            # Titan returns: { 'results': [ { 'outputText': ... } ] }
            try:
                content = response_body.get("results", [{}])[0].get("outputText", "")
            except Exception:
                content = str(response_body)
        elif "mistral.mistral-7b-instruct" in model_id or "deepseek.deepseek-coder" in model_id:
            # Mistral/DeepSeek: { 'outputs': [ { 'text': ... } ] }
            try:
                outputs = response_body.get("outputs", [{}])
                content = outputs[0].get("text", "") if outputs and isinstance(outputs[0], dict) else str(response_body)
            except Exception:
                content = str(response_body)
        else:
            content = str(response_body)

        # Try to extract JSON
        try:
            start_idx = content.find('{')
            end_idx = content.rfind('}') + 1
            if start_idx >= 0 and end_idx > start_idx:
                json_str = content[start_idx:end_idx]
                return json.loads(json_str)
            else:
                # Fall back to manual extraction
                scores = {}
                for category in ["completeness", "rationale_quality", "structure_quality"]:
                    match = re.search(rf"{category}.*?(\d+)", content, re.IGNORECASE)
                    if match:
                        scores[category] = int(match.group(1))
                
                # Extract explanations if possible
                for category in ["completeness", "rationale_quality", "structure_quality"]:
                    explanation_match = re.search(rf"{category}[^\n]*\n+([^\n#].*?)(?=\n\n|\n#|\Z)", content, re.DOTALL | re.IGNORECASE)
                    if explanation_match:
                        scores[f"{category}_explanation"] = explanation_match.group(1).strip()
                
                return scores
                
        except Exception as e:
            return {"error": f"Could not parse Bedrock response: {str(e)}", "raw": content}
    
    except Exception as e:
        return {"error": f"Bedrock error: {str(e)}"}

def score_outputs(md_paths):
    """
{{ ... }}
    Score outputs from a provided list of markdown file paths, using the same logic as evaluate_outputs.
    Returns evaluation results for report generation.
    """
    results = []
    for md_path in md_paths:
        with open(md_path, 'r') as f:
            content = f.read()
        # Extract framework name
        if 'normalized_b2_' in os.path.basename(md_path):
            framework = os.path.basename(md_path).replace('normalized_b2_', '').replace('_dynamic_orchestration.md', '')
        else:
            framework = os.path.basename(md_path).replace('b2_', '').replace('_dynamic_orchestration.md', '')
        print(f"Scoring: {framework} ({md_path})")
        # Score with Anthropic Claude
        try:
            claude_score = score_with_anthropic(content)
            claude_score["model"] = "claude-3-sonnet"
            print(f"  ✅ Claude scoring complete")
        except Exception as e:
            claude_score = {"error": str(e), "model": "claude-3-sonnet"}
            print(f"  ❌ Claude scoring failed: {e}")
        scores = [claude_score]
        # Score with Bedrock models if enabled
        if BEDROCK_ENABLED:
            for model_id, model_name in BEDROCK_MODELS:
                try:
                    print(f"  Scoring with Bedrock: {model_name}")
                    bedrock_score = score_with_bedrock(content, model_id)
                    bedrock_score["model"] = model_name
                    scores.append(bedrock_score)
                    print(f"  ✅ {model_name} scoring complete")
                except Exception as e:
                    print(f"  ❌ {model_name} scoring failed: {e}")
        results.append({
            "file": os.path.basename(md_path),
            "framework": framework,
            "scores": scores
        })
        time.sleep(1.5)  # Avoid rate limits
    return results

def normalize_outputs():
    """Normalize all framework outputs to standard format"""
    import subprocess
    try:
        print("\nRunning normalization script...")
        subprocess.run(["python", "normalize.py"], check=True)
        print("✅ Normalization complete")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Normalization failed: {e}")
        return False

def evaluate_outputs():
    """Score outputs with multiple models, using normalized files if available, else raw outputs."""
    print("\nEvaluating framework outputs...")
    # Prefer normalized files if they exist, else use raw output files
    normalized_files = glob(os.path.join(NORMALIZED_DIR, 'normalized_*_dynamic_orchestration.md'))
    if normalized_files:
        md_files = normalized_files
    else:
        # Fallback to raw output files
        md_files = glob(os.path.join(RESULTS_DIR, 'b2_*_dynamic_orchestration.md'))
    results = []
    
    for md_path in md_files:
        with open(md_path, 'r') as f:
            content = f.read()
        # Extract framework name
        if 'normalized_b2_' in os.path.basename(md_path):
            framework = os.path.basename(md_path).replace('normalized_b2_', '').replace('_dynamic_orchestration.md', '')
        else:
            framework = os.path.basename(md_path).replace('b2_', '').replace('_dynamic_orchestration.md', '')
        print(f"Scoring: {framework} ({md_path})")
        # Score with Anthropic Claude
        try:
            claude_score = score_with_anthropic(content)
            claude_score["model"] = "claude-3-sonnet"
            print(f"  ✅ Claude scoring complete")
        except Exception as e:
            claude_score = {"error": str(e), "model": "claude-3-sonnet"}
            print(f"  ❌ Claude scoring failed: {e}")
        scores = [claude_score]
        # Score with Bedrock models if enabled
        if BEDROCK_ENABLED:
            for model_id, model_name in BEDROCK_MODELS:
                try:
                    print(f"  Scoring with Bedrock: {model_name}")
                    bedrock_score = score_with_bedrock(content, model_id)
                    bedrock_score["model"] = model_name
                    scores.append(bedrock_score)
                    print(f"  ✅ {model_name} scoring complete")
                except Exception as e:
                    print(f"  ❌ {model_name} scoring failed: {e}")
        results.append({
            "file": os.path.basename(md_path),
            "framework": framework,
            "scores": scores
        })
        time.sleep(1.5)  # Avoid rate limits
    return results

# === REPORT GENERATION ===

def generate_report(framework_metrics, evaluation_results):
    """Generate comprehensive benchmark report"""
    with open(SUMMARY_REPORT, 'w') as f:
        f.write("# Multi-Agent Orchestration Benchmark Report\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        
        # Framework Performance Metrics
        f.write("## Performance Metrics\n\n")
        f.write("| Framework | Duration (s) | Agent Turns | Output Length | Message Count |\n")
        f.write("|-----------|--------------|-------------|----------------|----------------|\n")
        for framework, data in framework_metrics.items():
            messages = data.get("messages", [])
            message_count = len(messages) if isinstance(messages, list) else "?"
            f.write(f"| {framework.capitalize()} | {data['duration']} | {data['agent_turns']} | {data['output_length']} | {message_count} |\n")
        
        # Agent Selection Capabilities
        f.write("\n## Agent Selection Capabilities\n\n")
        f.write("| Framework | Filtered Irrelevant Agents | Analysis Method |\n")
        for framework, data in framework_metrics.items():
            f.write(f"| {framework.capitalize()} | {data.get('filtered_irrelevant_agents', '?')} | {data.get('agent_filtering_details', '?')} |\n")
        
        # Quality Assessment
        f.write("\n## Quality Assessment\n\n")
        f.write("| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |\n")
        f.write("|-----------|--------------|-------------------|-------------------|------------------------|\n")
        
        # Aggregate scores across evaluators
        framework_avg_scores = {}
        baseball_score_map = {0: 0, 1: 3, 2: 5}
        for result in evaluation_results:
            framework = result["framework"]
            valid_scores = [s for s in result["scores"] if "error" not in s]
            
            if valid_scores:
                # Calculate averages
                completeness_avg = sum(int(s.get("completeness", 0)) for s in valid_scores) / len(valid_scores)
                rationale_avg = sum(int(s.get("rationale_quality", 0)) for s in valid_scores) / len(valid_scores)
                structure_avg = sum(int(s.get("structure_quality", 0)) for s in valid_scores) / len(valid_scores)
                
                # Get baseball handling from Claude (more reliable)
                claude_score = next((s for s in result["scores"] if s.get("model") == "claude-3-sonnet"), {})
                baseball = claude_score.get("baseball_coach_handling", "?")
                baseball_rating = {0: "Not mentioned", 1: "Mentioned", 2: "Properly excluded"}
                # Normalize baseball score to 5-point scale
                baseball_display = f"{baseball_score_map.get(baseball, '?')}/5 ({baseball_rating.get(baseball, 'Unknown')})"
                
                f.write(f"| {framework.capitalize()} | {completeness_avg:.2f}/5 | {rationale_avg:.2f}/5 | {structure_avg:.2f}/5 | {baseball_display} |\n")
                
                # Store for ranking
                framework_avg_scores[framework] = {
                    "completeness": completeness_avg,
                    "rationale_quality": rationale_avg,
                    "structure_quality": structure_avg,
                    "total": completeness_avg + rationale_avg + structure_avg
                }
            else:
                f.write(f"| {framework.capitalize()} | ERROR | ERROR | ERROR | ERROR |\n")
        
        # Framework Rankings
        if framework_avg_scores:
            f.write("\n## Framework Rankings\n\n")
            rankings = sorted(framework_avg_scores.items(), key=lambda x: x[1]["total"], reverse=True)
            f.write("| Rank | Framework | Total Score | Completeness | Rationale | Structure |\n")
            f.write("|------|-----------|-------------|--------------|-----------|----------|\n")
            for i, (fw, scores) in enumerate(rankings, 1):
                f.write(f"| {i} | {fw.capitalize()} | {scores['total']:.2f}/15 | {scores['completeness']:.2f}/5 | {scores['rationale_quality']:.2f}/5 | {scores['structure_quality']:.2f}/5 |\n")

        # Model Scores by Framework
        f.write("\n## Model Scores by Framework\n\n")
        f.write("| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |\n")
        f.write("|-----------|-------|--------------|-------------------|-------------------|-------|\n")
        # Collect per-framework per-model scores for averaging
        framework_model_totals = {}
        for result in evaluation_results:
            framework = result["framework"]
            for s in result["scores"]:
                if "error" in s:
                    continue
                model = s.get("model", "?")
                completeness = int(s.get("completeness", 0))
                rationale = int(s.get("rationale_quality", 0))
                structure = int(s.get("structure_quality", 0))
                total = completeness + rationale + structure
                f.write(f"| {framework.capitalize()} | {model} | {completeness}/5 | {rationale}/5 | {structure}/5 | {total}/15 |\n")
                framework_model_totals.setdefault(framework, []).append(total)
        # Final Average Score per framework
        f.write("\n### Final Average Score by Framework (across all models)\n\n")
        f.write("| Framework | Average Score (All Models) |\n")
        f.write("|-----------|--------------------------|\n")
        for framework, totals in framework_model_totals.items():
            avg = sum(totals) / len(totals) if totals else 0
            f.write(f"| {framework.capitalize()} | {avg:.2f}/15 |\n")

        # Testing Methodology
        f.write("\n## Testing Methodology\n\n")
        f.write("All frameworks were tested with:\n\n")
        f.write("- Identical system prompts for each agent role\n")
        f.write("- Same user objective\n")
        f.write("- Equal access to agent roles including the irrelevant BaseballCoachAgent\n")
        f.write("- Evaluation by multiple LLM models\n\n")
        
        # Framework-Specific Observations
        f.write("### Framework-Specific Observations\n\n")
        for framework, data in framework_metrics.items():
            f.write(f"#### {framework.capitalize()}\n\n")
            
            # Add observations about BaseballCoachAgent handling
            if data["filtered_irrelevant_agents"] == "Yes":
                f.write("- Successfully filtered out the irrelevant BaseballCoachAgent\n")
                context = "explicitly states it was excluded" if "explicitly" in data["agent_filtering_details"] else "did not use the BaseballCoachAgent"
                f.write(f"- The output {context}\n")
            else:
                f.write("- Failed to filter out the irrelevant BaseballCoachAgent\n")
                f.write("- The BaseballCoachAgent participated in the conversation despite being irrelevant\n")
            
            # Add observations about performance metrics
            f.write(f"- Completed in {data['duration']} seconds with {data['agent_turns']} agent turns\n")
            f.write("\n")
        
        # Detailed Evaluations
        f.write("\n---\n\n## Detailed Evaluations\n\n")
        baseball_score_map = {0: 0, 1: 3, 2: 5}
        for result in evaluation_results:
            framework = result["framework"].capitalize()
            f.write(f"### {framework}\n\n")
            
            for score in result["scores"]:
                model = score.get("model", "Unknown")
                f.write(f"#### Evaluation by {model}\n\n")
                
                if 'error' in score:
                    f.write(f"**ERROR:** {score['error']}\n\n")
                    if 'raw' in score:
                        f.write(f"**Raw Output:**\n```\n{score['raw'][:500]}...\n```\n\n")
                else:
                    f.write(f"**Completeness:** {score.get('completeness', '?')}/5\n{score.get('completeness_explanation', 'No explanation provided.')}\n\n")
                    f.write(f"**Rationale Quality:** {score.get('rationale_quality', '?')}/5\n{score.get('rationale_explanation', 'No explanation provided.')}\n\n")
                    f.write(f"**Structure Quality:** {score.get('structure_quality', '?')}/5\n{score.get('structure_explanation', 'No explanation provided.')}\n\n")
                    
                    baseball = score.get('baseball_coach_handling', '?')
                    if baseball == 2:
                        baseball_text = "BaseballCoachAgent was properly excluded with explanation"
                    elif baseball == 1:
                        baseball_text = "BaseballCoachAgent was mentioned but not properly explained"
                    elif baseball == 0:
                        baseball_text = "BaseballCoachAgent was not mentioned at all"
                    else:
                        baseball_text = "Unknown BaseballCoachAgent handling"
                    
                    f.write(f"**BaseballCoachAgent Handling:** {baseball_text} — Score: {baseball_score_map.get(baseball, '?')}/5\n\n")
                    
                    if all(k in score for k in ['completeness', 'rationale_quality', 'structure_quality']):
                        total = int(score['completeness']) + int(score['rationale_quality']) + int(score['structure_quality'])
                        f.write(f"**Total Score: {total}/15**\n\n")
            
            # Key output examples
            framework_key = framework.lower()
            if framework_key in framework_metrics:
                # BaseballCoach handling examples
                if framework_key == "autogen":
                    f.write("#### BaseballCoachAgent Handling Examples\n\n")

                    # Extract BaseballCoachAgent messages from framework_metrics
                    autogen_messages = framework_metrics.get("autogen", {}).get("messages", [])
                    baseball_messages = [m for m in autogen_messages if m.get("name") == "BaseballCoachAgent"]
                    if baseball_messages:
                        f.write(f"BaseballCoachAgent was used and sent {len(baseball_messages)} messages.\n")
                        f.write(f"First message: ```\n{baseball_messages[0].get('content', '')[:200]}...\n```\n\n")
                    else:
                        f.write("BaseballCoachAgent was not used in the conversation.\n\n")
                else:
                    # For other frameworks, use regex to find mentions
                    output = framework_metrics[framework_key]["output"]
                    baseball_context = re.search(r'[^.]*?Baseball\s*Coach\s*Agent[^.]*\.', output, re.IGNORECASE)
                    if baseball_context:
                        f.write("#### BaseballCoachAgent Handling Examples\n\n")
                        f.write(f"```\n{baseball_context.group(0)}\n```\n\n")
        # Append date/time at the end of the report
        f.write(f"\n---\n\nReport finalized: {datetime.now().isoformat()}\n")
    # === PLOT TRENDS ===
    def plot_score_trends(evaluation_results):
        import numpy as np
        import matplotlib.pyplot as plt
        import webbrowser

        frameworks = []
        completeness_scores = []
        rationale_scores = []
        structure_scores = []
        model_counts = []

        # Standard deviation lists
        completeness_stds = []
        rationale_stds = []
        structure_stds = []

        for result in evaluation_results:
            framework = result["framework"]
            valid_scores = [s for s in result["scores"] if "error" not in s]
            if valid_scores:
                c_scores = [int(s.get("completeness", 0)) for s in valid_scores]
                r_scores = [int(s.get("rationale_quality", 0)) for s in valid_scores]
                s_scores = [int(s.get("structure_quality", 0)) for s in valid_scores]

                completeness_avg = np.mean(c_scores)
                rationale_avg = np.mean(r_scores)
                structure_avg = np.mean(s_scores)

                completeness_std = np.std(c_scores)
                rationale_std = np.std(r_scores)
                structure_std = np.std(s_scores)

                frameworks.append(framework)
                completeness_scores.append(completeness_avg)
                rationale_scores.append(rationale_avg)
                structure_scores.append(structure_avg)

                completeness_stds.append(completeness_std)
                rationale_stds.append(rationale_std)
                structure_stds.append(structure_std)

                model_counts.append(len(valid_scores))

        plt.figure(figsize=(10, 6))
        x = np.arange(len(frameworks))
        width = 0.25

        plt.bar(x - width, completeness_scores, width, yerr=completeness_stds, capsize=5, label='Completeness')
        plt.bar(x, rationale_scores, width, yerr=rationale_stds, capsize=5, label='Rationale Quality')
        plt.bar(x + width, structure_scores, width, yerr=structure_stds, capsize=5, label='Structure Quality')

        for i, count in enumerate(model_counts):
            plt.text(i, max(completeness_scores[i], rationale_scores[i], structure_scores[i]) + 0.2,
                     f"{count} models", ha='center', fontsize=8)

        plt.xticks(x, frameworks, rotation=30)
        plt.ylim(0, 5.5)
        plt.title("Framework Evaluation Trends (Avg ± Std Dev)")
        plt.xlabel("Framework")
        plt.ylabel("Score")
        plt.legend()
        plt.grid(True, axis='y')
        plt.tight_layout()

        chart_path = os.path.join(RESULTS_DIR, 'score_trends.png')
        plt.savefig(chart_path)
        print(f"📊 Trend chart saved to: {chart_path}")
        webbrowser.open(f"file://{chart_path}")

    plot_score_trends(evaluation_results)
    print(f"\n✅ Benchmark report written to {SUMMARY_REPORT}")

# === MAIN ===
def main():
    if args.score_only:
        # Only run scoring/evaluation on existing outputs
        if args.output_dir:
            results_dir = os.path.abspath(args.output_dir)
        else:
            # Use latest_run symlink
            PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
            RESULTS_PARENT = os.path.join(PROJECT_ROOT, 'results', 'benchmark2')
            latest_symlink = os.path.join(RESULTS_PARENT, 'latest_run')
            results_dir = os.path.realpath(latest_symlink) if os.path.exists(latest_symlink) else None
        if not results_dir or not os.path.exists(results_dir):
            print(f"❌ Could not find results directory: {results_dir}")
            sys.exit(1)
        # Find output markdown files (run folder only)
        md_paths = sorted(glob(os.path.join(results_dir, 'b2_*_dynamic_orchestration.md')))
        if not md_paths:
            print(f"❌ No framework output markdown files found in {results_dir}")
            sys.exit(1)
        print(f"🔄 Scoring the following output files:")
        for p in md_paths:
            print(f"  - {p}")
        # Minimal framework_metrics for reporting
        framework_metrics = {}
        # Try to reconstruct metrics from output files (basic)
        for p in md_paths:
            framework = os.path.basename(p).split('_')[1].lower()
            with open(p, 'r') as f:
                content = f.read()
            duration_match = re.search(r"\*\*Time to complete:\*\* ([\d.]+) seconds", content)
            turns_match = re.search(r"\*\*Agent turns:\*\* (\d+)", content)
            duration = float(duration_match.group(1)) if duration_match else "?"
            turns = int(turns_match.group(1)) if turns_match else "?"

            framework_metrics[framework] = {
                'output': content,
                'duration': duration,
                'agent_turns': turns,
                'output_length': len(content),
                'filtered_irrelevant_agents': '?',
                'agent_filtering_details': '?',
}
        # Score outputs
        evaluation_results = score_outputs(md_paths)
        generate_report(framework_metrics, evaluation_results)
        print("\n✅ Re-scoring complete.")
        return

    # Run all framework tests
    framework_metrics = run_all_framework_tests()
    # Normalize output files
    normalize_success = normalize_outputs()
    if not normalize_success:
        print("⚠️ Continuing with evaluation despite normalization issues.")
    # Score outputs
    evaluation_results = evaluate_outputs()
    # Generate comprehensive report
    generate_report(framework_metrics, evaluation_results)

if __name__ == '__main__':
    main()