import os
import time
from dotenv import load_dotenv
import requests
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# --- Subclass for message windowing ---
class WindowedAssistantAgent(AssistantAgent):
    def __init__(self, *args, max_history=12, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_history = max_history

    def generate_reply(self, messages=None, sender=None):
        if messages is not None and len(messages) > self.max_history:
            messages = messages[-self.max_history:]
        return super().generate_reply(messages=messages, sender=sender)

# System prompt for the orchestrator agent
orchestrator_system_message = """
You are an autonomous AI Chief Operations Officer.
You will receive a business objective from a user, and you must create a comprehensive, sectioned business plan by dynamically engaging other agents (experts). For each agent, instruct them to generate a full markdown section for their assigned business plan component (Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion). Once you have received input from all necessary agents, synthesize the final plan and include a rationale at the top. At the top, note any agent not used (e.g., BaseballCoachAgent). Output a single markdown file with all sections in order. Then stop the conversation by saying: **"Here is the final business plan and rationale."**
"""

# Config for OpenAI (gpt-4)
config_list = [{
    'model': 'gpt-4o',
    'api_key': os.getenv('OPENAI_API_KEY')
}]

# Create expert assistant agents using WindowedAssistantAgent
# === Enhanced AutoGen Agent Section Assignments ===
research_agent = WindowedAssistantAgent(
    name="ExecutiveSummaryAgent",
    system_message="You are an expert business analyst. Write the Executive Summary section for a business plan to launch an AI productivity app. Output a markdown section titled '# Executive Summary'.",
    llm_config={"config_list": config_list},
    max_history=12
)

market_analysis_agent = WindowedAssistantAgent(
    name="MarketAnalysisAgent",
    system_message="You are a market research expert. Write the Market Analysis section for a business plan to launch an AI productivity app. Output a markdown section titled '# Market Analysis'.",
    llm_config={"config_list": config_list},
    max_history=12
)

product_agent = WindowedAssistantAgent(
    name="ProductStrategyAgent",
    system_message="You are a senior product manager. Write the Product Strategy section for a business plan to launch an AI productivity app. Output a markdown section titled '# Product Strategy'.",
    llm_config={"config_list": config_list},
    max_history=12
)

go_to_market_agent = WindowedAssistantAgent(
    name="GoToMarketAgent",
    system_message="You are a marketing strategist. Write the Go-to-Market Plan section for a business plan to launch an AI productivity app. Output a markdown section titled '# Go-to-Market Plan'.",
    llm_config={"config_list": config_list},
    max_history=12
)

financial_agent = WindowedAssistantAgent(
    name="FinancialAgent",
    system_message="You are a finance expert. Write the Financial Projections section for a business plan to launch an AI productivity app. Output a markdown section titled '# Financial Projections'.",
    llm_config={"config_list": config_list},
    max_history=12
)

team_agent = WindowedAssistantAgent(
    name="TeamAgent",
    system_message="You are an HR and org design expert. Write the Team & Roles section for a business plan to launch an AI productivity app. Output a markdown section titled '# Team & Roles'.",
    llm_config={"config_list": config_list},
    max_history=12
)

risks_agent = WindowedAssistantAgent(
    name="RisksAgent",
    system_message="You are a risk management consultant. Write the Risks & Mitigation section for a business plan to launch an AI productivity app. Output a markdown section titled '# Risks & Mitigation'.",
    llm_config={"config_list": config_list},
    max_history=12
)

pm_agent = WindowedAssistantAgent(
    name="TimelineAgent",
    system_message="You are a project manager. Write the 12-Week Rollout Timeline section for a business plan to launch an AI productivity app. Output a markdown section titled '# 12-Week Rollout Timeline'.",
    llm_config={"config_list": config_list},
    max_history=12
)

conclusion_agent = WindowedAssistantAgent(
    name="ConclusionAgent",
    system_message="You are a business consultant. Write the Conclusion section for a business plan to launch an AI productivity app. Output a markdown section titled '# Conclusion'.",
    llm_config={"config_list": config_list},
    max_history=12
)

baseball_coach_agent = WindowedAssistantAgent(
    name="BaseballCoachAgent",
    system_message="You are a baseball coach. Give advice on teamwork, batting, and fielding. You are not an expert in business or software. If asked about business plans, reply with baseball coaching tips only.",
    llm_config={"config_list": config_list},
    max_history=12
)

# Orchestrator agent
orchestrator_system_message = """
You are an autonomous AI Chief Operations Officer.
You will receive a business objective from a user, and you must create a comprehensive, sectioned business plan by dynamically engaging other agents (experts). For each agent, instruct them to generate a full markdown section for their assigned business plan component (Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion). Once you have received input from all necessary agents, synthesize the final plan and include a rationale at the top. At the top, note any agent not used (e.g., BaseballCoachAgent). Output a single markdown file with all sections in order. Then stop the conversation by saying: **"Here is the final business plan and rationale."**
"""

orchestrator = WindowedAssistantAgent(
    name="COOAgent",
    system_message=orchestrator_system_message,
    llm_config={"config_list": config_list},
    max_history=12
)

# User Proxy Agent (simulates the user)
user_proxy = UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    code_execution_config=False
)

# Group chat configuration
groupchat = GroupChat(
    agents=[
        user_proxy,
        orchestrator,
        research_agent,
        market_analysis_agent,
        product_agent,
        go_to_market_agent,
        financial_agent,
        team_agent,
        risks_agent,
        pm_agent,
        conclusion_agent,
        baseball_coach_agent
    ],
    messages=[],
    max_round=30
)

manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})


# Start orchestration
print("🚀 Starting dynamic multi-agent orchestration test...\n")
# User goal prompt for the orchestrator
user_goal = """
You're helping launch a new AI productivity app.

Please provide a 3-month operational plan covering product strategy, marketing, research, and execution — but only if necessary.

You may use the following expert agents:
- ResearchAgent (market and competitor analysis)
- ProductAgent (MVP design and features)
- MarketingAgent (go-to-market messaging and targeting)
- PMAgent (timeline and task planning)
- BaseballCoachAgent (expert in baseball coaching, teamwork, and sports; not a business or software expert)

At the **top of your final output**, include a short **rationale section** where you explain:
- Which agents you decided to involve and why
- Which agents you chose not to involve and why (especially irrelevant agents like BaseballCoachAgent)
- The order in which you used them and your reasoning
- How their contributions affected the final plan

Then output a 1-page strategic plan formatted in markdown.
"""
def has_final_plan_with_rationale(messages):
    for m in reversed(messages):
        content = m["content"].lower()
        if m["name"] == "COOAgent" and "rationale" in content and ("operational plan" in content or "business plan" in content):
            return True
    return False

start = time.time()
initial_message = {"content": user_goal, "role": "user", "name": user_proxy.name}
messages = [initial_message]
final_plan = ""

# Step-by-step chat: break when COOAgent outputs the final plan
for i in range(groupchat.max_round):
    manager.run_chat(messages=messages, sender=user_proxy, config=groupchat)
    # Check for final COOAgent message
    for m in reversed(groupchat.messages):
        content_lower = m["content"].lower()
        if m["name"] == "COOAgent" and "rationale" in content_lower and ("operational plan" in content_lower or "business plan" in content_lower) and "here is the final business plan and rationale." in content_lower:
            final_plan = m["content"]
            break
    if final_plan:
        break
end = time.time()
duration = round(end - start, 2)

# Fallback if no rationale-containing message is found
if not final_plan:
    for m in reversed(groupchat.messages):
        if m["name"] == "COOAgent":
            final_plan = m["content"]
            break

# Count messages from section agents as agent turns
section_agent_names = [
    "ExecutiveSummaryAgent",
    "MarketAnalysisAgent",
    "ProductStrategyAgent",
    "GoToMarketAgent",
    "FinancialAgent",
    "TeamAgent",
    "RisksAgent",
    "TimelineAgent",
    "ConclusionAgent",
    "BaseballCoachAgent"
]
agent_turns = sum(1 for m in groupchat.messages if m["name"] in section_agent_names)

# Multi-model Bedrock scoring
import boto3
import json

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

import re

def extract_scores(text):
    scores = {}
    for line in text.splitlines():
        match = re.search(r'([a-zA-Z]+) quality: (\d+)', line)
        if match:
            scores[match.group(1).lower().replace(' ', '_')] = int(match.group(2))
    return scores

def format_bedrock_score(label, raw_response):
    try:
        import json
        # Try to parse outer JSON if present (Bedrock API response)
        data = None
        try:
            outer = json.loads(raw_response)
            if isinstance(outer, dict) and 'content' in outer:
                content = outer['content']
                if isinstance(content, list) and 'text' in content[0]:
                    model_text = content[0]['text']
                elif isinstance(content, str):
                    model_text = content
                else:
                    model_text = str(content)
            else:
                model_text = raw_response
        except Exception:
            model_text = raw_response
        # Remove code block wrappers if present
        json_match = re.search(r'```json\n?(.*?)```', model_text, re.DOTALL)
        json_str = json_match.group(1) if json_match else model_text
        json_str = json_str.strip()
        data = json.loads(json_str)
        # Handle nested JSON
        def extract_scores(data):
            scores = {}
            for key, value in data.items():
                if isinstance(value, dict):
                    scores.update(extract_scores(value))
                elif key in ["completeness", "rationale_quality", "structure_quality"]:
                    scores[key] = value
            return scores
        scores = extract_scores(data)
        output = f"{label}: {scores}"
        return output
    except Exception:
        scores = extract_scores(raw_response)
        if scores:
            output = f"{label}: {scores}"
            return output
        else:
            return f"{label}: No output."

def bedrock_score(plan, model_id, label):
    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        prompt = (
            "Score the following business plan for completeness, rationale quality, and structure quality on a scale of 0–3. "
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
        return format_bedrock_score(label, result)
    except Exception as e:
        return f"{label}: Bedrock API call failed: {str(e)}\n"

bedrock_models = [
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0", "Claude Opus 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0", "Claude Sonnet 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0", "Claude 3.7 Sonnet"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.deepseek.r1-v1:0", "DeepSeek-R1"),
]

bedrock_scores = []
for model_id, label in bedrock_models:
    score = bedrock_score(final_plan, model_id, label)
    bedrock_scores.append([label, score])

# Save final result
os.makedirs("results", exist_ok=True)
print(f"[DEBUG] final_plan content before writing to file:\n{final_plan}\n---END---")
with open("results/b2_autogen_dynamic_orchestration.md", "w") as f:
    output_md = f"Generated: 2025-05-28T13:04:52-06:00\n# AutoGen Dynamic Orchestration Output\n\n"
    f.write(output_md)
    if final_plan.strip():
        f.write(final_plan)
    else:
        f.write("[WARNING] No business plan content was extracted. Please check the agent conversation or extraction logic.\n")
    f.write(f"\n\n**Time to complete:** {duration} seconds\n")
    f.write(f"\n**Agent turns:** {agent_turns}\n")
    f.write("\n**Bedrock LLM Scores:**\n")
    f.write("| Model | Score |\n")
    f.write("| --- | --- |\n")
    for score in bedrock_scores:
        f.write(f"| {score[0]} | {score[1]} |\n")

print("✅ Output saved to results/b2_autogen_dynamic_orchestration.md")