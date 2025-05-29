import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from anthropic import Anthropic
from frameworks.autogen_educator import run_autogen_educator_task
import time

load_dotenv()

start = time.time()
# Step 1: Generate plan with AutoGen (OpenAI)
print("📚 AutoGen generating with OpenAI...")
plan_output = run_autogen_educator_task(llm_model="gpt-4")

# Step 2: Score with Claude
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
from runners.prompt_utils import load_prompt

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
with open("results/autogen_openai_claude.md", "w") as f:
    f.write("## AutoGen with OpenAI Output\n\n")
    f.write(plan_output)
    f.write("\n\n---\n\n")
    f.write("## Claude Evaluation\n\n")
    f.write(evaluation_md)
    f.write(f"\n\n**Time to complete:** {time.time() - start:.2f} seconds\n")

print(f"\u2705 Saved to results/autogen_openai_claude.md\n⏱️ Duration: {time.time() - start:.2f} seconds")