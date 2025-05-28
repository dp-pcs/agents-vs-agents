import os
import time
from dotenv import load_dotenv
import requests
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

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
start = time.time()
result = crew.kickoff()
end = time.time()
duration = round(end - start, 2)

# Count agent turns (excluding orchestrator)
def count_agent_turns(output):
    # Simple heuristic: count agent role mentions in the result
    return sum(output.count(agent.role) for agent in [research_agent, product_agent, marketing_agent, pm_agent])
agent_turns = count_agent_turns(str(result))

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
        "Return a JSON object with the scores and a brief explanation.\n\nBusiness Plan:\n" + str(result)
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

llm_score = perplexity_score(str(result))

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
    bedrock_scores += bedrock_score(str(result), model_id, label)


# Save the final orchestrated output
os.makedirs("results", exist_ok=True)
with open("results/crewai_dynamic_orchestration.md", "w") as f:
    f.write("# CrewAI Dynamic Orchestration Output\n\n")
    f.write(str(result))
    f.write(f"\n\n**Time to complete:** {duration} seconds\n")
    f.write(f"\n**Agent turns:** {agent_turns}\n")
    f.write(f"\n**Manual Scores:**\n- Completeness: {completeness_score}\n- Rationale Quality: {rationale_quality}\n- Structure Quality: {structure_quality}\n")
    f.write(f"\n**Perplexity LLM Score:**\n{llm_score}\n")
    f.write(f"\n**Bedrock LLM Scores:**\n{bedrock_scores}\n")

print("✅ Output saved to results/crewai_dynamic_orchestration.md")