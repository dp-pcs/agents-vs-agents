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
run_dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

if args.output_dir:
    RESULTS_DIR = os.path.abspath(args.output_dir)
else:
    # Always create results under the project root /results/benchmark2
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
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
SUMMARY_REPORT = os.path.join(RESULTS_DIR, f'benchmark_report_{run_dt_str}.md')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_MODEL = 'claude-3-sonnet-20240229'

# Bedrock config for multi-model scoring
from src.shared.scoring_utils import score_with_bedrock
from tools.bedrock_models_validated import LLM_MODELS as BEDROCK_MODELS
BEDROCK_ENABLED = os.getenv('AWS_ACCESS_KEY_ID') is not None

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
    autogen_final_output_text = str(results["autogen"].get("output", "")).lower()
    autogen_messages = results["autogen"].get("messages", []) # Ensure we get it from results dict
    
    # Primary check: Does the final output explicitly state exclusion?
    # Normalize phrases by removing spaces for more robust matching against potentially varied phrasing
    normalized_autogen_output = autogen_final_output_text.replace(" ", "")
    exclusion_phrases_normalized = [
        "chosenottoinvolveagentssuchasbaseballcoachagent",
        "chosonottoinvolvebaseballcoachagent", # Common typo
        "baseballcoachagentwasnotused",
        "baseballcoachagentisirrelevant",
        "excludedbaseballcoachagent",
        "didnotinvolvebaseballcoachagent"
    ]
    
    explicitly_excluded_in_output = any(phrase in normalized_autogen_output for phrase in exclusion_phrases_normalized)

    if explicitly_excluded_in_output:
        results["autogen"]["filtered_irrelevant_agents"] = "Yes"
        results["autogen"]["agent_filtering_details"] = (
            "Detection method: Final output analysis.\n"
            "BaseballCoachAgent was explicitly mentioned as excluded or not used in the final output."
        )
    else:
        # Fallback to message-level analysis if not explicitly excluded in output
        autogen_baseball_messages = [m for m in autogen_messages if m.get("name") == "BaseballCoachAgent"]
        if autogen_baseball_messages:
            results["autogen"]["filtered_irrelevant_agents"] = "No"
            results["autogen"]["agent_filtering_details"] = (
                "Detection method: Message-level analysis (fallback).\n"
                "BaseballCoachAgent was not explicitly excluded in final output AND "
                f"appears to have messages ({len(autogen_baseball_messages)}) in the transcript, suggesting it might have participated or its messages were not fully suppressed."
            )
        else:
            results["autogen"]["filtered_irrelevant_agents"] = "Yes"
            results["autogen"]["agent_filtering_details"] = (
                "Detection method: Final output and message-level analysis.\n"
                "BaseballCoachAgent was not explicitly excluded in final output, but also sent no messages, suggesting it was effectively filtered out."
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

def score_outputs(md_paths):
    """
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

        # Score with OpenAI GPT
        try:
            from src.shared.scoring_utils import score_with_openai
            openai_score = score_with_openai(content)
            openai_score["model"] = "gpt-4o"
            print(f"  ✅ OpenAI scoring complete")
        except Exception as e:
            openai_score = {"error": str(e), "model": "gpt-4o"}
            print(f"  ❌ OpenAI scoring failed: {e}")

        scores = [claude_score, openai_score]

        # Average scores if both succeeded
        avg_score = {}
        score_keys = ["completeness", "rationale_quality", "structure_quality"]
        valid_scores = [s for s in scores if all(k in s and isinstance(s[k], (int, float)) for k in score_keys)]
        if len(valid_scores) == 2:
            for k in score_keys:
                avg_score[k] = (float(claude_score[k]) + float(openai_score[k])) / 2
            avg_score["model"] = "average"
            scores.append(avg_score)
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

        # Score with OpenAI GPT
        try:
            from src.shared.scoring_utils import score_with_openai
            openai_score = score_with_openai(content)
            openai_score["model"] = "gpt-4o"
            print(f"  ✅ OpenAI scoring complete")
        except Exception as e:
            openai_score = {"error": str(e), "model": "gpt-4o"}
            print(f"  ❌ OpenAI scoring failed: {e}")

        scores = [claude_score, openai_score]

        # Average scores if both succeeded
        avg_score = {}
        score_keys = ["completeness", "rationale_quality", "structure_quality"]
        valid_scores = [s for s in scores if all(k in s and isinstance(s[k], (int, float)) for k in score_keys)]
        if len(valid_scores) == 2:
            for k in score_keys:
                avg_score[k] = (float(claude_score[k]) + float(openai_score[k])) / 2
            avg_score["model"] = "average"
            scores.append(avg_score)
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
        f.write("| Framework | Duration (s) | Agent Turns | Output Length |\n")
        f.write("|-----------|--------------|-------------|----------------|\n")
        for framework, data in framework_metrics.items():
            f.write(f"| {framework.capitalize()} | {data['duration']} | {data['agent_turns']} | {data['output_length']} |\n")
        
        # Populate framework_ranking_data with average scores for the Quality Assessment table
        framework_ranking_data = {}
        for res_idx, res_item in enumerate(evaluation_results):
            framework_name = res_item["framework"]
            # Try to get the 'average' score calculated by evaluate_outputs
            avg_score_entry = next((s for s in res_item["scores"] if s.get("model") == "average"), None)

            if avg_score_entry and "error" not in avg_score_entry:
                comp = avg_score_entry.get("completeness", 0)
                rat = avg_score_entry.get("rationale_quality", 0)
                stru = avg_score_entry.get("structure_quality", 0)
                framework_ranking_data[framework_name] = {
                    "completeness": comp,
                    "rationale_quality": rat,
                    "structure_quality": stru,
                    "total": comp + rat + stru  # Total for the average
                }
            else:
                # Fallback: If 'average' entry is missing or errored, calculate average from available valid individual model scores
                valid_individual_scores = [s_ind for s_ind in res_item["scores"] if s_ind.get("model") in VALID_SCORING_MODELS and "error" not in s_ind]
                if valid_individual_scores:
                    comp_sum = sum(s_ind.get("completeness", 0) for s_ind in valid_individual_scores)
                    rat_sum = sum(s_ind.get("rationale_quality", 0) for s_ind in valid_individual_scores)
                    stru_sum = sum(s_ind.get("structure_quality", 0) for s_ind in valid_individual_scores)
                    num_valid = len(valid_individual_scores)
                    avg_comp = comp_sum / num_valid
                    avg_rat = rat_sum / num_valid
                    avg_stru = stru_sum / num_valid
                    framework_ranking_data[framework_name] = {
                        "completeness": avg_comp,
                        "rationale_quality": avg_rat,
                        "structure_quality": avg_stru,
                        "total": avg_comp + avg_rat + avg_stru
                    }
                else:
                    # No valid scores to average for this framework
                    framework_ranking_data[framework_name] = {
                        "completeness": 0, "rationale_quality": 0, "structure_quality": 0, "total": 0, "error": True
                    }
        
        # Quality Assessment Table (Averages)
        f.write("\n## Quality Assessment (Claude & OpenAI Average)\n\n")
        f.write("| Framework | Avg Completeness | Avg Rationale | Avg Structure | Avg Total Score (out of 15) |\n")
        f.write("|-----------|------------------|---------------|---------------|---------------------------|\n")
        for fw_name, avg_data in framework_ranking_data.items():
            if avg_data.get("error"):
                f.write(f"| {fw_name.capitalize()} | ERROR | ERROR | ERROR | ERROR |\n")
            else:
                f.write(f"| {fw_name.capitalize()} | {avg_data['completeness']:.2f}/5 | {avg_data['rationale_quality']:.2f}/5 | {avg_data['structure_quality']:.2f}/5 | {avg_data['total']:.2f}/15 |\n")

        # Framework Rankings (Based on Averaged Scores from Claude & OpenAI)
        # This uses the same framework_ranking_data, which is now correctly populated with 3 criteria totals.
        if framework_ranking_data:
            f.write("\n## Framework Rankings (Claude & OpenAI Average)\n\n")
            rankings = sorted(framework_ranking_data.items(), key=lambda x: x[1]["total"], reverse=True)
            f.write("| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |\n")
            f.write("|------|-----------|------------------|-------------------|----------------|----------------|\n")
            for i, (fw, scores) in enumerate(rankings, 1):
                f.write(f"| {i} | {fw.capitalize()} | {scores['total']:.2f}/15 | {scores['completeness']:.2f}/5 | {scores['rationale_quality']:.2f}/5 | {scores['structure_quality']:.2f}/5 |\n")

        # Individual Model Scores by Framework (Claude & OpenAI)
        # This table shows scores from each individual model (not averages)
        f.write("\n## Individual Model Scores by Framework (Claude & OpenAI)\n\n")
        f.write("| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total Score (out of 15) |\n")
        f.write("|-----------|-------|--------------|-------------------|-------------------|-------------------------|\n")
        
        # This final_avg_scores_data is for the *next* table (Final Average Score per framework)
        # It should be populated based on the individual model scores for each framework
        final_avg_scores_data = {} 
        for res_item in evaluation_results:
            framework_name = res_item["framework"]
            scores_for_current_framework = []
            for score_entry in res_item["scores"]:
                model_name = score_entry.get("model")
                # We only want to list individual models here, not the 'average' entry
                if model_name in VALID_SCORING_MODELS and "error" not in score_entry:
                    comp = float(score_entry.get("completeness", 0))
                    rat = float(score_entry.get("rationale_quality", 0))
                    stru = float(score_entry.get("structure_quality", 0))
                    total_score = comp + rat + stru
                    f.write(f"| {framework_name.capitalize()} | {model_name} | {comp:.0f}/5 | {rat:.0f}/5 | {stru:.0f}/5 | {total_score:.0f}/15 |\n")
                    scores_for_current_framework.append(total_score) # Collect totals for averaging later
                elif model_name in VALID_SCORING_MODELS and "error" in score_entry:
                    f.write(f"| {framework_name.capitalize()} | {model_name} | ERROR | ERROR | ERROR | ERROR |\n")
            
            if scores_for_current_framework: # if there were any valid scores for this framework
                final_avg_scores_data[framework_name] = sum(scores_for_current_framework) / len(scores_for_current_framework)
            else:
                final_avg_scores_data[framework_name] = 0 # Default if no valid scores

        # Final Average Score per framework (Claude & OpenAI) - This table uses the averages calculated above
        f.write("\n### Final Average Score by Framework (Claude & OpenAI)\n\n")
        f.write("| Framework | Average Score (Claude & OpenAI) |\n")
        f.write("|-----------|-------------------------------|\n")
        for framework_name, avg_total_score in final_avg_scores_data.items():
            f.write(f"| {framework_name.capitalize()} | {avg_total_score:.2f}/15 |\n")

        # Testing Methodology
        f.write("\n## Testing Methodology\n\n")
        f.write("All frameworks were tested with:\n\n")
        f.write("- Identical system prompts for each agent role\n")
        f.write("- Same user objective\n")
        f.write("- Equal access to agent roles including the irrelevant BaseballCoachAgent\n")
        f.write("- Evaluation by multiple LLM models\n\n")
        
        # Agent Engagement Decisions & Performance Metrics
        f.write("### Agent Engagement Decisions & Performance Metrics\n\n")
        for framework, data in framework_metrics.items():
            f.write(f"#### {framework.capitalize()}\n\n")
            
            # Report on BaseballCoachAgent engagement decision
            engagement_decision = "Yes (Correctly Handled)" if data.get("filtered_irrelevant_agents") == "Yes" else "No (Incorrectly Handled)"
            f.write(f"- **Agent Engagement Decision (BaseballCoachAgent):** {engagement_decision}\n")
            filtering_details = data.get("agent_filtering_details", "Details not available.")
            # Clean up the details text a bit for better readability
            filtering_details = filtering_details.replace("Detection method: Final output analysis.\n", "Note: ")
            filtering_details = filtering_details.replace("Detection method: Message-level analysis (fallback).\n", "Note: ")
            filtering_details = filtering_details.replace("Detection method: Final output and message-level analysis.\n", "Note: ")
            f.write(f"  - {filtering_details.strip()}\n")
            
            # Add observations about performance metrics
            f.write(f"- **Performance:** Completed in {data['duration']:.2f} seconds with {data['agent_turns']} agent turns\n")
            # Add message count if available (especially for Autogen)
            if "messages" in data and isinstance(data["messages"], list):
                f.write(f"  - Total messages exchanged: {len(data['messages'])}\n")
            f.write("\n")

        # Detailed Evaluations
        f.write("\n---\n\n## Detailed Evaluations\n\n")
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
                    completeness_val = score.get('completeness')
                    rationale_val = score.get('rationale_quality')
                    structure_val = score.get('structure_quality')

                    f.write(f"**Completeness:** {completeness_val if isinstance(completeness_val, (int,float)) else '?'}/5\n{score.get('completeness_explanation', 'No explanation provided.')}\n\n")
                    f.write(f"**Rationale Quality:** {rationale_val if isinstance(rationale_val, (int,float)) else '?'}/5\n{score.get('rationale_explanation', 'No explanation provided.')}\n\n")
                    f.write(f"**Structure Quality:** {structure_val if isinstance(structure_val, (int,float)) else '?'}/5\n{score.get('structure_explanation', 'No explanation provided.')}\n\n")
                    
                    # Calculate Total Score out of 15
                    if isinstance(completeness_val, (int, float)) and isinstance(rationale_val, (int, float)) and isinstance(structure_val, (int, float)):
                        total = float(completeness_val) + float(rationale_val) + float(structure_val)
                        f.write(f"**Total Score: {total:.0f}/15**\n\n")
                    else:
                        f.write(f"**Total Score: ?/15** (One or more scores missing/invalid for summation)\n\n")
            
            # Key output examples section removed as BaseballCoachAgent handling is no longer part of detailed LLM scoring
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