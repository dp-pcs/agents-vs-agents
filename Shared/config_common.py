# Shared/config_common.py
import os
import json
import re
from datetime import datetime

# --- Common configurations shared across all frameworks ---

# Standardized system prompts for all agents
SYSTEM_PROMPTS = {
    "orchestrator": """
You are an autonomous AI Chief Operations Officer.
You will receive a business objective from a user, and you must create a comprehensive, sectioned business plan by dynamically engaging other agents (experts).

For each agent, instruct them to generate a full markdown section for their assigned business plan component:
- Executive Summary
- Market Analysis 
- Product Strategy
- Go-to-Market Plan
- Financial Projections
- Team & Roles
- Risks & Mitigation
- 12-Week Rollout Timeline
- Conclusion

Once you have received input from all necessary agents, synthesize the final plan and include a rationale at the top.
At the top, note any agent not used (e.g., BaseballCoachAgent).
Output a single markdown file with all sections in order.
Then stop the conversation by saying: **"Here is the final business plan and rationale."**
""",

    "executive_summary": """
You are an expert business analyst. Write the Executive Summary section for a business plan to launch an AI productivity app. Output a markdown section titled '# Executive Summary'.
""",

    "market_analysis": """
You are a market research expert. Write the Market Analysis section for a business plan to launch an AI productivity app. Output a markdown section titled '# Market Analysis'.
""",

    "product_strategy": """
You are a senior product manager. Write the Product Strategy section for a business plan to launch an AI productivity app. Output a markdown section titled '# Product Strategy'.
""",
    
    "go_to_market": """
You are a marketing strategist. Write the Go-to-Market Plan section for a business plan to launch an AI productivity app. Output a markdown section titled '# Go-to-Market Plan'.
""",
    
    "financial": """
You are a finance expert. Write the Financial Projections section for a business plan to launch an AI productivity app. Output a markdown section titled '# Financial Projections'.
""",
    
    "team_roles": """
You are an HR and org design expert. Write the Team & Roles section for a business plan to launch an AI productivity app. Output a markdown section titled '# Team & Roles'.
""",
    
    "risks": """
You are a risk management consultant. Write the Risks & Mitigation section for a business plan to launch an AI productivity app. Output a markdown section titled '# Risks & Mitigation'.
""",
    
    "timeline": """
You are a project manager. Write the 12-Week Rollout Timeline section for a business plan to launch an AI productivity app. Output a markdown section titled '# 12-Week Rollout Timeline'.
""",
    
    "conclusion": """
You are a business consultant. Write the Conclusion section for a business plan to launch an AI productivity app. Output a markdown section titled '# Conclusion'.
""",
    
    "baseball_coach": """
You are a baseball coach. Give advice on teamwork, batting, and fielding. You are not an expert in business or software. If asked about business plans, reply with baseball coaching tips only.
"""
}

# Standard user goal for all frameworks
USER_GOAL = """
You're helping launch a new AI productivity app.

Please provide a 3-month operational plan covering product strategy, marketing, research, and execution.

At the top of your final output, include a short rationale section where you explain:
- Which agents you decided to involve and why
- Which agents you chose not to involve and why (especially irrelevant agents like BaseballCoachAgent)
- How the different components fit together into a cohesive plan

Then output a comprehensive business plan formatted in markdown.
"""

# Standard Bedrock evaluation function
def bedrock_score(plan, model_id, label):
    import boto3
    
    def get_bedrock_body(model_id, prompt, max_tokens=512):
        if "anthropic" in model_id:
            return {
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": 0.2,
                "anthropic_version": "bedrock-2023-05-31"
            }
        else:
            return {
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": 0.2
            }
    
    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        prompt = (
            "Score the following business plan for completeness, rationale quality, and structure quality on a scale of 0-3. "
            "Return a JSON object with the scores and a brief explanation.\n\nBusiness Plan:\n" + plan
        )
        body = get_bedrock_body(model_id, prompt)
        response = bedrock.invoke_model(
            modelId=model_id,
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )
        result = response['body'].read().decode()
        
        # Process the response
        try:
            # Handle Bedrock response format
            if isinstance(result, str):
                try:
                    parsed = json.loads(result)
                    if 'content' in parsed:
                        if isinstance(parsed['content'], list) and len(parsed['content']) > 0:
                            content = parsed['content'][0].get('text', '')
                        else:
                            content = str(parsed['content'])
                    else:
                        content = result
                except:
                    content = result
            else:
                content = str(result)
            
            # Extract scores from JSON if present
            json_match = re.search(r'```json\n?(.*?)```', content, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
            else:
                json_str = content
            
            data = json.loads(json_str)
            
            # Extract scores from nested structure
            scores = {}
            def extract_nested_scores(obj, scores):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if k.lower() in ["completeness", "rationale_quality", "structure_quality"] and isinstance(v, (int, float)):
                            scores[k.lower()] = v
                        elif isinstance(v, (dict, list)):
                            extract_nested_scores(v, scores)
                elif isinstance(obj, list):
                    for item in obj:
                        if isinstance(item, (dict, list)):
                            extract_nested_scores(item, scores)
            
            extract_nested_scores(data, scores)
            return scores
        except Exception as e:
            # Fallback to regex pattern matching if JSON parsing fails
            scores = {}
            patterns = {
                "completeness": r"(?:completeness|complete).*?(\d+)\/3",
                "rationale_quality": r"(?:rationale quality|rationale).*?(\d+)\/3",
                "structure_quality": r"(?:structure quality|structure).*?(\d+)\/3"
            }
            
            for key, pattern in patterns.items():
                match = re.search(pattern, result, re.IGNORECASE)
                if match:
                    scores[key] = int(match.group(1))
            
            return scores if scores else {"error": f"Failed to parse scores: {str(e)[:100]}..."}
    except Exception as e:
        return {"error": f"Bedrock API call failed: {str(e)[:100]}..."}

# Standard Bedrock models for evaluation
BEDROCK_MODELS = [
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0", "Claude Opus 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0", "Claude Sonnet 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0", "Claude 3.7 Sonnet"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.deepseek.r1-v1:0", "DeepSeek-R1"),
]

# Standard functions for saving results
def save_results(framework_name, output, duration, agent_turns, bedrock_scores):
    """Save test results in a standardized format across frameworks"""
    os.makedirs("results", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    
    with open(f"results/b2_{framework_name}_dynamic_orchestration.md", "w") as f:
        f.write(f"Generated: {timestamp}\n")
        f.write(f"# {framework_name.capitalize()} Dynamic Orchestration Output\n\n")
        f.write(output)
        f.write(f"\n\n**Time to complete:** {duration} seconds\n")
        f.write(f"\n**Agent turns:** {agent_turns}\n")
        
        # Format bedrock scores
        f.write("\n**Bedrock LLM Scores:**\n")
        f.write("| Model | Completeness | Rationale Quality | Structure Quality |\n")
        f.write("| --- | --- | --- | --- |\n")
        
        for model_name, scores in bedrock_scores.items():
            completeness = scores.get("completeness", "N/A")
            rationale = scores.get("rationale_quality", "N/A")
            structure = scores.get("structure_quality", "N/A")
            
            f.write(f"| {model_name} | {completeness} | {rationale} | {structure} |\n")
            
    print(f"✅ Output saved to results/b2_{framework_name}_dynamic_orchestration.md")