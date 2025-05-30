import os
from dotenv import load_dotenv
from anthropic import Anthropic
from src.frameworks.crewai_educator import run_crewai_educator_task
import time

load_dotenv()

start = time.time()
# Step 1: CrewAI generates plan using OpenAI
print("📚 CrewAI generating with OpenAI...")
plan_output = run_crewai_educator_task()

# Step 2: Claude evaluates
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
from src.shared.prompt_utils import load_prompt

claude_prompt = load_prompt() + f"\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}"

print("🧠 Claude evaluating...")
claude_response = anthropic_client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    temperature=0.3,
    messages=[{"role": "user", "content": claude_prompt}]
)

evaluation_md = claude_response.content[0].text

# Save result
os.makedirs("results", exist_ok=True)
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
output_file = os.path.join(output_dir, f"b1_crewai_openai_claude_{dt_str}.md")
with open(output_file, "w") as f:
    f.write("## CrewAI with OpenAI Output\n\n")
    f.write(plan_output)
    f.write("\n\n---\n\n")
    f.write("## Claude Evaluation\n\n")
    f.write(evaluation_md)

end = time.time()
duration = end - start
with open(output_file, "a") as f:
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f"\u2705 Saved to {output_file}")
print(f"⏱️ Duration: {duration:.2f} seconds")