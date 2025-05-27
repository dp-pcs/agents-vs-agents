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
from runners.prompt_utils import load_prompt

evaluation_prompt = load_prompt() + f"\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}"

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
end = time.time()
duration = end - start
with open("results/crewai_claude_openai.md", "w") as f:
    f.write("## CrewAI with Claude Output\n\n")
    f.write(str(plan_output))
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(str(evaluation_md))
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f"⏱️ Duration: {duration:.2f} seconds")
