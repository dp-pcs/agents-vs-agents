import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

from runners.prompt_utils import load_prompt

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
with open("results/langchain_claude_openai.md", "w") as f:
    f.write("## LangChain with Claude Output\n\n")
    f.write(str(plan_output))
    f.write("\n\n---\n\n")
    f.write("## OpenAI Evaluation\n\n")
    f.write(str(evaluation_md))
    f.write(f"\n\n**Time to complete:** {time.time() - start:.2f} seconds\n")

print(f" Saved to results/langchain_claude_openai.md\n Duration: {time.time() - start:.2f} seconds")