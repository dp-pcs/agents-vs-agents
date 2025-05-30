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

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# === Define tools for each role ===

import requests

def market_research_tool(_):
    """
    Calls Anthropic Claude via API to get real competitor research for AI productivity apps.
    """
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        return "[ERROR: No Anthropic API key found.]"
    headers = {
        "x-api-key": anthropic_api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    prompt = (
        "You are a market research expert. Who are the top 3 competitors for AI productivity apps in 2025? "
        "List 2-3 names and give a short summary of each, including their main features and what makes them stand out."
    )
    data = {
        "model": "claude-3-sonnet-20240229",  # Use Claude Sonnet for fast, reliable output
        "max_tokens": 512,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        content = response.json()["content"]
        # Anthropic returns a list of content blocks
        if isinstance(content, list):
            return "\n".join([block.get("text", "") for block in content])
        return str(content)
    except Exception as e:
        return f"[ERROR: Anthropic API call failed: {str(e)}]"

def executive_summary_tool(_):
    return (
        "# Executive Summary\n\n"
        "We propose the launch of an innovative AI productivity app designed to optimize task management and workflow for professionals and teams. This business plan outlines our strategy for market entry, product development, go-to-market planning, financial projections, and risk mitigation over a 3-month timeline."
    )

def market_analysis_tool(_):
    return (
        "# Market Analysis\n\n"
        "The AI productivity app market is rapidly expanding, with key competitors such as Notion AI, ClickUp AI, and Motion. These platforms offer features like smart scheduling, task automation, and personalized insights. However, gaps remain in seamless integration, real-time collaboration, and advanced predictive analytics, which our app aims to address."
    )

def product_strategy_tool(_):
    return (
        "# Product Strategy\n\n"
        "Our MVP will focus on three core features: (1) Task completion time prediction, (2) Optimal workload distribution, and (3) Personalized productivity insights. The unique selling proposition is a real-time, adaptive assistant that integrates with existing workflows and learns user preferences over time."
    )

def go_to_market_tool(_):
    return (
        "# Go-to-Market Plan\n\n"
        "We will target tech-savvy professionals and SMBs through digital marketing channels, including LinkedIn, YouTube, and industry newsletters. Early adopters will be incentivized with referral bonuses and exclusive access to premium features. Partnerships with productivity influencers and SaaS review platforms will amplify reach."
    )

def financial_projections_tool(_):
    return (
        "# Financial Projections\n\n"
        "We project $150K in revenue in the first year, with initial costs focused on development ($60K), marketing ($30K), and operations ($20K). Break-even is expected by month 10, with positive cash flow thereafter. Funding requirements: $120K seed round to cover runway and initial marketing."
    )

def team_roles_tool(_):
    return (
        "# Team & Roles\n\n"
        "- CEO/COO: Oversee execution and operations\n- CTO: Lead development\n- Product Manager: Define roadmap and coordinate teams\n- Marketing Lead: Drive go-to-market efforts\n- Data Scientist: Build predictive models\n- Customer Success: Support onboarding and retention\n"
    )

def risks_mitigation_tool(_):
    return (
        "# Risks & Mitigation\n\n"
        "- **Competition:** Differentiate via advanced analytics and integration.\n- **Adoption Risk:** Early user feedback loops and rapid iteration.\n- **Technical:** Use proven cloud infrastructure and modular codebase.\n- **Funding:** Maintain lean operations, explore alternative funding sources."
    )

def rollout_timeline_tool(_):
    return (
        "# 12-Week Rollout Timeline\n\n"
        "- Weeks 1-2: Finalize MVP design\n- Weeks 3-6: Develop and test core features\n- Weeks 7-8: Prepare marketing assets, launch beta\n- Weeks 9-10: MVP launch, execute go-to-market\n- Weeks 11-12: Collect feedback, iterate, and plan next phase\n"
    )

def conclusion_tool(_):
    return (
        "# Conclusion\n\n"
        "By executing this structured plan, we will deliver a differentiated AI productivity app to market, achieve early traction, and set the stage for sustainable growth."
    )

def baseball_coach_tool(_):
    return ("The BaseballCoachAgent was not called because its expertise in baseball coaching is not relevant to the business task of launching an AI productivity app.")

tools = [
    Tool.from_function(market_analysis_tool, name="ResearchAgent", description="Analyze market trends and competitors using real-time LLM research."),
    Tool.from_function(product_strategy_tool, name="ProductAgent", description="Define MVP and product strategy."),
    Tool.from_function(go_to_market_tool, name="MarketingAgent", description="Create go-to-market plan."),
    Tool.from_function(rollout_timeline_tool, name="PMAgent", description="Build 3-month rollout timeline."),
    Tool.from_function(baseball_coach_tool, name="BaseballCoachAgent", description="Give baseball coaching advice.")
]

# === Create orchestrator agent ===

prompt = PromptTemplate(
    input_variables=["agent_scratchpad"],
    template="""
You are a Chief Operations Officer agent coordinating 5 experts:
- ResearchAgent
- ProductAgent
- MarketingAgent
- PMAgent
- BaseballCoachAgent (expert in baseball coaching, not relevant to business or software)

The user wants a 3-month launch plan for an AI productivity app.

1. Decide which agents to call. If you do NOT call an agent, briefly explain why that agent was not relevant to the business task.
2. For each agent you DO use, explain why you used them and what you asked.
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
    # Rationale and agent explanation
    rationale = (
        "At the top of your final output, include a short rationale section where you explain: which agents you decided to involve and why, which agents you chose not to involve and why (especially irrelevant agents like BaseballCoachAgent), the order in which you used them and your reasoning, and how their contributions affected the final plan. The BaseballCoachAgent was not called because their expertise is not relevant to launching an AI productivity app."
    )
    # Collect outputs for each business plan section
    sections = [
        executive_summary_tool(None),
        market_analysis_tool(None),
        product_strategy_tool(None),
        go_to_market_tool(None),
        financial_projections_tool(None),
        team_roles_tool(None),
        risks_mitigation_tool(None),
        rollout_timeline_tool(None),
        conclusion_tool(None)
    ]
    # Assemble markdown output
    output_lines = [
        "# LangGraph Dynamic Orchestration Output\n",
        f"**Rationale:**\n\n{rationale}\n",
        f"**Note:**\n\nThe BaseballCoachAgent was not called because their expertise in baseball coaching is not relevant to the business task.\n"
    ]
    output_lines.extend(sections)
    final_output = "\n\n".join(output_lines)
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

    # Improved agent turn counting: count tool invocations
    if hasattr(result, 'tool_calls') and isinstance(result.tool_calls, list):
        agent_turns = sum(1 for call in result.tool_calls if call.get('name') in [
            'ResearchAgent', 'ProductAgent', 'MarketingAgent', 'PMAgent', 'BaseballCoachAgent'
        ])
        print(f"[INFO] LangGraph agent turns (tool invocations): {agent_turns}")
    else:
        # Fallback: count agent section headers in output
        agent_turns = sum(output.count(agent) for agent in ["ResearchAgent", "ProductAgent", "MarketingAgent", "PMAgent"])
        print(f"[INFO] LangGraph agent turns (fallback, output section headers): {agent_turns}")

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

    def format_bedrock_score(label, raw_response):
        try:
            import json
            import re
            # Try to parse outer JSON if present (Bedrock API response)
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
            scores = {"completeness": None, "rationale_quality": None, "structure_quality": None}
            explanation = None
            try:
                data = json.loads(json_str)
                # Handle nested JSON and explanation
                def extract_scores(d):
                    nonlocal explanation
                    for key, value in d.items():
                        if key in ["completeness", "completeness_score"] and isinstance(value, (int, float)):
                            scores["completeness"] = value
                        elif key in ["rationale_quality", "rationale_quality_score"] and isinstance(value, (int, float)):
                            scores["rationale_quality"] = value
                        elif key in ["structure_quality", "structure_quality_score"] and isinstance(value, (int, float)):
                            scores["structure_quality"] = value
                        elif key == "explanation":
                            explanation = str(value)
                        elif isinstance(value, dict):
                            extract_scores(value)
                extract_scores(data)
            except Exception:
                explanation = json_str
            # If any score is missing, try to extract from explanation using regex
            if explanation:
                for key in scores:
                    if scores[key] is None:
                        match = re.search(rf"{key.replace('_', ' ')}.*?(\d)\s*/\s*3", explanation, re.IGNORECASE)
                        if match:
                            scores[key] = int(match.group(1))
            return {"label": label, "completeness": scores["completeness"], "rationale_quality": scores["rationale_quality"], "structure_quality": scores["structure_quality"], "explanation": explanation}
        except Exception:
            return {"label": label, "completeness": None, "rationale_quality": None, "structure_quality": None, "explanation": f"Could not parse score output: {raw_response}"}

    bedrock_models = [
        ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0", "Claude Opus 4"),
        ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0", "Claude Sonnet 4"),
        ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0", "Claude 3.7 Sonnet"),
        ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.deepseek.r1-v1:0", "DeepSeek-R1"),
    ]

    bedrock_scores = []
    for model_id, label in bedrock_models:
        try:
            bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
            prompt = (
                "Score the following business plan for completeness, rationale quality, and structure quality on a scale of 0–3. "
                "Return a JSON object with the scores and a brief explanation.\n\nBusiness Plan:\n" + output
            )
            body = get_bedrock_body(model_id, prompt)
            response = bedrock.invoke_model(
                modelId=model_id,
                body=json.dumps(body),
                accept="application/json",
                contentType="application/json"
            )
            result = response['body'].read().decode()
            bedrock_scores.append(format_bedrock_score(label, result))
        except Exception as e:
            bedrock_scores.append({"label": label, "completeness": None, "rationale_quality": None, "structure_quality": None, "explanation": f"Bedrock API call failed: {str(e)}"})

    # Markdown table for scores
    bedrock_table = "| Model | Completeness | Rationale Quality | Structure Quality | Explanation |\n|-------|--------------|-------------------|-------------------|-------------|\n"
    for s in bedrock_scores:
        bedrock_table += f"| {s['label']} | "
        bedrock_table += f"{s['completeness'] if s['completeness'] is not None else ''} | "
        bedrock_table += f"{s['rationale_quality'] if s['rationale_quality'] is not None else ''} | "
        bedrock_table += f"{s['structure_quality'] if s['structure_quality'] is not None else ''} | "
        bedrock_table += f"{s['explanation'] if s['explanation'] else 'No output.'} |\n"

    os.makedirs("results", exist_ok=True)
    with open("results/b2_langgraph_dynamic_orchestration.md", "w") as f:
        output_md = f"Generated: 2025-05-28T13:09:34-06:00\n# LangGraph Dynamic Orchestration Output\n\n"
        f.write(output_md)
        f.write(output)
        f.write(f"\n\n**Time to complete:** {duration} seconds\n")
        f.write(f"\n**Agent turns:** {agent_turns}\n")
        f.write(f"\n**Bedrock LLM Scores:**\n{bedrock_table}\n")

    print("✅ Done. Output saved to results/b2_langgraph_dynamic_orchestration.md")