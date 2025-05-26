import subprocess
import sys
import os
import time

# Ensure project root is in the Python p;ath
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

scripts = [
    "runners/runner_langchain_openai_claude.py",
    "runners/runner_langchain_claude_openai.py",
    "runners/runner_langgraph_openai_claude.py",
    "runners/runner_langgraph_claude_openai.py",
    "runners/runner_crewai_openai_claude.py",
    "runners/runner_autogen_openai_claude.py",
    "results/benchmark_summary.py"
]

for script in scripts:
    print(f"▶️ Running {script}")
    subprocess.run(["python", script])