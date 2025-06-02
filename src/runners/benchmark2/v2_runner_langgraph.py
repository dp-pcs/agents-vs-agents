import os
import time
from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, StateGraph
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, AgentExecutor, create_openai_functions_agent
from typing import TypedDict
from datetime import datetime

# Import common configurations
from src.shared.config_common import SYSTEM_PROMPTS, USER_GOAL, save_results

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

# Initialize LLM with standardized parameters
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Define LLM-based tools for each section instead of hardcoded content
def executive_summary_tool(_):
    """Generate executive summary using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["executive_summary"])
    return "# Executive Summary\n\n" + response.content

def market_analysis_tool(_):
    """Generate market analysis using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["market_analysis"])
    return "# Market Analysis\n\n" + response.content

def product_strategy_tool(_):
    """Generate product strategy using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["product_strategy"])
    return "# Product Strategy\n\n" + response.content

def go_to_market_tool(_):
    """Generate go-to-market plan using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["go_to_market"])
    return "# Go-to-Market Plan\n\n" + response.content

def financial_projections_tool(_):
    """Generate financial projections using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["financial"])
    return "# Financial Projections\n\n" + response.content

def team_roles_tool(_):
    """Generate team & roles section using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["team_roles"])
    return "# Team & Roles\n\n" + response.content

def risks_mitigation_tool(_):
    """Generate risks & mitigation section using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["risks"])
    return "# Risks & Mitigation\n\n" + response.content

def rollout_timeline_tool(_):
    """Generate 12-week rollout timeline using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["timeline"])
    return "# 12-Week Rollout Timeline\n\n" + response.content

def conclusion_tool(_):
    """Generate conclusion using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["conclusion"])
    return "# Conclusion\n\n" + response.content

def baseball_coach_tool(_):
    """Generate baseball coaching advice using LLM"""
    response = llm.invoke(SYSTEM_PROMPTS["baseball_coach"])
    return "# Baseball Coaching Advice\n\n" + response.content

# Define tools with standardized names matching other frameworks
tools = [
    Tool.from_function(executive_summary_tool, name="ExecutiveSummaryAgent", 
                      description="Generate the Executive Summary section."),
    Tool.from_function(market_analysis_tool, name="MarketAnalysisAgent", 
                      description="Generate the Market Analysis section."),
    Tool.from_function(product_strategy_tool, name="ProductStrategyAgent", 
                      description="Generate the Product Strategy section."),
    Tool.from_function(go_to_market_tool, name="GoToMarketAgent", 
                      description="Generate the Go-to-Market Plan section."),
    Tool.from_function(financial_projections_tool, name="FinancialAgent", 
                      description="Generate the Financial Projections section."),
    Tool.from_function(team_roles_tool, name="TeamAgent", 
                      description="Generate the Team & Roles section."),
    Tool.from_function(risks_mitigation_tool, name="RisksAgent", 
                      description="Generate the Risks & Mitigation section."),
    Tool.from_function(rollout_timeline_tool, name="TimelineAgent", 
                      description="Generate the 12-Week Rollout Timeline section."),
    Tool.from_function(conclusion_tool, name="ConclusionAgent", 
                      description="Generate the Conclusion section."),
    Tool.from_function(baseball_coach_tool, name="BaseballCoachAgent", 
                      description="Get baseball coaching advice (not relevant for business plans).")
]

# Create orchestrator prompt with standardized content
prompt = PromptTemplate(
    input_variables=["agent_scratchpad"],
    template=f"""
{SYSTEM_PROMPTS["orchestrator"]}

You have access to the following expert agents:
- ExecutiveSummaryAgent: For executive summary
- MarketAnalysisAgent: For market analysis
- ProductStrategyAgent: For product strategy
- GoToMarketAgent: For go-to-market planning
- FinancialAgent: For financial projections
- TeamAgent: For team & roles
- RisksAgent: For risks & mitigation strategies
- TimelineAgent: For 12-week rollout timeline
- ConclusionAgent: For conclusion
- BaseballCoachAgent: Expert in baseball coaching (not relevant for business plans)

The user request is:
{USER_GOAL}

{{agent_scratchpad}}
"""
)

# Create orchestrator agent that dynamically selects which tools to use
orchestrator = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=orchestrator, tools=tools, verbose=True)

# Define LangGraph state type
class OrchestratorState(TypedDict):
    input: str
    output: str

# Define LangGraph node that allows the agent to dynamically decide which tools to use
def orchestrator_node(state):
    # Let the orchestrator decide which tools to call instead of hardcoding them
    result = agent_executor.invoke({"input": state["input"]})
    return {"output": result["output"]}

def run_langgraph_test():
    print("🚀 Running LangGraph Multi-Agent COO Test...\n")
    
    # Build the workflow
    workflow = StateGraph(state_schema=OrchestratorState)
    workflow.add_node("orchestrator", orchestrator_node)
    workflow.set_entry_point("orchestrator")
    workflow.add_edge("orchestrator", END)
    app = workflow.compile()
    
    # Start the test and measure time
    start = time.time()
    result = app.invoke({"input": USER_GOAL}, config=RunnableConfig())
    end = time.time()
    duration = round(end - start, 2)
    
    final_output = result["output"]
    
    # Count agent tool usage based on tool names appearing in output
    agent_turns = sum(1 for tool in [
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
    ] if tool in final_output)
    
    # Analyze baseball coach handling
    baseball_mentioned = "BaseballCoachAgent" in final_output
    baseball_excluded = any(phrase in final_output.lower() for phrase in [
        "not use baseballcoachagent", 
        "not involve baseball", 
        "excluded baseball", 
        "irrelevant baseball",
        "not relevant baseball"
    ])
    
    baseball_handling = "Properly excluded" if baseball_mentioned and baseball_excluded else \
                       "Incorrectly used" if baseball_mentioned else \
                       "Not mentioned"
    
    print(f"BaseballCoachAgent handling: {baseball_handling}")
    
    # Save a custom results file with framework behavior analysis
    date_str = datetime.now().strftime("%Y-%m-%d")
    raw_output_dir = os.path.join("results", "benchmark2", f"raw_outputs_{date_str}")
    os.makedirs(raw_output_dir, exist_ok=True)
    dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(raw_output_dir, f"langgraph_dynamic_orchestration_{dt_str}.md")
    
    try:
        print(f"Writing LangGraph output to {output_file}...")
        with open(output_file, "w", encoding="utf-8") as f:
            # Header
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write("# LangGraph Dynamic Orchestration Output\n\n")
            
            # Framework behavior analysis
            f.write("## Framework Behavior Analysis\n\n")
            
            # Document BaseballCoachAgent handling
            f.write("### Agent Selection:\n")
            f.write(f"- **BaseballCoachAgent**: {baseball_handling}\n\n")
            
            if baseball_mentioned and baseball_excluded:
                f.write("**FINDING**: BaseballCoachAgent was correctly identified as irrelevant to the business task.\n\n")
            elif baseball_mentioned:
                f.write("**FINDING**: BaseballCoachAgent may have been incorrectly used despite being irrelevant to the business task.\n\n")
            else:
                f.write("**FINDING**: BaseballCoachAgent was not mentioned in the output.\n\n")
            
            # Business plan content
            f.write("## Business Plan Content\n\n")
            f.write(final_output)
            
            # Metadata
            f.write(f"\n\n**Time to complete:** {duration} seconds\n")
            f.write(f"\n**Agent turns:** {agent_turns}\n")
        
        print(f"✅ Output successfully written to {output_file}")
    except Exception as e:
        print(f"❌ Error writing output file: {str(e)}")
    
    # Save results with an empty bedrock_scores dictionary
    save_results("langgraph", final_output, duration, agent_turns, {})
    
    return final_output, duration, agent_turns

if __name__ == "__main__":
    run_langgraph_test()