import os
from dotenv import load_dotenv
from openai import OpenAI
from src.frameworks.crewai_educator import run_crewai_educator_task

load_dotenv()

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from anthropic import Anthropic
import time
start = time.time()
# Step 1: CrewAI generates plan using Claude
print("\U0001F4DA CrewAI generating with Claude...")
plan_output = run_crewai_educator_task(llm_model="claude-3-opus-20240229")

# Step 2: OpenAI evaluates
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from src.shared.prompt_utils import load_prompt

evaluation_prompt = load_prompt() + f"\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}"

print("\U0001F9E0 OpenAI evaluating...")
openai_response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": evaluation_prompt}],
    max_tokens=1024,
    temperature=0.3
)
evaluation_md = openai_response.choices[0].message.content

print("\n--- DEBUG: evaluation_md ---\n")
print(evaluation_md)
print("\n--- END DEBUG ---\n")

# Save result
os.makedirs("results", exist_ok=True)
end = time.time()
duration = end - start
import sys
from datetime import datetime
# Accept output directory as argument
if len(sys.argv) > 1:
    output_dir = sys.argv[1]
else:
    output_dir = "results/benchmark1"
os.makedirs(output_dir, exist_ok=True)
# Use timestamp from output_dir if present, else generate new
try:
    dt_str = os.path.basename(output_dir).replace('benchmark1_', '')
    datetime.strptime(dt_str, "%Y-%m-%d_%H-%M-%S")
except Exception:
    dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = os.path.join(output_dir, f"b1_crewai_claude_openai_{dt_str}.md")
with open(output_file, "w") as f:
    f.write("## CrewAI with Claude Output\n\n")
    f.write(str(plan_output))
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(str(evaluation_md))
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f"\u2705 Saved to {output_file}\n\u23f1\ufe0f Duration: {duration:.2f} seconds")
