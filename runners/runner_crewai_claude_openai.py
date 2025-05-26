import os
from dotenv import load_dotenv
from openai import OpenAI
from frameworks.crewai_educator import run_crewai_educator_task

load_dotenv()

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from anthropic import Anthropic
from frameworks.crewai_educator import run_crewai_educator_task
import time
start = time.time()
# Step 1: CrewAI generates plan using Claude
print("\U0001F4DA CrewAI generating with Claude...")
plan_output = run_crewai_educator_task(llm_model="claude-3-opus-20240229")

# Step 2: OpenAI evaluates
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
evaluation_prompt = f"""
Evaluate the following AI-generated output for a 12-week AI/ML learning plan. Score it 1–5 in each category:\n\n
1. Task Execution
2. Output Clarity
3. Error Recovery
4. Autonomy & Initiative

Return a markdown table with the scores and a brief summary paragraph.\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}
"""

print("\U0001F9E0 OpenAI evaluating...")
openai_response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": evaluation_prompt}],
    max_tokens=1024,
    temperature=0.3
)
evaluation_md = openai_response.choices[0].message.content

# Save result
os.makedirs("results", exist_ok=True)
with open("results/crewai_claude_openai.md", "w") as f:
    f.write("## CrewAI with Claude Output\n\n")
    f.write(str(plan_output))
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(str(evaluation_md))
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
end = time.time()
duration = end - start
print(f"⏱️ Duration: {duration:.2f} seconds")
