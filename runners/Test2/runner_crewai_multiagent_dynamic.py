import os
import time
from dotenv import load_dotenv
import requests
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define sub-agents
# === Enhanced CrewAI Agent Section Assignments ===
research_agent = Agent(
    role="Executive Summary Agent",
    goal="Write the Executive Summary section for a business plan to launch an AI productivity app.",
    backstory="You are a business analyst skilled in summarizing strategic initiatives. Output a markdown section titled '# Executive Summary'.",
    llm=llm,
    verbose=True
)

market_analysis_agent = Agent(
    role="Market Analysis Agent",
    goal="Write the Market Analysis section for a business plan to launch an AI productivity app.",
    backstory="You are a market research expert. Output a markdown section titled '# Market Analysis'.",
    llm=llm,
    verbose=True
)

product_agent = Agent(
    role="Product Strategy Agent",
    goal="Write the Product Strategy section for a business plan to launch an AI productivity app.",
    backstory="You are a senior product manager. Output a markdown section titled '# Product Strategy'.",
    llm=llm,
    verbose=True
)

go_to_market_agent = Agent(
    role="Go-to-Market Agent",
    goal="Write the Go-to-Market Plan section for a business plan to launch an AI productivity app.",
    backstory="You are a marketing strategist. Output a markdown section titled '# Go-to-Market Plan'.",
    llm=llm,
    verbose=True
)

financial_agent = Agent(
    role="Financial Agent",
    goal="Write the Financial Projections section for a business plan to launch an AI productivity app.",
    backstory="You are a finance expert. Output a markdown section titled '# Financial Projections'.",
    llm=llm,
    verbose=True
)

team_agent = Agent(
    role="Team Agent",
    goal="Write the Team & Roles section for a business plan to launch an AI productivity app.",
    backstory="You are an HR and org design expert. Output a markdown section titled '# Team & Roles'.",
    llm=llm,
    verbose=True
)

risks_agent = Agent(
    role="Risks Agent",
    goal="Write the Risks & Mitigation section for a business plan to launch an AI productivity app.",
    backstory="You are a risk management consultant. Output a markdown section titled '# Risks & Mitigation'.",
    llm=llm,
    verbose=True
)

pm_agent = Agent(
    role="Timeline Agent",
    goal="Write the 12-Week Rollout Timeline section for a business plan to launch an AI productivity app.",
    backstory="You are a project manager. Output a markdown section titled '# 12-Week Rollout Timeline'.",
    llm=llm,
    verbose=True
)

conclusion_agent = Agent(
    role="Conclusion Agent",
    goal="Write the Conclusion section for a business plan to launch an AI productivity app.",
    backstory="You are a business consultant. Output a markdown section titled '# Conclusion'.",
    llm=llm,
    verbose=True
)

baseball_coach_agent = Agent(
    role="Baseball Coach Agent",
    goal="Provide advice on baseball coaching, teamwork, and training.",
    backstory="You are a baseball coach. Your expertise is in sports, not business or software. You give advice on batting, fielding, and team morale.",
    llm=llm,
    verbose=True
)

# Orchestrator agent
orchestrator = Agent(
    role="Orchestrator Agent",
    goal="Assemble a comprehensive, sectioned business plan for an AI productivity app by dynamically engaging other agents (experts). For each agent, instruct them to generate a full markdown section for their assigned business plan component (Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion). Once you have received input from all necessary agents, synthesize the final plan and include a rationale at the top. At the top, note any agent not used (e.g., BaseballCoachAgent). Output a single markdown file with all sections in order.",
    backstory="You coordinate expert agents to create a professional business plan. The BaseballCoachAgent is not relevant to the business task.",
    llm=llm,
    verbose=True
)

# Define tasks for each section
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
    description="Provide baseball coaching advice for launching an AI productivity app (should be irrelevant to the business plan).",
    expected_output="A short paragraph of baseball coaching advice.",
    agent=baseball_coach_agent
)

task_orchestrator = Task(
    description="Collect all markdown sections from the expert agents and assemble a single, comprehensive business plan. At the top, include a rationale for agent selection and a note about the BaseballCoachAgent. Output a markdown file with all sections in order.",
    expected_output="Full business plan in markdown, with rationale and agent notes at the top.",
    agent=orchestrator
)

# Run the orchestrated crew
crew = Crew(
    agents=[research_agent, market_analysis_agent, product_agent, go_to_market_agent, financial_agent, team_agent, risks_agent, pm_agent, conclusion_agent, baseball_coach_agent, orchestrator],
    tasks=[task_executive, task_market, task_product, task_goto, task_financial, task_team, task_risks, task_timeline, task_conclusion, task_baseball, task_orchestrator],
    verbose=True
)

print("🚀 Running multi-agent orchestrator benchmark...\n")
start = time.time()
result = crew.kickoff()
end = time.time()
duration = round(end - start, 2)

# Count agent turns (excluding orchestrator)
def count_agent_turns_from_tasks(task_results):
    # Count the number of completed section tasks (one per agent section)
    return sum(1 for t in task_results if t.get('status') == 'completed' and t.get('agent') in [
        'Executive Summary Agent',
        'Market Analysis Agent',
        'Product Strategy Agent',
        'Go-to-Market Agent',
        'Financial Agent',
        'Team Agent',
        'Risks Agent',
        'Timeline Agent',
        'Conclusion Agent',
        'Baseball Coach Agent'
    ])

# Run the orchestrated crew
crew = Crew(
    agents=[research_agent, market_analysis_agent, product_agent, go_to_market_agent, financial_agent, team_agent, risks_agent, pm_agent, conclusion_agent, baseball_coach_agent, orchestrator],
    tasks=[task_executive, task_market, task_product, task_goto, task_financial, task_team, task_risks, task_timeline, task_conclusion, task_baseball, task_orchestrator],
    verbose=True
)

print("🚀 Running multi-agent orchestrator benchmark...\n")

start = time.time()
result = crew.kickoff()
end = time.time()
duration = round(end - start, 2)

# Count agent turns by task execution if possible
agent_turns = None
if hasattr(result, 'tasks') and isinstance(result.tasks, list):
    agent_turns = count_agent_turns_from_tasks(result.tasks)
    print(f"[INFO] CrewAI agent turns (completed section tasks): {agent_turns}")
else:
    # Fallback: count role mentions in output
    agent_turns = sum(str(result).count(agent.role) for agent in [
        research_agent,
        market_analysis_agent,
        product_agent,
        go_to_market_agent,
        financial_agent,
        team_agent,
        risks_agent,
        pm_agent,
        conclusion_agent
    ])
    print(f"[INFO] CrewAI agent turns (fallback, output role mentions): {agent_turns}")
agent_turns = count_agent_turns(str(result))


# Multi-model Bedrock scoring
import boto3
import json
import re

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

def extract_scores(raw_response):
    try:
        # Remove markdown/code block wrappers if present
        json_match = re.search(r'```json\\n?(.*?)```', raw_response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            json_str = raw_response

        # Try to parse JSON
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            # Extract numeric scores from explanations
            scores = {}
            for line in raw_response.splitlines():
                match = re.search(r'(\d+(?:\.\d+)?)\/3', line)
                if match:
                    score = float(match.group(1))
                    if 'completeness' in line.lower():
                        scores['completeness'] = score
                    elif 'rationale quality' in line.lower():
                        scores['rationale_quality'] = score
                    elif 'structure quality' in line.lower():
                        scores['structure_quality'] = score
            return scores
        else:
            # Handle nested JSON
            def extract_scores(data):
                scores = {}
                for key, value in data.items():
                    if isinstance(value, dict):
                        scores.update(extract_scores(value))
                    elif key in ["completeness", "rationale_quality", "structure_quality"]:
                        scores[key] = value
                    elif key == "scores":
                        scores.update(value)
                return scores

            scores = extract_scores(data)
            return scores
    except Exception as e:
        return {}

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
        scores = extract_scores(result)
        return scores
    except Exception as e:
        return {}

bedrock_models = [
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0", "Claude Opus 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0", "Claude Sonnet 4"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0", "Claude 3.7 Sonnet"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.deepseek.r1-v1:0", "DeepSeek-R1"),
]

bedrock_scores = {}
for model_id, label in bedrock_models:
    scores = bedrock_score(str(result), model_id, label)
    if scores:
        bedrock_scores[label] = scores
    else:
        bedrock_scores[label] = 'No output.'

# Save the final orchestrated output
os.makedirs("results", exist_ok=True)
with open("results/b2_crewai_dynamic_orchestration.md", "w") as f:
    output_md = f"Generated: 2025-05-28T13:04:52-06:00\n# CrewAI Dynamic Orchestration Output\n\n"
    f.write(output_md)
    f.write(str(result))
    f.write(f"\n\n**Time to complete:** {duration} seconds\n")
    f.write(f"\n**Agent turns:** {agent_turns}\n")

    f.write("\n**Bedrock LLM Scores:**\n")
    f.write("| Model | Completeness | Rationale Quality | Structure Quality |\n")
    f.write("| --- | --- | --- | --- |\n")
    for label, scores in bedrock_scores.items():
        if scores != 'No output.':
            def fmt(score):
                try:
                    return f"{float(score):.2f}" if score is not None and score != 'N/A' else str(score)
                except Exception:
                    return str(score)
            f.write(f"| {label} | {fmt(scores.get('completeness', 'N/A'))}/3 | {fmt(scores.get('rationale_quality', 'N/A'))}/3 | {fmt(scores.get('structure_quality', 'N/A'))}/3 |\n")
        else:
            f.write(f"| {label} | {scores} | {scores} | {scores} |\n")

print("✅ Output saved to results/b2_crewai_dynamic_orchestration.md")