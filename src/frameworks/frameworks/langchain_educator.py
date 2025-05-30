from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def run_langchain_educator_task() -> str:
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
