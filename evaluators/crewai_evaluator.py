

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def evaluate_output(task_prompt: str, output: str) -> str:
    print("🧠 CrewAI is evaluating LangGraph's output...")

    reviewer = Agent(
        role="Evaluator",
        goal="Review and score AI-generated content.",
        backstory="You are a detail-oriented AI tasked with reviewing other AI outputs.",
        verbose=True,
        llm=llm
    )

    review_instruction = f"""
    TASK:
    {task_prompt}

    OUTPUT:
    {output}

    Please evaluate the result on a scale of 1 to 5 in each of the following categories:
    1. Task Execution
    2. Output Clarity
    3. Error Recovery
    4. Autonomy & Initiative

    Write your response in markdown with:
    - A score breakdown
    - One paragraph of feedback
    - Total score out of 20

    Only return the markdown. Do not include any commentary outside the markdown.
    """

    task = Task(
        description=review_instruction,
        expected_output="A markdown-formatted evaluation report.",
        agent=reviewer
    )

    crew = Crew(agents=[reviewer], tasks=[task], verbose=True)
    result = crew.kickoff()
    return result