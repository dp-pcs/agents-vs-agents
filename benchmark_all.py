import os
import sys
import time
import json
import re
import requests
from glob import glob
from datetime import datetime

# Add paths to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'runners/Test2'))

# Import the testing functions from each framework
from v2_runner_autogen import run_autogen_test
from v2_runner_crewai import run_crewai_test
from v2_runner_langgraph import run_langgraph_test

# === CONFIG ===
RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')
NORMALIZED_DIR = os.path.join(RESULTS_DIR, 'normalized')
SUMMARY_REPORT = os.path.join(RESULTS_DIR, 'benchmark_report.md')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_MODEL = 'claude-3-sonnet-20240229'

# === AWS Credentials Check ===
def check_aws_credentials():
    """Check if AWS credentials from SAM2AWS are available and usable"""
    try:
        import boto3
        # Try to create a simple client to test credentials
        sts = boto3.client('sts')
        # Get caller identity will fail if credentials are not valid
        identity = sts.get_caller_identity()
        print(f"✅ AWS credentials found for account: {identity['Account']}")
        return True
    except Exception as e:
        print(f"❌ AWS credentials not available or invalid: {e}")
        print("   Using only Claude API for evaluation.")
        return False

# === FRAMEWORK TESTING ===
def run_all_framework_tests():
    """Run all framework tests and gather metrics"""
    print("=" * 50)
    print("RUNNING STANDARDIZED AGENT FRAMEWORK COMPARISON")
    print("=" * 50)
    
    # Run all tests and collect results
    results = {}
    
    print("\n\n=== AUTOGEN TEST ===\n")
    autogen_output, autogen_duration, autogen_turns = run_autogen_test()
    
    # Get BaseballCoachAgent usage info from analyzing the output text
    results["autogen"] = {
        "duration": autogen_duration,
        "agent_turns": autogen_turns,
        "output_length": len(autogen_output) if autogen_output else 0,
        "output": autogen_output  # Store the actual output for analysis
    }
    
    # Check if BaseballCoach appears in the output
    if "BaseballCoachAgent" in autogen_output:
        # Check if it's mentioned in the context of being excluded
        if any(phrase in autogen_output.lower() for phrase in [
            "not use baseballcoachagent", 
            "not involve baseball", 
            "excluded baseball", 
            "irrelevant baseball",
            "not relevant baseball",
            "was correctly identified as irrelevant",
            "was correctly filtered out"
        ]):
            # It was mentioned in the context of being excluded
            results["autogen"]["filtered_irrelevant_agents"] = "Yes"
            results["autogen"]["agent_filtering_details"] = (
                "Detection method: Text analysis.\n"
                "BaseballCoachAgent was mentioned but in context of being excluded."
            )
        else:
            # It appears to have been used
            results["autogen"]["filtered_irrelevant_agents"] = "No"
            results["autogen"]["agent_filtering_details"] = (
                "Detection method: Text analysis.\n"
                "BaseballCoachAgent appears to have been used despite being irrelevant."
            )
    else:
        # Not mentioned at all
        results["autogen"]["filtered_irrelevant_agents"] = "Yes"  
        results["autogen"]["agent_filtering_details"] = (
            "Detection method: Text analysis.\n"
            "BaseballCoachAgent was not mentioned, suggesting it was filtered out."
        )
    
    print("\n\n=== CREWAI TEST ===\n")
    crewai_output, crewai_duration, crewai_turns = run_crewai_test()
    # Fix for CrewAI agent turns - count major sections as a proxy for agent contributions
    crewai_section_count = len(re.findall(r'##? [A-Za-z\s&]+\n', str(crewai_output)))
    if crewai_turns == 0 and crewai_section_count > 0:
        crewai_turns = crewai_section_count
        print(f"[INFO] CrewAI agent turns updated from 0 to {crewai_turns} based on section count")
    
    results["crewai"] = {
        "duration": crewai_duration,
        "agent_turns": crewai_turns,
        "output_length": len(crewai_output) if crewai_output else 0,
        "output": crewai_output  # Store the actual output for analysis
    }
    
    # Check if BaseballCoach appears in the output
    if "Baseball Coach" in str(crewai_output):
        # Check if it's mentioned in the context of being excluded
        if any(phrase in str(crewai_output).lower() for phrase in [
            "not use baseball", 
            "not involve baseball", 
            "excluded baseball", 
            "irrelevant baseball",
            "not relevant baseball",
            "was not involved",
            "was not used",
            "baseballcoachagent was not"
        ]):
            # It was mentioned in the context of being excluded
            results["crewai"]["filtered_irrelevant_agents"] = "Yes"
            results["crewai"]["agent_filtering_details"] = (
                "Detection method: Text analysis.\n"
                "BaseballCoachAgent was mentioned but in context of being excluded."
            )
        else:
            # It appears to have been used
            results["crewai"]["filtered_irrelevant_agents"] = "No"
            results["crewai"]["agent_filtering_details"] = (
                "Detection method: Text analysis.\n"
                "BaseballCoachAgent appears to have been used despite being irrelevant."
            )
    else:
        # Not mentioned at all
        results["crewai"]["filtered_irrelevant_agents"] = "Yes"  
        results["crewai"]["agent_filtering_details"] = (
            "Detection method: Text analysis.\n"
            "BaseballCoachAgent was not mentioned, suggesting it was filtered out."
        )
    
    print("\n\n=== LANGGRAPH TEST ===\n")
    langgraph_output, langgraph_duration, langgraph_turns = run_langgraph_test()
    results["langgraph"] = {
        "duration": langgraph_duration,
        "agent_turns": langgraph_turns,
        "output_length": len(langgraph_output) if langgraph_output else 0,
        "output": langgraph_output  # Store the actual output for analysis
    }
    
    # Check if BaseballCoach appears in the output
    if "BaseballCoachAgent" in str(langgraph_output):
        # Check if it's mentioned in the context of being excluded
        if any(phrase in str(langgraph_output).lower() for phrase in [
            "not use baseball", 
            "not involve baseball", 
            "excluded baseball", 
            "irrelevant baseball",
            "not relevant baseball",
            "chose not to involve",
            "was not used"
        ]):
            # It was mentioned in the context of being excluded
            results["langgraph"]["filtered_irrelevant_agents"] = "Yes"
            results["langgraph"]["agent_filtering_details"] = (
                "Detection method: Text analysis.\n"
                "BaseballCoachAgent was mentioned but in context of being excluded."
            )
        else:
            # It appears to have been used
            results["langgraph"]["filtered_irrelevant_agents"] = "No"
            results["langgraph"]["agent_filtering_details"] = (
                "Detection method: Text analysis.\n"
                "BaseballCoachAgent appears to have been used despite being irrelevant."
            )
    else:
        # Not mentioned at all
        results["langgraph"]["filtered_irrelevant_agents"] = "Yes"  
        results["langgraph"]["agent_filtering_details"] = (
            "Detection method: Text analysis.\n"
            "BaseballCoachAgent was not mentioned, suggesting it was filtered out."
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

def score_with_anthropic(plan_md):
    """Score plan using Anthropic Claude API"""
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
                if "baseball_coach_handling" not in j:
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
            
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

def score_with_bedrock(plan_md, model_id):
    """Score plan using AWS Bedrock models with SAM2AWS credentials"""
    try:
        import boto3
        import botocore
        
        # Truncate content to fit model limits
        truncated_plan = plan_md[:10000]  # Adjust depending on model token limits
        
        # Prepare prompt
        prompt = SCORING_PROMPT + "\n\nBusiness Plan:\n" + truncated_plan
        
        # Format request based on model type
        if "anthropic" in model_id:
            body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "temperature": 0.2,
                "messages": [{"role": "user", "content": prompt}]
            }
        elif "meta.llama" in model_id:
            body = {
                "prompt": prompt,
                "max_gen_len": 1000,
                "temperature": 0.2
            }
        else:
            return {"error": f"Unsupported model: {model_id}"}
        
        # Create session with explicit credential handling that works with SAM2AWS
        session = boto3.Session()
        
        # Make Bedrock request with explicit region
        bedrock = session.client(
            "bedrock-runtime", 
            region_name="us-east-1",
            # Use existing credentials from SAM2AWS-created session
            config=botocore.config.Config(
                retries={"max_attempts": 2, "mode": "standard"},
                connect_timeout=30,
                read_timeout=30
            )
        )
        
        print(f"  Calling Bedrock with model: {model_id}")
        response = bedrock.invoke_model(
            modelId=model_id,
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )
        
        # Extract result
        response_body = json.loads(response["body"].read())
        
        if "anthropic" in model_id:
            content = response_body.get("content", [])
            if isinstance(content, list) and len(content) > 0 and "text" in content[0]:
                content = content[0]["text"]
            else:
                content = str(content)
        elif "meta.llama" in model_id:
            content = response_body.get("generation", "")
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
                
                if scores:
                    return scores
                else:
                    return {"error": "Could not extract scores from response", "raw": content[:500]}
                
        except Exception as e:
            return {"error": f"Could not parse Bedrock response: {str(e)}", "raw": content[:500]}
    
    except Exception as e:
        print(f"  ❌ Bedrock error: {str(e)}")
        return {"error": f"Bedrock error: {str(e)}"}

# === NORMALIZATION AND EVALUATION ===

def normalize_outputs():
    """Normalize all framework outputs to standard format"""
    print("\nNormalizing framework outputs...")
    
    # Create normalized directory
    os.makedirs(NORMALIZED_DIR, exist_ok=True)
    
    # Get list of files to normalize
    input_files = glob(os.path.join(RESULTS_DIR, "b2_*_dynamic_orchestration.md"))
    if not input_files:
        print("❌ No files found to normalize")
        return False
    
    print(f"Found {len(input_files)} files to normalize")
    
    for input_path in input_files:
        try:
            filename = os.path.basename(input_path)
            output_path = os.path.join(NORMALIZED_DIR, f"normalized_{filename}")
            
            # Extract framework name for specific processing
            framework = re.search(r'b2_(\w+)_dynamic', filename).group(1)
            print(f"  Normalizing {framework} output...")
            
            with open(input_path, 'r') as f:
                content = f.read()
            
            # Remove timestamp line and other metadata
            content = re.sub(r'^Generated:.*?\n', '', content)
            
            # Remove time tracking info at the end
            content = re.sub(r'\n\n\*\*Time to complete.*', '', content)
            content = re.sub(r'\n\n\*\*Agent turns.*', '', content)
            
            # Framework-specific processing
            if framework == "autogen":
                # Clean up autogen specific patterns
                content = re.sub(r'<\|.*?\|>', '', content)  # Remove marker tags
                content = re.sub(r'$$MESSAGE.*?\n', '', content)  # Remove message headers
                
                # Try to extract just the final business plan
                plan_match = re.search(r'(?:# Business Plan for|# Final Business Plan).*?(?=\Z)', content, re.DOTALL)
                if plan_match:
                    content = plan_match.group(0).strip()
                
            elif framework == "crewai":
                # Clean up crewai formatting
                content = re.sub(r'Task: .*?\n', '', content)
                content = re.sub(r'Result: ', '', content)
                
                # Remove extra crew-specific info
                content = re.sub(r'\nCredibility:.*?\n', '\n', content)
                
            elif framework == "langgraph":
                # Make sure we extract just the business plan
                plan_match = re.search(r'(?:# Business Plan|## Business Plan).*?(?=\Z)', content, re.DOTALL)
                if plan_match:
                    content = plan_match.group(0).strip()
            
            # Common cleaning
            # Ensure proper markdown headers
            content = re.sub(r'^(?!#)(.+?):\s*\$', r'## \1', content, flags=re.MULTILINE)  # Convert "Header:" to "## Header"
            
            # Standardize main title
            if not content.startswith("# Business Plan"):
                content = re.sub(r'^#+ .*?(?:Business Plan|Plan for).*\$', '# Business Plan for SaaSy Startup', content, flags=re.MULTILINE | re.IGNORECASE)
            
            # Write normalized content
            with open(output_path, 'w') as f:
                f.write(content)
                
            print(f"  ✅ Normalized {framework} - output saved to {output_path}")
            
        except Exception as e:
            print(f"  ❌ Error normalizing {input_path}: {str(e)}")
    
    print("✅ Normalization complete")
    return True

def evaluate_outputs(use_bedrock=False):
    """Score normalized outputs with multiple models"""
    print("\nEvaluating framework outputs...")
    md_files = glob(os.path.join(NORMALIZED_DIR, 'normalized_*_dynamic_orchestration.md'))
    results = []
    
    for md_path in md_files:
        with open(md_path, 'r') as f:
            content = f.read()
            
        # Extract framework name
        framework = os.path.basename(md_path).replace('normalized_b2_', '').replace('_dynamic_orchestration.md', '')
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
        if use_bedrock:
            # Reduced model list (no DeepSeek)
            bedrock_models = [
                ("anthropic.claude-3-sonnet-20240229-v1:0", "Claude 3 Sonnet"),
                ("anthropic.claude-3-haiku-20240307-v1:0", "Claude 3 Haiku")
            ]
            
            for model_id, model_name in bedrock_models:
                try:
                    print(f"  Scoring with Bedrock: {model_name}")
                    bedrock_score = score_with_bedrock(content, model_id)
                    bedrock_score["model"] = model_name
                    scores.append(bedrock_score)
                    print(f"  ✅ {model_name} scoring complete")
                except Exception as e:
                    print(f"  ❌ {model_name} scoring failed: {e}")
                # Add slight delay between model calls
                time.sleep(1.0)
        
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
        f.write("| Framework | Duration (seconds) | Agent Turns | Output Length (chars) |\n")
        f.write("|-----------|-------------------|-------------|----------------------|\n")
        
        for framework, data in framework_metrics.items():
            f.write(f"| {framework.capitalize()} | {data['duration']} | {data['agent_turns']} | {data['output_length']} |\n")
        
        # Agent Selection Capabilities
        f.write("\n## Agent Selection Capabilities\n\n")
        f.write("| Framework | Filtered Irrelevant Agents | Detection Details |\n")
        f.write("|-----------|----------------------------|-------------------|\n")
        for framework, data in framework_metrics.items():
            f.write(f"| {framework.capitalize()} | {data['filtered_irrelevant_agents']} | {data['agent_filtering_details']} |\n")
        
        # Quality Assessment
        f.write("\n## Quality Assessment\n\n")
        f.write("| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |\n")
        f.write("|-----------|--------------|-------------------|-------------------|------------------------|\n")
        
        # Aggregate scores across evaluators
        framework_avg_scores = {}
        for result in evaluation_results:
            framework = result["framework"]
            valid_scores = [s for s in result["scores"] if "error" not in s]
            
            if valid_scores:
                # Calculate averages
                completeness_avg = sum(float(s.get("completeness", 0)) for s in valid_scores) / len(valid_scores)
                rationale_avg = sum(float(s.get("rationale_quality", 0)) for s in valid_scores) / len(valid_scores)
                structure_avg = sum(float(s.get("structure_quality", 0)) for s in valid_scores) / len(valid_scores)
                
                # Get baseball handling from Claude (more reliable)
                claude_score = next((s for s in result["scores"] if s.get("model") == "claude-3-sonnet"), {})
                baseball = claude_score.get("baseball_coach_handling", "?")
                baseball_rating = {0: "Not mentioned", 1: "Mentioned", 2: "Properly excluded"}
                baseball_display = f"{baseball} ({baseball_rating.get(baseball, 'Unknown')})"
                
                f.write(f"| {framework.capitalize()} | {completeness_avg:.2f}/3 | {rationale_avg:.2f}/3 | {structure_avg:.2f}/3 | {baseball_display} |\n")
                
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
                f.write(f"| {i} | {fw.capitalize()} | {scores['total']:.2f}/9 | {scores['completeness']:.2f}/3 | {scores['rationale_quality']:.2f}/3 | {scores['structure_quality']:.2f}/3 |\n")
        
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
                    f.write(f"**Completeness:** {score.get('completeness', '?')}/3\n{score.get('completeness_explanation', 'No explanation provided.')}\n\n")
                    f.write(f"**Rationale Quality:** {score.get('rationale_quality', '?')}/3\n{score.get('rationale_explanation', 'No explanation provided.')}\n\n")
                    f.write(f"**Structure Quality:** {score.get('structure_quality', '?')}/3\n{score.get('structure_explanation', 'No explanation provided.')}\n\n")
                    
                    baseball = score.get('baseball_coach_handling', '?')
                    if baseball == 2:
                        baseball_text = "BaseballCoachAgent was properly excluded with explanation"
                    elif baseball == 1:
                        baseball_text = "BaseballCoachAgent was mentioned but not properly explained"
                    elif baseball == 0:
                        baseball_text = "BaseballCoachAgent was not mentioned at all"
                    else:
                        baseball_text = "Unknown BaseballCoachAgent handling"
                    
                    f.write(f"**BaseballCoachAgent Handling:** {baseball_text}\n\n")
                    
                    if all(k in score for k in ['completeness', 'rationale_quality', 'structure_quality']):
                        total = float(score['completeness']) + float(score['rationale_quality']) + float(score['structure_quality'])
                        f.write(f"**Total Score: {total:.2f}/9**\n\n")
    
    print(f"\n✅ Benchmark report written to {SUMMARY_REPORT}")

# === MAIN ===
def main():
    # Run all framework tests
    framework_metrics = run_all_framework_tests()
    
    # Normalize output files
    normalize_success = normalize_outputs()
    if not normalize_success:
        print("⚠️ Continuing with evaluation despite normalization issues.")
    
    # Check for AWS credentials
    use_bedrock = check_aws_credentials()
    
    # Score outputs with appropriate models
    evaluation_results = evaluate_outputs(use_bedrock=use_bedrock)
    
    # Generate comprehensive report
    generate_report(framework_metrics, evaluation_results)

# Constants for scoring
SCORING_PROMPT = '''
You are an expert business plan evaluator. Given the following business plan, score it on a scale of 0-3 for each category:

- Completeness (Does it cover all sections and details expected in a professional business plan, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion, and a rationale at the top?)
  - 0: Missing most required sections
  - 1: Missing several key sections or most sections lack depth
  - 2: Contains most sections with adequate detail
  - 3: Comprehensive with all required sections and appropriate detail

- Rationale Quality (Does it clearly explain why certain agents were used and others were not? Does it mention the BaseballCoachAgent and explain why it was excluded? Does it explain the reasoning behind strategic decisions?)
  - 0: No rationale provided
  - 1: Minimal rationale with little explanation
  - 2: Adequate rationale with some explanation of decisions
  - 3: Excellent rationale with clear explanations for all key decisions

- Structure Quality (Is it well-organized, readable, and follows a standard business plan format with clear markdown sections in the required order?)
  - 0: Poorly structured, difficult to follow
  - 1: Basic structure but with organizational issues
  - 2: Good structure with clear sections
  - 3: Excellent structure with professional formatting and logical flow

For each, provide a brief explanation for the score.

Additional considerations:
- For Completeness: Check if there's a rationale section at the top and if it mentions which agents were used and not used
- For Structure Quality: Check for consistent headers, logical flow between sections, and appropriate formatting

Respond in the following JSON format:
{
  "completeness": <score>,
  "completeness_explanation": "...",
  "rationale_quality": <score>,
  "rationale_explanation": "...",
  "structure_quality": <score>,
  "structure_explanation": "...",
  "baseball_coach_handling": <0 if not mentioned, 1 if mentioned but not explained, 2 if mentioned as excluded with explanation>
}
'''

HEADERS = {
    'x-api-key': ANTHROPIC_API_KEY,
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
}

if __name__ == '__main__':
    import requests
    main()