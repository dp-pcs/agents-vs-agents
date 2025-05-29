import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Import common configurations
from Shared.config_common import SYSTEM_PROMPTS, USER_GOAL, save_results

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

# --- Subclass for message windowing ---
class WindowedAssistantAgent(AssistantAgent):
    def __init__(self, *args, max_history=12, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_history = max_history

    def generate_reply(self, messages=None, sender=None):
        if messages is not None and len(messages) > self.max_history:
            messages = messages[-self.max_history:]
        return super().generate_reply(messages=messages, sender=sender)

# Config for OpenAI (gpt-4)
config_list = [{
    'model': 'gpt-4o',
    'api_key': os.getenv('OPENAI_API_KEY')
}]

# Create expert assistant agents using standardized prompts
research_agent = WindowedAssistantAgent(
    name="ExecutiveSummaryAgent",
    system_message=SYSTEM_PROMPTS["executive_summary"],
    llm_config={"config_list": config_list},
    max_history=12
)

market_analysis_agent = WindowedAssistantAgent(
    name="MarketAnalysisAgent",
    system_message=SYSTEM_PROMPTS["market_analysis"],
    llm_config={"config_list": config_list},
    max_history=12
)

product_agent = WindowedAssistantAgent(
    name="ProductStrategyAgent",
    system_message=SYSTEM_PROMPTS["product_strategy"],
    llm_config={"config_list": config_list},
    max_history=12
)

go_to_market_agent = WindowedAssistantAgent(
    name="GoToMarketAgent",
    system_message=SYSTEM_PROMPTS["go_to_market"],
    llm_config={"config_list": config_list},
    max_history=12
)

financial_agent = WindowedAssistantAgent(
    name="FinancialAgent",
    system_message=SYSTEM_PROMPTS["financial"],
    llm_config={"config_list": config_list},
    max_history=12
)

team_agent = WindowedAssistantAgent(
    name="TeamAgent",
    system_message=SYSTEM_PROMPTS["team_roles"],
    llm_config={"config_list": config_list},
    max_history=12
)

risks_agent = WindowedAssistantAgent(
    name="RisksAgent",
    system_message=SYSTEM_PROMPTS["risks"],
    llm_config={"config_list": config_list},
    max_history=12
)

pm_agent = WindowedAssistantAgent(
    name="TimelineAgent",
    system_message=SYSTEM_PROMPTS["timeline"],
    llm_config={"config_list": config_list},
    max_history=12
)

conclusion_agent = WindowedAssistantAgent(
    name="ConclusionAgent",
    system_message=SYSTEM_PROMPTS["conclusion"],
    llm_config={"config_list": config_list},
    max_history=12
)

baseball_coach_agent = WindowedAssistantAgent(
    name="BaseballCoachAgent",
    system_message=SYSTEM_PROMPTS["baseball_coach"],
    llm_config={"config_list": config_list},
    max_history=12
)

# Orchestrator agent
orchestrator = WindowedAssistantAgent(
    name="COOAgent",
    system_message=SYSTEM_PROMPTS["orchestrator"],
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

def run_autogen_test():
    print("🚀 Starting AutoGen dynamic multi-agent orchestration test...\n")

    # Start the test and measure time
    start = time.time()
    
    initial_message = {"content": USER_GOAL, "role": "user", "name": user_proxy.name}
    messages = [initial_message]
    final_plan = ""

    # Step-by-step chat: break when COOAgent outputs the final plan
    for i in range(groupchat.max_round):
        manager.run_chat(messages=messages, sender=user_proxy, config=groupchat)
        # Check for final COOAgent message
        for m in reversed(groupchat.messages):
            content_lower = m["content"].lower()
            if m["name"] == "COOAgent" and "rationale" in content_lower and ("operational plan" in content_lower or "business plan" in content_lower) and "here is the final" in content_lower:
                final_plan = m["content"]
                print(f"[DEBUG] Found final plan message, length: {len(final_plan)}")
                break
        if final_plan:
            break
    
    end = time.time()
    duration = round(end - start, 2)

    # More robust extraction of final plan if the exact matching failed
    if not final_plan:
        print("[DEBUG] No exact matching final plan found. Trying alternative extraction methods...")
        
        # Try to find any substantial COOAgent message
        coo_messages = [m for m in groupchat.messages if m["name"] == "COOAgent"]
        if coo_messages:
            for m in reversed(coo_messages):
                if len(m["content"]) > 500:  # A substantial message
                    final_plan = m["content"]
                    print(f"[DEBUG] Found long COOAgent message, length: {len(final_plan)}")
                    break
    
    # Section agent definition
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
    
    # Analyze agent usage and irrelevant agent filtering
    print("\n[ANALYSIS] Agent Selection Behavior:")
    section_agent_counts = {}
    for agent_name in section_agent_names:
        count = sum(1 for m in groupchat.messages if m["name"] == agent_name)
        section_agent_counts[agent_name] = count
        print(f"- {agent_name}: {count} messages")

    # Special focus on BaseballCoachAgent
    baseball_messages = [m for m in groupchat.messages if m["name"] == "BaseballCoachAgent"]
    if baseball_messages:
        print(f"[FINDING] BaseballCoachAgent was used despite being irrelevant ({len(baseball_messages)} messages)")
        print(f"First baseball message: {baseball_messages[0]['content'][:100]}...")
    else:
        print("[FINDING] BaseballCoachAgent was correctly filtered out")
    
    # Count messages from section agents as agent turns
    agent_turns = sum(1 for m in groupchat.messages if m["name"] in section_agent_names)
    
    # If still no final plan, try to assemble one from section messages
    if not final_plan:
        print("[DEBUG] No COOAgent final plan found. Attempting to assemble from section agents...")
        section_contents = {}
        
        # Extract content from each section agent
        for m in groupchat.messages:
            if m["name"] in section_agent_names and len(m["content"]) > 50 and m["name"] != "BaseballCoachAgent":
                section_contents[m["name"]] = m["content"]
        
        # If we found section content, combine it
        if section_contents:
            # Add a rationale header
            assembled_plan = "# AI Productivity App Business Plan\n\n"
            assembled_plan += "## Rationale\n\nThis business plan was created by coordinating expert agents for different sections. "
            
            # Note about BaseballCoachAgent
            if baseball_messages:
                assembled_plan += "The BaseballCoachAgent was incorrectly used despite being irrelevant to the business task.\n\n"
            else:
                assembled_plan += "The BaseballCoachAgent was correctly identified as irrelevant and not used.\n\n"
            
            # Add section contents in a logical order
            for agent_name in [
                "ExecutiveSummaryAgent",
                "MarketAnalysisAgent",
                "ProductStrategyAgent",
                "GoToMarketAgent",
                "FinancialAgent",
                "TeamAgent",
                "RisksAgent",
                "TimelineAgent",
                "ConclusionAgent"
            ]:
                if agent_name in section_contents:
                    assembled_plan += section_contents[agent_name] + "\n\n"
            
            final_plan = assembled_plan
            print(f"[DEBUG] Assembled plan from sections, total length: {len(final_plan)}")

    # Save results and output (Bedrock scoring removed)
    os.makedirs("results", exist_ok=True)
    try:
        output_file = "results/b2_autogen_dynamic_orchestration.md"
        print(f"[DEBUG] Writing to: {output_file}")
        
        with open(output_file, "w") as f:
            timestamp = datetime.now().isoformat()
            f.write(f"Generated: {timestamp}\n# AutoGen Dynamic Orchestration Output\n\n")
            
            # Add framework behavior analysis
            f.write("## Framework Behavior Analysis\n\n")
            
            # Document agent selection behavior
            f.write("### Agent Selection:\n")
            for agent_name in section_agent_names:
                count = sum(1 for m in groupchat.messages if m["name"] == agent_name)
                f.write(f"- **{agent_name}**: {count} messages\n")
            
            # Highlight irrelevant agent handling
            if baseball_messages:
                f.write(f"\n**FINDING**: BaseballCoachAgent was incorrectly used despite being irrelevant to the business task. The framework did not properly filter irrelevant agents.\n\n")
                f.write(f"BaseballCoach contribution: \n```\n{baseball_messages[0]['content'][:300]}...\n```\n\n")
            else:
                f.write(f"\n**FINDING**: BaseballCoachAgent was correctly identified as irrelevant and filtered out.\n\n")
            
            f.write("## Business Plan Content\n\n")
            
            # Add the actual business plan content
            if final_plan:
                f.write(final_plan)
            else:
                f.write("[WARNING] No comprehensive business plan was generated.\n\n")
                
                # Try to recover by logging the last COOAgent message
                for m in reversed(groupchat.messages):
                    if m["name"] == "COOAgent":
                        f.write(f"Last COOAgent message:\n\n{m['content']}")
                        break
            
            # Write standard metadata
            f.write(f"\n\n**Time to complete:** {duration} seconds\n")
            f.write(f"\n**Agent turns:** {agent_turns}\n")
        print(f"[DEBUG] Successfully wrote output to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to write output file: {str(e)}")
        # Try to write to a different location as fallback
        try:
            with open("autogen_output_fallback.txt", "w") as f:
                f.write(f"Error with original file: {str(e)}\n\n")
                f.write(f"Final plan length: {len(final_plan) if final_plan else 0}\n\n")
                if final_plan:
                    f.write(final_plan)
        except Exception as inner_e:
            print(f"[ERROR] Even fallback file writing failed: {str(inner_e)}")
    
    # Return values for the comparison script
    # Save results (Bedrock scoring removed)
    save_results("autogen", final_plan, duration, agent_turns, {})
    return final_plan, duration, agent_turns

if __name__ == "__main__":
    run_autogen_test()