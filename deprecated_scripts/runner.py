# runner.py

from frameworks.crewai_runner import run_crewai_task
from evaluators.langgraph_evaluator import evaluate_output
import os

# Define the task LangGraph wants CrewAI to do
task_prompt = (
    "Based on statistical analysis of trends for NFL quarterbacks over the past 5 years, "
    "which 2nd year starting quarterbacks are most likely to have a successful 2025–2026 season, and why?"
)

# Run task with CrewAI
print("🔧 Running task via CrewAI...")
crewai_result = run_crewai_task(task_prompt)

# Evaluate result with LangGraph evaluator
print("🧠 Evaluating CrewAI’s result with LangGraph evaluator...")
evaluation_md = evaluate_output(task_prompt, crewai_result)

# Save result
os.makedirs("results", exist_ok=True)
with open("results/test1_langgraph_to_crewai.md", "w") as f:
    f.write(evaluation_md)

print("✅ Evaluation complete. See results/test1_langgraph_to_crewai.md")