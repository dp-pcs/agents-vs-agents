# evaluators/langgraph_evaluator.py

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(
    model="gpt-4",  # Feel free to downgrade to gpt-3.5-turbo if needed
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Evaluation scoring prompt
evaluation_prompt = ChatPromptTemplate.from_template("""
You are an expert evaluator judging the performance of an AI agent.

The task assigned was:

"{task}"

The agent produced the following output:

"{output}"

Evaluate the result on a scale of 1 to 5 in each of the following categories:

1. Task Execution
2. Output Clarity
3. Error Recovery
4. Autonomy & Initiative

Then write a markdown-formatted report with:
- A score breakdown
- One paragraph of feedback
- Total score (out of 20)

Only return markdown. No extra commentary.
""")

def evaluate_output(task: str, output: str) -> str:
    prompt = evaluation_prompt.format_messages(task=task, output=output)
    response = llm(prompt)
    return response.content