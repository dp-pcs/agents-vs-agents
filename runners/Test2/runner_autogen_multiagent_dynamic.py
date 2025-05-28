import os
import time
from dotenv import load_dotenv
import requests
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# System prompt for the orchestrator agent
orchestrator_system_message = """
You are an autonomous AI Chief Operations Officer.
You will receive a business objective from a user, and you must create a strategic operational plan by dynamically engaging other agents (experts).
You may decide:
- Which agents to involve (if any)
- What subtasks to assign
- Whether to ask follow-ups or iterate

Your goal is to return a 1-page markdown-formatted strategic plan for the business scenario.
You must decide the sequence, collaboration, and scope of work needed to produce the best outcome.

Once you have received input from any necessary agents, synthesize the final plan and include a rationale. Then stop the conversation by saying:
**"Here is the final operational plan and rationale."**
"""

# Config for OpenAI (gpt-4)
config_list = [{
    'model': 'gpt-4',
    'api_key': os.getenv('OPENAI_API_KEY')
}]

# Create expert assistant agents
research_agent = AssistantAgent(
    name="ResearchAgent",
    system_message="You are a market research analyst. Answer questions about competitors, trends, and market data.",
    llm_config={"config_list": config_list}
)

product_agent = AssistantAgent(
    name="ProductAgent",
    system_message="You are a product strategist. Design features, define MVPs, and map product-market fit.",
    llm_config={"config_list": config_list}
)

marketing_agent = AssistantAgent(
    name="MarketingAgent",
    system_message="You are a marketing planner. Build campaigns, targeting strategies, and messaging.",
    llm_config={"config_list": config_list}
)

pm_agent = AssistantAgent(
    name="PMAgent",
    system_message="You are a project manager. Build timelines, task boards, and resource plans.",
    llm_config={"config_list": config_list}
)

# Orchestrator agent
orchestrator = AssistantAgent(
    name="COOAgent",
    system_message=orchestrator_system_message,
    llm_config={"config_list": config_list}
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
        product_agent,
        marketing_agent,
        pm_agent
    ],
    messages=[],
    max_round=30
)

manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

# Start orchestration
print("🚀 Starting dynamic multi-agent orchestration test...\n")
# User goal prompt for the orchestrator
user_goal = """You're helping launch a new AI productivity app.

Please provide a 3-month operational plan covering product strategy, marketing, research, and execution — but only if necessary.

You may use the following expert agents:
- ResearchAgent (market and competitor analysis)
- ProductAgent (MVP design and features)
- MarketingAgent (go-to-market messaging and targeting)
- PMAgent (timeline and task planning)

At the **top of your final output**, include a short **rationale section** where you explain:

- Which agents you decided to involve and why
- Which agents you chose not to involve and why
- The order in which you used them and your reasoning
- How their contributions affected the final plan

Then output a 1-page strategic plan formatted in markdown."""
def has_final_plan_with_rationale(messages):
    for m in reversed(messages):
        content = m["content"].lower()
        if m["name"] == "COOAgent" and "rationale" in content and "operational plan" in content:
            return True
    return False

start = time.time()
manager.run_chat_until_condition(
    user_goal,
    condition=has_final_plan_with_rationale
)
end = time.time()
duration = round(end - start, 2)

 # Extract final message from COOAgent with rationale or fallback to last COOAgent message
final_plan = ""
for m in reversed(groupchat.messages):
    if m["name"] == "COOAgent" and "rationale" in m["content"].lower():
        final_plan = m["content"]
        break

# Fallback if no rationale-containing message is found
if not final_plan:
    for m in reversed(groupchat.messages):
        if m["name"] == "COOAgent":
            final_plan = m["content"]
            break

# Count assistant agent messages as a proxy for agent turns
agent_turns = sum(1 for m in groupchat.messages if m["name"] != "UserProxy" and m["name"] != "COOAgent")

# Manual scoring
plan_completeness = 2  # 0 = partial, 1 = missing agents, 2 = complete
rationale_quality = 3  # 0–3 scale
structure_quality = 3  # 0–3 scale

# Perplexity scoring
perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
def perplexity_score(plan):
    if not perplexity_api_key:
        return "No API key provided."
    url = "https://api.perplexity.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {perplexity_api_key}",
        "Content-Type": "application/json"
    }
    prompt = (
        "Score the following business plan for completeness, rationale quality, and structure quality on a scale of 0–3. "
        "Return a JSON object with the scores and a brief explanation.\n\nBusiness Plan:\n" + plan
    )
    data = {
        "model": "pplx-70b-online",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=60)
        if resp.ok:
            return resp.json()["choices"][0]["message"]["content"]
        else:
            return f"Perplexity API error: {resp.status_code} {resp.text}"
    except Exception as e:
        return f"Perplexity API call failed: {str(e)}"

llm_score = perplexity_score(final_plan)

# Multi-model Bedrock scoring
import boto3
import json

def bedrock_score(plan, model_id, label):
    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
        prompt = (
            "Score the following business plan for completeness, rationale quality, and structure quality on a scale of 0–3. "
            "Return a JSON object with the scores and a brief explanation.\n\nBusiness Plan:\n" + plan
        )
        body = {
            "prompt": prompt,
            "max_tokens_to_sample": 512,
            "temperature": 0.2
        }
        response = bedrock.invoke_model(
            modelId=model_id,
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )
        result = response['body'].read().decode()
        return f"**{label} Score:**\n{result}\n"
    except Exception as e:
        return f"**{label} Score:** Bedrock API call failed: {str(e)}\n"

bedrock_models = [
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0", "Claude Opus 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0", "Claude Sonnet 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0", "Claude 3.7 Sonnet"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.deepseek.r1-v1:0", "DeepSeek-R1"),
]

bedrock_scores = ""
for model_id, label in bedrock_models:
    bedrock_scores += bedrock_score(final_plan, model_id, label)


# Save final result
os.makedirs("results", exist_ok=True)
with open("results/autogen_dynamic_orchestration.md", "w") as f:
    f.write("# AutoGen Dynamic Orchestration Output\n\n")
    f.write(final_plan)
    f.write(f"\n\n**Time to complete:** {duration} seconds\n")
    f.write(f"\n**Agent turns:** {agent_turns}\n")
    f.write(f"\n**Manual Scores:**\n- Completeness: {plan_completeness}\n- Rationale Quality: {rationale_quality}\n- Structure Quality: {structure_quality}\n")
    f.write(f"\n**Perplexity LLM Score:**\n{llm_score}\n")
    f.write(f"\n**Bedrock LLM Scores:**\n{bedrock_scores}\n")

print("✅ Output saved to results/autogen_dynamic_orchestration.md")