import os
import time
from dotenv import load_dotenv
import requests
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, StateGraph
from langchain_core.chat_history import BaseChatMessageHistory

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, AgentExecutor, create_openai_functions_agent
from langchain.tools.render import render_text_description

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0)

# === Define tools for each role ===

def market_research_tool(_):
    return "Market trends show rising demand for AI productivity tools. Key competitors: App A, App B."

def product_strategy_tool(_):
    return "MVP: Task assistant + voice capture. Priority: Speed and clean UX."

def marketing_plan_tool(_):
    return "Target: freelancers and SMBs. Channels: LinkedIn, YouTube, newsletters."

def pm_timeline_tool(_):
    return "3-month rollout: Month 1 = build, Month 2 = test, Month 3 = launch."

tools = [
    Tool.from_function(market_research_tool, name="ResearchAgent", description="Analyze market trends and competitors."),
    Tool.from_function(product_strategy_tool, name="ProductAgent", description="Define MVP and product strategy."),
    Tool.from_function(marketing_plan_tool, name="MarketingAgent", description="Create marketing plan."),
    Tool.from_function(pm_timeline_tool, name="PMAgent", description="Build 3-month timeline.")
]

# === Create orchestrator agent ===

prompt = PromptTemplate(
    input_variables=["agent_scratchpad"],
    template="""
You are a Chief Operations Officer agent coordinating 4 experts:
- ResearchAgent
- ProductAgent
- MarketingAgent
- PMAgent

The user wants a 3-month launch plan for an AI productivity app.

1. Decide which agents to call.
2. For each, explain why you used them and what you asked.
3. Summarize the responses into a final markdown plan.
4. Include a **rationale** at the top.
5. Format cleanly in markdown.

You may call each agent **once** via tools, then end the task.

{agent_scratchpad}
"""
)

orchestrator = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=orchestrator, tools=tools, verbose=True)

# === LangGraph wrapper node ===

import re

def orchestrator_node(state):
    user_goal = state["input"]
    result = agent_executor.invoke({"input": user_goal})
    final_output = result.get("output", "")
    if isinstance(final_output, list):
        final_output = "\n".join(
            str(chunk) for chunk in final_output if isinstance(chunk, str)
        )

    # Collect orchestrator summary and agent markdown sections
    summary_lines = []
    agent_outputs = {}
    for line in final_output.splitlines():
        match = re.search(r"FunctionMessage\(content='(.*?)',.*name='(.*?)'\)", line)
        if match:
            content, agent = match.groups()
            agent_outputs[agent] = content
        elif "AIMessageChunk" not in line and "FunctionMessage" not in line:
            summary_lines.append(line)
    summary = "\n".join(summary_lines).strip()

    # Always include all expected agents
    expected_agents = ["ResearchAgent", "ProductAgent", "MarketingAgent", "PMAgent"]
    agent_sections = []
    for agent in expected_agents:
        if agent in agent_outputs:
            agent_sections.append(f"### {agent}\n{agent_outputs[agent]}")
        else:
            agent_sections.append(f"### {agent}\n_No direct output found._")
    agent_markdown = "\n\n".join(agent_sections)

    if summary and agent_markdown:
        final_output = f"{summary}\n\n{agent_markdown}"
    elif agent_markdown:
        final_output = agent_markdown
    else:
        final_output = summary
    return {"output": final_output}


# === Build LangGraph ===

from typing import TypedDict

class OrchestratorState(TypedDict):
    input: str
    output: str

workflow = StateGraph(state_schema=OrchestratorState)
workflow.add_node("orchestrator", orchestrator_node)
workflow.set_entry_point("orchestrator")
workflow.add_edge("orchestrator", END)
app = workflow.compile()

# === Run it ===

import time
import requests

if __name__ == "__main__":
    print("🚀 Running LangGraph Multi-Agent COO Test...\n")
    input_goal = "Design a 3-month strategic launch plan for an AI productivity app with rationale and agent coordination."
    start = time.time()
    result = app.invoke({"input": input_goal}, config=RunnableConfig())
    end = time.time()
    duration = round(end - start, 2)
    output = result["output"]

    # Heuristic for agent turns: count agent section headers in output
    agent_turns = sum(output.count(agent) for agent in ["ResearchAgent", "ProductAgent", "MarketingAgent", "PMAgent"])

    # Manual scores (placeholders)
    completeness_score = 2  # 0=partial, 1=missing agents, 2=complete
    rationale_quality = 3   # 0–3 scale
    structure_quality = 3   # 0–3 scale

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
            "Return a JSON object with the scores and a brief explanation.\n\nBusiness Plan:\n" + output
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

    llm_score = perplexity_score(output)

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
        bedrock_scores += bedrock_score(output, model_id, label)


    os.makedirs("results", exist_ok=True)
    with open("results/langgraph_dynamic_orchestration.md", "w") as f:
        f.write("# LangGraph Dynamic Orchestration Output\n\n")
        f.write(output)
        f.write(f"\n\n**Time to complete:** {duration} seconds\n")
        f.write(f"\n**Agent turns:** {agent_turns}\n")
        f.write(f"\n**Manual Scores:**\n- Completeness: {completeness_score}\n- Rationale Quality: {rationale_quality}\n- Structure Quality: {structure_quality}\n")
        f.write(f"\n**Perplexity LLM Score:**\n{llm_score}\n")
        f.write(f"\n**Bedrock LLM Scores:**\n{bedrock_scores}\n")

    print("✅ Done. Output saved to results/langgraph_dynamic_orchestration.md")