import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Import common configurations
from src.shared.config_common import SYSTEM_PROMPTS, USER_GOAL, save_results

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

def run_autogen_test():
    print("🚀 Starting AutoGen dynamic multi-agent orchestration test...\n")
    
    # Config for OpenAI (gpt-4)
    config_list = [{
        'model': 'gpt-4o',
        'api_key': os.getenv('OPENAI_API_KEY')
    }]
    
    # --- Subclass for message windowing ---
    class WindowedAssistantAgent(AssistantAgent):
        def __init__(self, *args, max_history=12, **kwargs):
            super().__init__(*args, **kwargs)
            self.max_history = max_history

        def generate_reply(self, messages=None, sender=None):
            if messages is not None and len(messages) > self.max_history:
                messages = messages[-self.max_history:]
            return super().generate_reply(messages=messages, sender=sender)
    
    # Create expert assistant agents
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
    
    # Define section agent names for use in analysis
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
    
    # === Start the conversation ===
    
    # Start timing
    start = time.time()
    
    # Create new group chat for this run
    print("Creating group chat...")
    agents = [
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
    ]
    
    # Create the group chat with a clean message history
    gc = GroupChat(
        agents=agents,
        messages=[],
        max_round=30
    )
    
    # Create the manager with the group chat
    manager = GroupChatManager(groupchat=gc, llm_config={"config_list": config_list})
    
    # Initiate conversation with user goal
    print("Starting conversation...")
    message = {"content": USER_GOAL, "role": "user", "name": "UserProxy"}
    user_proxy.initiate_chat(manager, message=message)
    
    # End timing
    end = time.time()
    duration = round(end - start, 2)
    
    # Access the messages from the group chat
    messages = gc.messages
    print(f"Conversation completed with {len(messages)} total messages in {duration} seconds")
    
    # === Extract business plan ===
    # Try multiple approaches to extract the final plan
    final_plan = None
    
    # 1. Look for the final message from COOAgent containing "final business plan"
    coo_messages = [m for m in messages if m["name"] == "COOAgent"]
    print(f"Found {len(coo_messages)} messages from COOAgent")
    
    for m in reversed(coo_messages):
        content = m["content"].lower()
        if "here is the final" in content and len(m["content"]) > 500:
            final_plan = m["content"]
            print(f"Found final plan with marker phrase, length: {len(final_plan)}")
            break
    
    # 2. If no message with marker found, use the longest COOAgent message
    if not final_plan:
        print("No message with marker phrase found. Looking for longest message...")
        longest_message = ""
        for m in coo_messages:
            if len(m["content"]) > len(longest_message):
                longest_message = m["content"]
                
        if len(longest_message) > 500:  # Only use if substantial
            final_plan = longest_message
            print(f"Using longest COOAgent message as plan, length: {len(final_plan)}")
    
    # 3. If still no plan, reconstruct from section agent outputs
    if not final_plan:
        print("Reconstructing from section agent messages...")
        section_outputs = {}
        
        # Get the latest message from each agent
        for name in section_agent_names:
            if name != "BaseballCoachAgent":
                agent_messages = [m for m in messages if m["name"] == name]
                if agent_messages:
                    section_outputs[name] = agent_messages[-1]["content"]
        
        # Assemble the plan if we have section outputs
        if section_outputs:
            # Create a header and rationale
            parts = ["# AI Productivity App Business Plan\n\n"]
            parts.append("## Rationale\n\n")
            parts.append("This business plan combines insights from specialized agents. ")
            
            # Add BaseballCoach analysis
            baseball_messages = [m for m in messages if m["name"] == "BaseballCoachAgent"]
            if baseball_messages:
                parts.append("The BaseballCoachAgent was used despite being irrelevant to this business task.\n\n")
            else:
                parts.append("The BaseballCoachAgent was correctly identified as irrelevant and not used.\n\n")
            
            # Add sections in logical order
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
            
            for name in section_order:
                if name in section_outputs:
                    parts.append(section_outputs[name] + "\n\n")
            
            final_plan = "".join(parts)
            print(f"Reconstructed plan from sections, length: {len(final_plan)}")
    
    # 4. Last resort: create minimal plan
    if not final_plan:
        print("WARNING: Could not extract plan. Creating minimal plan.")
        final_plan = "# AI Productivity App Business Plan (Incomplete)\n\n"
        final_plan += "## Note\n\nUnable to extract complete business plan content from agent conversation.\n\n"
        
        if coo_messages:
            final_plan += "## Partial Content from COO Agent\n\n"
            final_plan += coo_messages[-1]["content"]
    
    # === Analyze and report ===
    # Count agent turns
    agent_turns = sum(1 for m in messages if m["name"] in section_agent_names)
    print(f"Total agent turns: {agent_turns}")
    
    # Check if BaseballCoachAgent was used
    baseball_messages = [m for m in messages if m["name"] == "BaseballCoachAgent"]
    if baseball_messages:
        print(f"[FINDING] BaseballCoachAgent was used despite being irrelevant ({len(baseball_messages)} messages)")
        print(f"First baseball message: {baseball_messages[0]['content'][:100]}...")
    else:
        print("[FINDING] BaseballCoachAgent was correctly filtered out")
    
    # === Save results ===
    # Create directory if it doesn't exist
    from datetime import datetime
    date_str = datetime.now().strftime("%Y-%m-%d")
    raw_output_dir = os.path.join("results", "benchmark2", f"raw_outputs_{date_str}")
    os.makedirs(raw_output_dir, exist_ok=True)
    dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(raw_output_dir, f"autogen_dynamic_orchestration_{dt_str}.md")
    
    try:
        print(f"Writing output to {output_file}...")
        with open(output_file, "w", encoding="utf-8") as f:
            # Write header
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write("# AutoGen Dynamic Orchestration Output\n\n")
            
            # Framework analysis
            f.write("## Framework Behavior Analysis\n\n")
            
            # Agent selection
            f.write("### Agent Selection:\n")
            for name in section_agent_names:
                count = sum(1 for m in messages if m["name"] == name)
                f.write(f"- **{name}**: {count} messages\n")
            
            # Baseball coach finding
            if baseball_messages:
                f.write("\n**FINDING**: BaseballCoachAgent was incorrectly used despite being irrelevant to the business task.\n\n")
                f.write(f"BaseballCoach contribution: \n```\n{baseball_messages[0]['content'][:300]}...\n```\n\n")
            else:
                f.write("\n**FINDING**: BaseballCoachAgent was correctly identified as irrelevant and filtered out.\n\n")
            
            # Business plan content
            f.write("## Business Plan Content\n\n")
            f.write(final_plan)
            
            # Metadata
            f.write(f"\n\n**Time to complete:** {duration} seconds\n")
            f.write(f"\n**Agent turns:** {agent_turns}\n")
        
        print(f"✅ Output file written successfully")
    except Exception as e:
        print(f"❌ Error writing output file: {str(e)}")
    
    # Use common save function
    save_results("autogen", final_plan, duration, agent_turns, {})
    
    return final_plan, duration, agent_turns, messages

if __name__ == "__main__":
    run_autogen_test()