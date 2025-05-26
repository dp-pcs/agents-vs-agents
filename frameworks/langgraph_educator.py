from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

try:
    from langchain_anthropic import ChatAnthropic
except ImportError:
    ChatAnthropic = None

load_dotenv()

def run_langgraph_educator_task(model: str = "gpt-4") -> str:
    if "claude" in model.lower():
        if ChatAnthropic is None:
            raise ImportError("langchain-anthropic is not installed. Install with: pip install langchain-anthropic")
        llm = ChatAnthropic(
            model=model,
            temperature=0.3,
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
        )
    elif "gpt" in model.lower():
        llm = ChatOpenAI(
            model=model,
            temperature=0.3,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    else:
        raise NotImplementedError(f"Unsupported LLM model: {model}. Only OpenAI GPT or Claude models are supported.")
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
    response = llm.invoke(task_prompt)
    # Ensure the result is a string for file writing
    return str(response.content) if hasattr(response, 'content') else str(response)
