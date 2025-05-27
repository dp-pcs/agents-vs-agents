import os
from dotenv import load_dotenv
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

if __name__ == "__main__":
    print("🚀 Running LangGraph Multi-Agent COO Test...\n")
    input_goal = "Design a 3-month strategic launch plan for an AI productivity app with rationale and agent coordination."
    result = app.invoke({"input": input_goal}, config=RunnableConfig())
    output = result["output"]

    os.makedirs("results", exist_ok=True)
    with open("results/langgraph_dynamic_orchestration.md", "w") as f:
        f.write("# LangGraph Dynamic Orchestration Output\n\n")
        f.write(output)

    print("✅ Done. Output saved to results/langgraph_dynamic_orchestration.md")