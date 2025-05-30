import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import time

load_dotenv()

start = time.time()

# === Step 1: LangChain uses Claude to generate the learning plan ===

claude_llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    temperature=0.3,
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

from src.shared.prompt_utils import load_prompt

task_prompt = load_prompt()
print(" Generating plan with LangChain + Claude...")
plan_output = claude_llm.invoke(task_prompt)

# === Step 2: OpenAI evaluates the plan ===

openai_llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

evaluation_prompt = load_prompt() + f"\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}"
print(" Scoring with OpenAI...")
evaluation_md = openai_llm.invoke(evaluation_prompt)

# === Step 3: Save the output ===

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
output_file = os.path.join(output_dir, f"b1_langchain_claude_openai_{dt_str}.md")
with open(output_file, "w") as f:
    f.write("## LangChain with Claude Output\n\n")
    f.write(str(plan_output))
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(str(evaluation_md))
    f.write(f"\n\n**Time to complete:** {time.time() - start:.2f} seconds\n")

print(f"\u2705 Saved to {output_file}\n\u23f1\ufe0f Duration: {time.time() - start:.2f} seconds")