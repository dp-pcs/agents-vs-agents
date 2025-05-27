import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define sub-agents
research_agent = Agent(
    role="Research Agent",
    goal="Analyze the competitive landscape for AI note-taking apps",
    backstory="You are a market analyst skilled in extracting competitive intelligence.",
    llm=llm,
    verbose=True
)

product_agent = Agent(
    role="Product Agent",
    goal="Design an MVP feature set for the AI note-taking app",
    backstory="You are a senior product manager focused on AI UX.",
    llm=llm,
    verbose=True
)

marketing_agent = Agent(
    role="Marketing Agent",
    goal="Draft a product launch campaign for the new app",
    backstory="You are a marketing strategist with experience in SaaS launches.",
    llm=llm,
    verbose=True
)

pm_agent = Agent(
    role="Project Manager Agent",
    goal="Define a 3-month rollout timeline with key milestones",
    backstory="You are a project manager known for fast execution plans.",
    llm=llm,
    verbose=True
)

# Define orchestrator agent
orchestrator = Agent(
    role="Orchestrator Agent",
    goal="Plan the go-to-market strategy for the AI note-taking app using outputs from all agents.",
    backstory="You coordinate input from research, product, marketing, and project management to create a final strategic report.",
    llm=llm,
    verbose=True
)

# Define tasks
task_research = Task(
    description="Find the top 3 competitors in the AI note-taking space and summarize their features and pricing.",
    expected_output="Summary of 3 competitors with bullet points.",
    agent=research_agent
)

task_product = Task(
    description="Define a minimum viable feature set for an AI-powered note-taking app.",
    expected_output="List of 6–8 core features.",
    agent=product_agent
)

task_marketing = Task(
    description="Draft a 3-paragraph product launch campaign including positioning and audience.",
    expected_output="Launch copy + high-level targeting plan.",
    agent=marketing_agent
)

task_pm = Task(
    description="Create a 12-week timeline with milestones for building and launching the product.",
    expected_output="Timeline in markdown table format with 4–5 phases.",
    agent=pm_agent
)

task_orchestrator = Task(
    description="Take all other outputs and summarize into a 1-page go-to-market report.",
    expected_output="Integrated strategy document.",
    agent=orchestrator
)

# Run the orchestrated crew
crew = Crew(
    agents=[research_agent, product_agent, marketing_agent, pm_agent, orchestrator],
    tasks=[task_research, task_product, task_marketing, task_pm, task_orchestrator],
    verbose=True
)

print("🚀 Running multi-agent orchestrator benchmark...\n")
result = crew.kickoff()

# Save the final orchestrated output
os.makedirs("results", exist_ok=True)
with open("results/multiagent_orchestrator_result.md", "w") as f:
    f.write("# Multi-Agent Orchestrator Benchmark Result\n\n")
    f.write(str(result))

print("✅ Output saved to results/multiagent_orchestrator_result.md")