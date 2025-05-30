import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.frameworks.autogen_educator import run_autogen_educator_task
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

start = time.time()
# Step 1: Generate plan with AutoGen (Claude)
print("📚 AutoGen generating with Claude...")
plan_output = run_autogen_educator_task(llm_model="claude-3-opus-20240229")

# Step 2: Score with OpenAI
openai_llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

from src.shared.prompt_utils import load_prompt

evaluation_prompt = load_prompt() + f"\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}"

print("🧠 OpenAI evaluating...")
evaluation_md = openai_llm.invoke(evaluation_prompt)

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
output_file = os.path.join(output_dir, f"b1_autogen_claude_openai_{dt_str}.md")
with open(output_file, "w") as f:
    f.write("## AutoGen with Claude Output\n\n")
    f.write(plan_output)
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(evaluation_md)
    f.write(f"\n\n**Time to complete:** {time.time() - start:.2f} seconds\n")

print(f"\u2705 Saved to {output_file}\n\u23f1\ufe0f Duration: {time.time() - start:.2f} seconds")