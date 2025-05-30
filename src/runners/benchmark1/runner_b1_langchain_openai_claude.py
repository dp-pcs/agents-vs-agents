import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from anthropic import Anthropic
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from anthropic import Anthropic
import time

load_dotenv()

start = time.time()

# === Step 1: LangChain uses OpenAI to generate the learning plan ===

openai_llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

from src.shared.prompt_utils import load_prompt

task_prompt = load_prompt()
print(" Generating plan with LangChain + OpenAI...")
plan_output = openai_llm.invoke(task_prompt)

# === Step 2: Claude evaluates the plan ===

anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

claude_prompt = load_prompt() + f"\n\n---\n\nOUTPUT TO EVALUATE:\n{plan_output}"
print(" Claude evaluating...")
claude_response = anthropic_client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    temperature=0.3,
    messages=[{"role": "user", "content": claude_prompt}]
)

evaluation_md = claude_response.content[0].text

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
    # Validate format
    datetime.strptime(dt_str, "%Y-%m-%d_%H-%M-%S")
except Exception:
    dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = os.path.join(output_dir, f"b1_langchain_openai_claude_{dt_str}.md")
with open(output_file, "w") as f:
    f.write("## LangChain with OpenAI Output\n\n")
    f.write(str(getattr(plan_output, 'content', plan_output)))
    f.write("\n\n---\n\n")
    f.write("## Claude Evaluation\n\n")
    f.write(str(getattr(evaluation_md, 'content', evaluation_md)))

end = time.time()
duration = end - start

with open(output_file, "a") as f:
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f"\u2705 Saved to {output_file}\n\u23f1\ufe0f Duration: {duration:.2f} seconds")