import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from frameworks.autogen_educator import run_autogen_educator_task
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from frameworks.autogen_educator import run_autogen_educator_task
import time

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

evaluation_prompt = (
    f"Evaluate the following AI-generated output for a 12-week AI/ML learning plan. "
    f"Score it 1–5 in each category:\n\n"
    f"1. Task Execution\n"
    f"2. Output Clarity\n"
    f"3. Error Recovery\n"
    f"4. Autonomy & Initiative\n\n"
    f"Return a markdown table with the scores and a brief summary paragraph.\n\n"
    f"---\n\n"
    f"OUTPUT TO EVALUATE:\n{plan_output}"
)

print("🧠 OpenAI evaluating...")
evaluation_md = openai_llm.invoke(evaluation_prompt)

# Save result
os.makedirs("results", exist_ok=True)
with open("results/autogen_claude_openai.md", "w") as f:
    f.write("## AutoGen with Claude Output\n\n")
    f.write(plan_output)
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(evaluation_md)
    f.write(f"\n\n**Time to complete:** {time.time() - start:.2f} seconds\n")

print(f"\u2705 Saved to results/autogen_claude_openai.md\n⏱️ Duration: {time.time() - start:.2f} seconds")