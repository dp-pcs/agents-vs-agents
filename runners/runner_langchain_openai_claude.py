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

task_prompt = (
    "You are an AI educational coach. A user has asked for help designing a personalized learning plan to become proficient in AI and machine learning.\n\n"
    "They already know:\n"
    "- Python programming\n"
    "- Basic statistics\n\n"
    "They want to:\n"
    "- Learn the core foundations of machine learning\n"
    "- Understand how large language models work\n"
    "- Build hands-on projects using real datasets\n\n"
    "Constraints:\n"
    "- The user has ~10 hours per week to learn\n"
    "- The total plan should last 12 weeks\n\n"
    "Your task:\n"
    "1. Design a 12-week curriculum that builds progressively each week\n"
    "2. Include at least one hands-on project every 3–4 weeks\n"
    "3. Recommend specific courses, tutorials, or reading (include links if possible)\n"
    "4. Make sure the difficulty increases over time — don’t start with transformers\n"
    "5. Output the plan in a clear markdown table:\n"
    "   - Week\n"
    "   - Topics\n"
    "   - Resources\n"
    "   - Project (if applicable)\n"
    "6. At the end, write a summary explaining:\n"
    "   - Why this order makes sense\n"
    "   - How it balances theory + practice\n"
    "   - What the user should know by the end"
)

print(" Generating plan with LangChain + OpenAI...")
plan_output = openai_llm.invoke(task_prompt)

# === Step 2: Claude evaluates the plan ===

anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

claude_prompt = f"""
Evaluate the following AI-generated output for a 12-week AI/ML learning plan. Score it 1–5 in each category:

1. Task Execution
2. Output Clarity
3. Error Recovery
4. Autonomy & Initiative

Return a markdown table with the scores and a brief summary paragraph.

---

OUTPUT TO EVALUATE:
{plan_output}
"""

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
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")

end = time.time()
duration = end - start
print(f" Saved to results/langchain_openai_claude.md\n Duration: {duration:.2f} seconds")