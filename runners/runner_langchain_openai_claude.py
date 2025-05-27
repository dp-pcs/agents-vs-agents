import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from anthropic import Anthropic
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

from runners.prompt_utils import load_prompt

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
with open("results/langchain_openai_claude.md", "w") as f:
    f.write("## LangChain with OpenAI Output\n\n")
    f.write(str(getattr(plan_output, 'content', plan_output)))
    f.write("\n\n---\n\n")
    f.write("## Claude Evaluation\n\n")
    f.write(str(getattr(evaluation_md, 'content', evaluation_md)))

end = time.time()
duration = end - start

with open("results/langchain_openai_claude.md", "a") as f:
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f" Saved to results/langchain_openai_claude.md\n Duration: {duration:.2f} seconds")