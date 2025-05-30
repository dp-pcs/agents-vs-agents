import subprocess
import sys
import os
from datetime import datetime

# Ensure project root is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

scripts = [
    "src.runners.benchmark1.runner_b1_langchain_openai_claude",
    "src.runners.benchmark1.runner_b1_langchain_claude_openai",
    "src.runners.benchmark1.runner_b1_langgraph_openai_claude",
    "src.runners.benchmark1.runner_b1_langgraph_claude_openai",
    "src.runners.benchmark1.runner_b1_crewai_openai_claude",
    "src.runners.benchmark1.runner_b1_crewai_claude_openai",
    "src.runners.benchmark1.runner_b1_autogen_openai_claude",
    "src.runners.benchmark1.runner_b1_autogen_claude_openai"
]


# Create results/benchmark1 if it doesn't exist
run_dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
run_folder = os.path.join("results", "benchmark1", f"benchmark1_{run_dt_str}")
os.makedirs(run_folder, exist_ok=True)

# Symlink latest_run to this run folder
latest_symlink = os.path.join("results", "benchmark1", "latest_run")
if os.path.islink(latest_symlink) or os.path.exists(latest_symlink):
    os.remove(latest_symlink)
os.symlink(os.path.abspath(run_folder), latest_symlink)

log_file = os.path.join(run_folder, f"b1_benchmark_run_{run_dt_str}.log")

with open(log_file, "w") as log:
    for script in scripts:
        log.write(f"\n▶️ Running {script}\n")
        print(f"▶️ Running {script}")
        result = subprocess.run(["python", "-m", script, run_folder], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log.write(result.stdout)
        if result.returncode != 0:
            log.write(f"\n❌ Script {script} failed with exit code {result.returncode}\n")
            print(f"❌ Script {script} failed with exit code {result.returncode}")
        else:
            log.write(f"\n✅ Script {script} completed successfully.\n")

    # Run the summary script and log its output
    summary_script = "src/shared/b1_benchmark_summary.py"
    log.write(f"\n▶️ Running {summary_script}\n")
    print(f"▶️ Running {summary_script}")
    result = subprocess.run(["python", summary_script, run_folder], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log.write(result.stdout)
    if result.returncode != 0:
        log.write(f"\n❌ Summary script failed with exit code {result.returncode}\n")
        print(f"❌ Summary script failed with exit code {result.returncode}")
    else:
        log.write(f"\n✅ Summary script completed successfully.\n")

print(f"\n📝 Benchmark run complete. Log saved to {log_file}\n")
