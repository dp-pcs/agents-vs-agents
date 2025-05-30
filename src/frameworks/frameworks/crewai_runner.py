from crewai import Agent, Task, Crew
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def run_crewai_task(task_prompt: str) -> str:
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.3)
    researcher = Agent(
        role='Researcher',
        goal='Find accurate and insightful answers',
        backstory="An expert at pulling key info from the internet.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    task = Task(
        description=task_prompt,
        expected_output="A short, formatted summary with key details.",
        agent=researcher
    )

    crew = Crew(
        agents=[researcher],
        tasks=[task],
        verbose=True
    )

    print("🚀 CrewAI is starting the task...")
    result = crew.kickoff()
    print("✅ CrewAI completed the task.")
    print(f"📝 Output:\n{result}")
    return result

if __name__ == "__main__":
    result = run_crewai_task(
        "Based on statistical analysis of trends for NFL quarterbacks over the past 5 years, "
        "which 2nd year starting quarterbacks are most likely to have a successful 2025–2026 season, and why?"
    )
    print(result)