# test_bedrock_single_model.py
from src.runners.benchmark2.b2_full_pipeline_run import score_with_bedrock

test_markdown = """
# Executive Summary

We are launching a productivity tool powered by agents...

# Agents

PlannerAgent, CalendarAgent. No use for BaseballCoachAgent.
"""

model_id = "anthropic.claude-3-sonnet-20240229-v1:0"  # Use only if you're 100% sure you have access

result = score_with_bedrock(test_markdown, model_id)
print(result)
