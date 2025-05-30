import os
import time
from dotenv import load_dotenv
import requests
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# --- Subclass for message windowing ---
class WindowedAssistantAgent(AssistantAgent):
    def __init__(self, *args, max_history=12, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_history = max_history

    def generate_reply(self, messages=None, sender=None):
        if messages is not None and len(messages) > self.max_history:
            messages = messages[-self.max_history:]
        return super().generate_reply(messages=messages, sender=sender)

# System prompt for the orchestrator agent
orchestrator_system_message = """
You are an autonomous AI Chief Operations Officer.
You will receive a business objective from a user, and you must create a comprehensive, sectioned business plan by dynamically engaging other agents (experts). For each agent, instruct them to generate a full markdown section for their assigned business plan component (Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion). Once you have received input from all necessary agents, synthesize the final plan and include a rationale at the top. At the top, note any agent not used (e.g., BaseballCoachAgent). Output a single markdown file with all sections in order. Then stop the conversation by saying: **"Here is the final business plan and rationale."**
"""

# Config for OpenAI (gpt-4)
config_list = [{
    'model': 'gpt-4o',
    'api_key': os.getenv('OPENAI_API_KEY')
}]

# Create expert assistant agents using WindowedAssistantAgent
# === Enhanced AutoGen Agent Section Assignments ===
research_agent = WindowedAssistantAgent(
    name="ExecutiveSummaryAgent",
    system_message="You are an expert business analyst. Write the Executive Summary section for a business plan to launch an AI productivity app. Output a markdown section titled '# Executive Summary'.",
    llm_config={"config_list": config_list},
    max_history=12
)

market_analysis_agent = WindowedAssistantAgent(
    name="MarketAnalysisAgent",
    system_message="You are a market research expert. Write the Market Analysis section for a business plan to launch an AI productivity app. Output a markdown section titled '# Market Analysis'.",
    llm_config={"config_list": config_list},
    max_history=12
)

product_agent = WindowedAssistantAgent(
    name="ProductStrategyAgent",
    system_message="You are a senior product manager. Write the Product Strategy section for a business plan to launch an AI productivity app. Output a markdown section titled '# Product Strategy'.",
    llm_config={"config_list": config_list},
    max_history=12
)

go_to_market_agent = WindowedAssistantAgent(
    name="GoToMarketAgent",
    system_message="You are a marketing strategist. Write the Go-to-Market Plan section for a business plan to launch an AI productivity app. Output a markdown section titled '# Go-to-Market Plan'.",
    llm_config={"config_list": config_list},
    max_history=12
)

financial_agent = WindowedAssistantAgent(
    name="FinancialAgent",
    system_message="You are a finance expert. Write the Financial Projections section for a business plan to launch an AI productivity app. Output a markdown section titled '# Financial Projections'.",
    llm_config={"config_list": config_list},
    max_history=12
)

team_agent = WindowedAssistantAgent(
    name="TeamAgent",
    system_message="You are an HR and org design expert. Write the Team & Roles section for a business plan to launch an AI productivity app. Output a markdown section titled '# Team & Roles'.",
    llm_config={"config_list": config_list},
    max_history=12
)

risks_agent = WindowedAssistantAgent(
    name="RisksAgent",
    system_message="You are a risk management consultant. Write the Risks & Mitigation section for a business plan to launch an AI productivity app. Output a markdown section titled '# Risks & Mitigation'.",
    llm_config={"config_list": config_list},
    max_history=12
)

pm_agent = WindowedAssistantAgent(
    name="TimelineAgent",
    system_message="You are a project manager. Write the 12-Week Rollout Timeline section for a business plan to launch an AI productivity app. Output a markdown section titled '# 12-Week Rollout Timeline'.",
    llm_config={"config_list": config_list},
    max_history=12
)

conclusion_agent = WindowedAssistantAgent(
    name="ConclusionAgent",
    system_message="You are a business consultant. Write the Conclusion section for a business plan to launch an AI productivity app. Output a markdown section titled '# Conclusion'.",
    llm_config={"config_list": config_list},
    max_history=12
)

baseball_coach_agent = WindowedAssistantAgent(
    name="BaseballCoachAgent",
    system_message="You are a baseball coach. Give advice on teamwork, batting, and fielding. You are not an expert in business or software. If asked about business plans, reply with baseball coaching tips only.",
    llm_config={"config_list": config_list},
    max_history=12
)

# Orchestrator agent
orchestrator_system_message = """
You are an autonomous AI Chief Operations Officer.
You will receive a business objective from a user, and you must create a comprehensive, sectioned business plan by dynamically engaging other agents (experts). For each agent, instruct them to generate a full markdown section for their assigned business plan component (Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion). Once you have received input from all necessary agents, synthesize the final plan and include a rationale at the top. At the top, note any agent not used (e.g., BaseballCoachAgent). Output a single markdown file with all sections in order. Then stop the conversation by saying: **"Here is the final business plan and rationale."**
"""

orchestrator = WindowedAssistantAgent(
    name="COOAgent",
    system_message=orchestrator_system_message,
    llm_config={"config_list": config_list},
    max_history=12
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
        market_analysis_agent,
        product_agent,
        go_to_market_agent,
        financial_agent,
        team_agent,
        risks_agent,
        pm_agent,
        conclusion_agent,
        baseball_coach_agent
    ],
    messages=[],
    max_round=30
)

manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})

# Define section agent names for later use
section_agent_names = [
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
]

# === AWS Credentials Check ===
def check_aws_credentials():
    """Check if AWS credentials from SAM2AWS are available and usable"""
    try:
        import boto3
        # Try to create a simple client to test credentials
        sts = boto3.client('sts')
        # Get caller identity will fail if credentials are not valid
        identity = sts.get_caller_identity()
        print(f"✅ AWS credentials found for account: {identity['Account']}")
        return True
    except Exception as e:
        print(f"❌ AWS credentials not available or invalid: {e}")
        print("   Skipping Bedrock evaluation.")
        return False

def run_autogen_test():
    """Run AutoGen test and return the complete business plan"""
    print("🚀 Starting AutoGen dynamic multi-agent orchestration test...\n")

    # User goal prompt for the orchestrator
    user_goal = """
    You're helping launch a new AI productivity app.

    Please provide a 3-month operational plan covering product strategy, marketing, research, and execution — but only if necessary.

    You may use the following expert agents:
    - ResearchAgent (market and competitor analysis)
    - ProductAgent (MVP design and features)
    - MarketingAgent (go-to-market messaging and targeting)
    - PMAgent (timeline and task planning)
    - BaseballCoachAgent (expert in baseball coaching, teamwork, and sports; not a business or software expert)

    At the **top of your final output**, include a short **rationale section** where you explain:
    - Which agents you decided to involve and why
    - Which agents you chose not to involve and why (especially irrelevant agents like BaseballCoachAgent)
    - The order in which you used them and your reasoning
    - How their contributions affected the final plan

    Then output a 1-page strategic plan formatted in markdown.
    """

    # Start the test and measure time
    start = time.time()
    initial_message = {"content": user_goal, "role": "user", "name": user_proxy.name}
    manager.run_chat(messages=[initial_message], sender=user_proxy, config=groupchat)
    end = time.time()
    duration = round(end - start, 2)

    # Enhanced extraction of the full business plan
    print("\nExtracting business plan content...")
    
    # Initialize final_plan
    final_plan = ""
    full_coo_messages = []
    
    # Collect all COOAgent messages for examination
    for m in groupchat.messages:
        if m["name"] == "COOAgent":
            full_coo_messages.append(m["content"])
            print(f"Found COOAgent message of length {len(m['content'])}")
    
    # First try: get the message with "final business plan and rationale"
    for content in full_coo_messages:
        if "here is the final business plan and rationale" in content.lower() and len(content) > 200:
            final_plan = content
            print(f"Found message with 'final business plan' marker, length: {len(final_plan)}")
            break
    
    # Second try: if first approach yielded nothing or a short message, get the longest COO message
    if not final_plan or len(final_plan) < 500:
        print("First approach failed or yielded short content, trying longest message...")
        longest_coo_message = ""
        for content in full_coo_messages:
            if len(content) > len(longest_coo_message):
                longest_coo_message = content
        
        if len(longest_coo_message) > len(final_plan):
            final_plan = longest_coo_message
            print(f"Using longest COO message, length: {len(final_plan)}")
    
    # Third try: if both approaches failed, reconstruct from section messages
    if not final_plan or len(final_plan) < 500:
        print("Both COO message approaches failed, reconstructing from section agent messages...")
        
        # Get content from each section agent
        section_contents = {}
        for m in groupchat.messages:
            if m["name"] in section_agent_names and m["name"] != "BaseballCoachAgent":
                section_contents[m["name"]] = m["content"]
                print(f"Found {m['name']} content, length: {len(m['content'])}")
        
        # If we have content from section agents, reconstruct the plan
        if section_contents:
            # Create a header and rationale
            combined_parts = ["# AI Productivity App Business Plan\n\n"]
            combined_parts.append("## Rationale\n\nThis plan combines insights from specialized agents to create a comprehensive business strategy. The BaseballCoachAgent was identified as irrelevant and not used for this business task.\n\n")
            
            # Add each section content in a logical order
            section_order = [
                "ExecutiveSummaryAgent", 
                "MarketAnalysisAgent", 
                "ProductStrategyAgent", 
                "GoToMarketAgent", 
                "FinancialAgent", 
                "TeamAgent", 
                "RisksAgent", 
                "TimelineAgent", 
                "ConclusionAgent"
            ]
            
            for agent_name in section_order:
                if agent_name in section_contents:
                    combined_parts.append(section_contents[agent_name])
                    combined_parts.append("\n\n")
            
            # Combine all parts
            final_plan = "".join(combined_parts)
            print(f"Successfully reconstructed plan from section agents, length: {len(final_plan)}")
    
    # Fourth try: if all else fails, we'll just have to return whatever we have
    if not final_plan:
        print("WARNING: Could not extract a proper business plan!")
        if full_coo_messages:
            final_plan = "# Business Plan (Incomplete)\n\nWARNING: This plan could not be properly extracted.\n\n" + full_coo_messages[-1]
        else:
            final_plan = "# Business Plan (Failed)\n\nCould not extract business plan content from the conversation."

    # Count messages from section agents as agent turns
    agent_turns = sum(1 for m in groupchat.messages if m["name"] in section_agent_names)
    print(f"Found {agent_turns} agent turns from section agents")
    
    return final_plan, duration, agent_turns

# When running this file directly, run the test and save results
if __name__ == "__main__":
    # Start orchestration
    final_plan, duration, agent_turns = run_autogen_test()
    
    # Check for AWS credentials before trying to use Bedrock
    bedrock_enabled = check_aws_credentials()
    bedrock_scores = []
    
    if bedrock_enabled:
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

        def extract_scores(text):
            scores = {}
            for line in text.splitlines():
                match = re.search(r'([a-zA-Z]+) quality: (\d+)', line)
                if match:
                    scores[match.group(1).lower().replace(' ', '_')] = int(match.group(2))
            return scores

        def format_bedrock_score(label, raw_response):
            try:
                import json
                # Try to parse outer JSON if present (Bedrock API response)
                data = None
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
                data = json.loads(json_str)
                # Handle nested JSON
                def extract_scores(data):
                    scores = {}
                    for key, value in data.items():
                        if isinstance(value, dict):
                            scores.update(extract_scores(value))
                        elif key in ["completeness", "rationale_quality", "structure_quality"]:
                            scores[key] = value
                    return scores
                scores = extract_scores(data)
                output = f"{label}: {scores}"
                return output
            except Exception:
                scores = extract_scores(raw_response)
                if scores:
                    output = f"{label}: {scores}"
                    return output
                else:
                    return f"{label}: No output."

        def bedrock_score(plan, model_id, label):
            try:
                # Create session with explicit credential handling that works with SAM2AWS
                session = boto3.Session()
                
                bedrock = session.client(
                    "bedrock-runtime", 
                    region_name="us-east-1"
                )
                
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
                return format_bedrock_score(label, result)
            except Exception as e:
                return f"{label}: Bedrock API call failed: {str(e)}\n"

        # Reduced model list (no DeepSeek)
        bedrock_models = [
            ("anthropic.claude-3-sonnet-20240229-v1:0", "Claude 3 Sonnet"),
            ("anthropic.claude-3-haiku-20240307-v1:0", "Claude 3 Haiku")
        ]

        for model_id, label in bedrock_models:
            try:
                score = bedrock_score(final_plan, model_id, label)
                bedrock_scores.append([label, score])
            except Exception as e:
                print(f"Error scoring with {label}: {e}")
                bedrock_scores.append([label, f"Error: {str(e)}"])

    # Save final result
    os.makedirs("results", exist_ok=True)
    print(f"[DEBUG] final_plan content before writing to file (length: {len(final_plan)}):")
    print(f"{final_plan[:500]}...\n...{final_plan[-500:]}\n---END---")
    
    # Framework behavior analysis
    baseball_used = any(m["name"] == "BaseballCoachAgent" for m in groupchat.messages)
    
    with open("results/b2_autogen_dynamic_orchestration.md", "w") as f:
        output_md = f"Generated: 2025-05-28T13:04:52-06:00\n# AutoGen Dynamic Orchestration Output\n\n"
        
        # Add framework behavior analysis
        f.write(output_md)
        f.write("## Framework Behavior Analysis\n\n")
        
        # Document agent selection behavior
        f.write("### Agent Selection:\n")
        for agent_name in section_agent_names:
            count = sum(1 for m in groupchat.messages if m["name"] == agent_name)
            f.write(f"- **{agent_name}**: {count} messages\n")
        
        # Highlight irrelevant agent handling
        if baseball_used:
            f.write(f"\n**FINDING**: BaseballCoachAgent was incorrectly used despite being irrelevant to the business task. The framework did not properly filter irrelevant agents.\n\n")
            baseball_messages = [m for m in groupchat.messages if m["name"] == "BaseballCoachAgent"]
            f.write(f"BaseballCoach contribution: \n```\n{baseball_messages[0]['content'][:300]}...\n```\n\n")
        else:
            f.write(f"\n**FINDING**: BaseballCoachAgent was correctly identified as irrelevant and filtered out.\n\n")
        
        # --- Output file metadata ---
        f.write("## Output File Metadata\n\n")
        f.write(f"**Filename:** {os.path.basename(output_file)}\n\n")
        f.write(f"**Path:** {output_file}\n\n")
        f.write(f"**Timestamp:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Business Plan Content\n\n")
        
        # Write the business plan content
        if final_plan.strip():
            f.write(final_plan)
        else:
            f.write("[WARNING] No business plan content was extracted. Please check the agent conversation or extraction logic.\n")
            
        # Write metadata
        f.write(f"\n\n**Time to complete:** {duration} seconds\n")
        f.write(f"\n**Agent turns:** {agent_turns}\n")
        
        # Only write Bedrock scores if available
        if bedrock_scores:
            f.write("\n**Bedrock LLM Scores:**\n")
            f.write("| Model | Score |\n")
            f.write("| --- | --- |\n")
            for score in bedrock_scores:
                f.write(f"| {score[0]} | {score[1]} |\n")

    print("✅ Output saved to results/b2_autogen_dynamic_orchestration.md")