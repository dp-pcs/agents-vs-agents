import subprocess
import sys
import os
from datetime import datetime

# Ensure project root is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

scripts = [
    "v2_runner_autogen.py",
    "v2_runner_crewai.py",
    "v2_runner_langgraph.py"
]

# Create results/benchmark2 if it doesn't exist
output_dir = os.path.join("results", "benchmark2")
os.makedirs(output_dir, exist_ok=True)

# Prepare a unique output log file for this run
run_dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(output_dir, f"b2_benchmark_run_{run_dt_str}.log")

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

    # Run the summary/report scripts and log their output
    for summary_script in ["run_comparison.py", "score_and_report.py"]:
        log.write(f"\n▶️ Running {summary_script}\n")
        print(f"▶️ Running {summary_script}")
        result = subprocess.run(["python", summary_script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log.write(result.stdout)
        if result.returncode != 0:
            log.write(f"\n❌ {summary_script} failed with exit code {result.returncode}\n")
            print(f"❌ {summary_script} failed with exit code {result.returncode}")
        else:
            log.write(f"\n✅ {summary_script} completed successfully.\n")

print(f"\n📝 Benchmark2 run complete. Log saved to {log_file}\n")
