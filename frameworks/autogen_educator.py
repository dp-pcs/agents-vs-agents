# AutoGen educator agent implementation
# Requires: pip install pyautogen
import os
from dotenv import load_dotenv

try:
    import autogen
except ImportError:
    raise ImportError("AutoGen is not installed. Install with: pip install pyautogen")

load_dotenv()


def run_autogen_educator_task(llm_model: str = "gpt-4") -> str:
    if "claude" in llm_model.lower():
        raise NotImplementedError("AutoGen does not support Claude or Anthropic models. Use OpenAI-compatible models only.")
    task_prompt = (
        "You are an AI educational coach. A user has asked for help designing a personalized learning plan to become proficient in AI and machine learning.\n\n"
        "They already know:\n"
        "- Python programming\n"
        "- Basic statistics\n\n"
        "They want to:\n"
        "- Learn the core foundations of machine learning\n"
        "- Understand how large language models work\n"
        "- Build hands-on projects using real datasets\n\n"
        "Constraints:\n"
        "- The user has ~10 hours per week to learn\n"
        "- The total plan should last 12 weeks\n\n"
        "Your task:\n"
        "1. Design a 12-week curriculum that builds progressively each week\n"
        "2. Include at least one hands-on project every 3–4 weeks\n"
        "3. Recommend specific courses, tutorials, or reading (include links if possible)\n"
        "4. Make sure the difficulty increases over time — don’t start with transformers\n"
        "5. Output the plan in a clear markdown table:\n"
        "   - Week\n"
        "   - Topics\n"
        "   - Resources\n"
        "   - Project (if applicable)\n"
        "6. At the end, write a summary explaining:\n"
        "   - Why this order makes sense\n"
        "   - How it balances theory + practice\n"
        "   - What the user should know by the end"
    )

    if llm_model == "claude-3-opus-20240229":
        config_list = [{
            'model': llm_model,
            'api_key': os.getenv('ANTHROPIC_API_KEY'),
            'base_url': 'https://api.anthropic.com'
        }]
    else:
        config_list = [{
            'model': llm_model,
            'api_key': os.getenv('OPENAI_API_KEY')
        }]

    assistant = autogen.AssistantAgent(
        name="EducatorAgent",
        llm_config={"config_list": config_list, "cache_seed": 42},
        system_message="You are an expert AI educational coach."
    )

    messages = assistant.generate_reply([{"role": "user", "content": task_prompt}])
    if isinstance(messages, list) and len(messages) > 0:
        msg = messages[0]
        if isinstance(msg, dict) and "content" in msg:
            return str(msg["content"])
        else:
            return str(msg)
    return str(messages)
