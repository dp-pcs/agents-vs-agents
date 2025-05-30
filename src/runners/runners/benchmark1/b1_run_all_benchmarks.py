import subprocess
import sys
import os
from datetime import datetime

# Ensure project root is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

scripts = [
    "runners/runner_langchain_openai_claude.py",
    "runners/runner_langchain_claude_openai.py",
    "runners/runner_langgraph_openai_claude.py",
    "runners/runner_langgraph_claude_openai.py",
    "runners/runner_crewai_openai_claude.py",
    "runners/runner_autogen_openai_claude.py"
]

# Create results/benchmark1 if it doesn't exist
output_dir = os.path.join("results", "benchmark1")
os.makedirs(output_dir, exist_ok=True)

# Prepare a unique output log file for this run
run_dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(output_dir, f"b1_benchmark_run_{run_dt_str}.log")

with open(log_file, "w") as log:
    for script in scripts:
        log.write(f"\n▶️ Running {script}\n")
        print(f"▶️ Running {script}")
        result = subprocess.run(["python", script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log.write(result.stdout)
        if result.returncode != 0:
            log.write(f"\n❌ Script {script} failed with exit code {result.returncode}\n")
            print(f"❌ Script {script} failed with exit code {result.returncode}")
        else:
            log.write(f"\n✅ Script {script} completed successfully.\n")

    # Run the summary script and log its output
    summary_script = "results/benchmark_summary.py"
    log.write(f"\n▶️ Running {summary_script}\n")
    print(f"▶️ Running {summary_script}")
    result = subprocess.run(["python", summary_script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log.write(result.stdout)
    if result.returncode != 0:
        log.write(f"\n❌ Summary script failed with exit code {result.returncode}\n")
        print(f"❌ Summary script failed with exit code {result.returncode}")
    else:
        log.write(f"\n✅ Summary script completed successfully.\n")

print(f"\n📝 Benchmark run complete. Log saved to {log_file}\n")
