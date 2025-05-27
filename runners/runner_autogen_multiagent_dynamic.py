import os
import time
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

load_dotenv()

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
    max_round=20
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
start = time.time()
user_proxy.initiate_chat(manager, message=user_goal)
end = time.time()
duration = round(end - start, 2)

# Save final result
os.makedirs("results", exist_ok=True)
final_plan = groupchat.messages[-1]['content']
with open("results/autogen_dynamic_orchestration.md", "w") as f:
    f.write("# AutoGen Dynamic Orchestration Output\n\n")
    f.write(final_plan)
    f.write(f"\n\n**Time to complete:** {duration} seconds\n")

print("✅ Output saved to results/autogen_dynamic_orchestration.md")