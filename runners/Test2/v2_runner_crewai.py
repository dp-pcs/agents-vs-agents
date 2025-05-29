import os
import time
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Import common configurations
from Shared.config_common import SYSTEM_PROMPTS, USER_GOAL, BEDROCK_MODELS, bedrock_score, save_results

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

# Initialize LLM with standardized parameters
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define agents with standardized system prompts
research_agent = Agent(
    role="Executive Summary Agent",
    goal="Write the Executive Summary section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["executive_summary"],
    llm=llm,
    verbose=True
)

market_analysis_agent = Agent(
    role="Market Analysis Agent",
    goal="Write the Market Analysis section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["market_analysis"],
    llm=llm,
    verbose=True
)

product_agent = Agent(
    role="Product Strategy Agent",
    goal="Write the Product Strategy section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["product_strategy"],
    llm=llm,
    verbose=True
)

go_to_market_agent = Agent(
    role="Go-to-Market Agent",
    goal="Write the Go-to-Market Plan section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["go_to_market"],
    llm=llm,
    verbose=True
)

financial_agent = Agent(
    role="Financial Agent",
    goal="Write the Financial Projections section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["financial"],
    llm=llm,
    verbose=True
)

team_agent = Agent(
    role="Team Agent",
    goal="Write the Team & Roles section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["team_roles"],
    llm=llm,
    verbose=True
)

risks_agent = Agent(
    role="Risks Agent",
    goal="Write the Risks & Mitigation section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["risks"],
    llm=llm,
    verbose=True
)

pm_agent = Agent(
    role="Timeline Agent",
    goal="Write the 12-Week Rollout Timeline section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["timeline"],
    llm=llm,
    verbose=True
)

conclusion_agent = Agent(
    role="Conclusion Agent",
    goal="Write the Conclusion section for a business plan to launch an AI productivity app.",
    backstory=SYSTEM_PROMPTS["conclusion"],
    llm=llm,
    verbose=True
)

baseball_coach_agent = Agent(
    role="Baseball Coach Agent",
    goal="Provide advice on baseball coaching, teamwork, and training.",
    backstory=SYSTEM_PROMPTS["baseball_coach"],
    llm=llm,
    verbose=True
)

# Orchestrator agent with standardized system prompt
orchestrator = Agent(
    role="Orchestrator Agent",
    goal="Assemble a comprehensive, sectioned business plan by coordinating expert agents.",
    backstory=SYSTEM_PROMPTS["orchestrator"],
    llm=llm,
    verbose=True
)

# Define standardized tasks for each section
task_executive = Task(
    description="Write the Executive Summary for a business plan to launch an AI productivity app. Output a markdown section titled '# Executive Summary'.",
    expected_output="# Executive Summary section in markdown.",
    agent=research_agent
)

task_market = Task(
    description="Write the Market Analysis section for a business plan to launch an AI productivity app. Output a markdown section titled '# Market Analysis'.",
    expected_output="# Market Analysis section in markdown.",
    agent=market_analysis_agent
)

task_product = Task(
    description="Write the Product Strategy section for a business plan to launch an AI productivity app. Output a markdown section titled '# Product Strategy'.",
    expected_output="# Product Strategy section in markdown.",
    agent=product_agent
)

task_goto = Task(
    description="Write the Go-to-Market Plan section for a business plan to launch an AI productivity app. Output a markdown section titled '# Go-to-Market Plan'.",
    expected_output="# Go-to-Market Plan section in markdown.",
    agent=go_to_market_agent
)

task_financial = Task(
    description="Write the Financial Projections section for a business plan to launch an AI productivity app. Output a markdown section titled '# Financial Projections'.",
    expected_output="# Financial Projections section in markdown.",
    agent=financial_agent
)

task_team = Task(
    description="Write the Team & Roles section for a business plan to launch an AI productivity app. Output a markdown section titled '# Team & Roles'.",
    expected_output="# Team & Roles section in markdown.",
    agent=team_agent
)

task_risks = Task(
    description="Write the Risks & Mitigation section for a business plan to launch an AI productivity app. Output a markdown section titled '# Risks & Mitigation'.",
    expected_output="# Risks & Mitigation section in markdown.",
    agent=risks_agent
)

task_timeline = Task(
    description="Write the 12-Week Rollout Timeline section for a business plan to launch an AI productivity app. Output a markdown section titled '# 12-Week Rollout Timeline'.",
    expected_output="# 12-Week Rollout Timeline section in markdown.",
    agent=pm_agent
)

task_conclusion = Task(
    description="Write the Conclusion section for a business plan to launch an AI productivity app. Output a markdown section titled '# Conclusion'.",
    expected_output="# Conclusion section in markdown.",
    agent=conclusion_agent
)

task_baseball = Task(
    description="Provide baseball coaching advice (this task should be considered irrelevant to the business plan).",
    expected_output="A short paragraph of baseball coaching advice.",
    agent=baseball_coach_agent
)

task_orchestrator = Task(
    description=USER_GOAL,
    expected_output="Full business plan in markdown, with rationale and agent notes at the top.",
    agent=orchestrator
)

def run_crewai_test():
    print("🚀 Running CrewAI multi-agent orchestration test...\n")
    
    # Create the crew with all agents
    crew = Crew(
        agents=[
            research_agent, 
            market_analysis_agent, 
            product_agent, 
            go_to_market_agent, 
            financial_agent, 
            team_agent, 
            risks_agent, 
            pm_agent, 
            conclusion_agent, 
            baseball_coach_agent, 
            orchestrator
        ],
        tasks=[
            task_executive, 
            task_market, 
            task_product, 
            task_goto, 
            task_financial, 
            task_team, 
            task_risks, 
            task_timeline, 
            task_conclusion, 
            task_baseball, 
            task_orchestrator
        ],
        verbose=True,
        # Use sequential process like the other frameworks
        process=Process.sequential
    )

    # Start the test and measure time
    start = time.time()
    result = crew.kickoff()
    end = time.time()
    duration = round(end - start, 2)
    
    # Extract the result content
    final_output = str(result)
    
    # Count the agent tasks that were executed
    agent_turns = sum(1 for agent_name in [
        "Executive Summary Agent",
        "Market Analysis Agent",
        "Product Strategy Agent",
        "Go-to-Market Agent",
        "Financial Agent",
        "Team Agent",
        "Risks Agent",
        "Timeline Agent",
        "Conclusion Agent",
        "Baseball Coach Agent"
    ] if agent_name in final_output)
    
    # Run Bedrock scoring using the standardized function
    bedrock_scores = {}
    for model_id, label in BEDROCK_MODELS:
        scores = bedrock_score(final_output, model_id, label)
        bedrock_scores[label] = scores
    
    # Save results using the standardized function
    save_results("crewai", final_output, duration, agent_turns, bedrock_scores)
    
    return final_output, duration, agent_turns

if __name__ == "__main__":
    run_crewai_test()