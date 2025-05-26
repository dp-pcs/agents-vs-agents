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

print(" Generating plan with LangChain + Claude...")
plan_output = claude_llm.invoke(task_prompt)

# === Step 2: OpenAI evaluates the plan ===

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