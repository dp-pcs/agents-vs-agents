

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def run_langgraph_task(task_prompt: str) -> str:
    print(f"📤 LangGraph is processing the task:\n{task_prompt}\n")
    response = llm.invoke(task_prompt)
    print("✅ LangGraph completed the task.")
    print(f"📝 Output:\n{response}")
    return response