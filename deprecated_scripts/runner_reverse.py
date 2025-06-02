from frameworks.langgraph_task_runner import run_langgraph_task
from evaluators.crewai_evaluator import evaluate_output
import os

task_prompt = (
    "Based on statistical analysis of trends for NFL quarterbacks over the past 5 years, "
    "which 2nd year starting quarterbacks are most likely to have a successful 2025–2026 season, and why?"
)

print("🔁 Running reverse test: LangGraph executes, CrewAI evaluates")

# LangGraph executes the task
langgraph_result = run_langgraph_task(task_prompt)

# CrewAI evaluates the LangGraph result
evaluation_md = evaluate_output(task_prompt, langgraph_result)

# Save the evaluation result
os.makedirs("results", exist_ok=True)
with open("results/test2_crewai_evaluates_langgraph.md", "w") as f:
    f.write(evaluation_md)

print("✅ Reverse evaluation complete. See results/test2_crewai_evaluates_langgraph.md")