import os
import re
import sys
from datetime import datetime

# Accept results directory as an argument, default to latest_run
if len(sys.argv) > 1:
    RESULTS_DIR = os.path.abspath(sys.argv[1])
else:
    # Default to latest_run symlink
    default_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../results/benchmark1/latest_run'))
    if os.path.islink(default_dir) or os.path.isdir(default_dir):
        RESULTS_DIR = default_dir
    else:
        raise RuntimeError('No results directory provided and latest_run symlink does not exist.')

SUMMARY_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
SUMMARY_FILE = os.path.join(RESULTS_DIR, f"b1_benchmark_summary_{SUMMARY_TIMESTAMP}.md")

header = "| Framework | LLM | Evaluator | Task | Clarity | Recovery | Autonomy | Total | Time (s) |\n"
divider = "|-----------|-----|-----------|------|---------|----------|----------|--------|----------|\n"
rows = []

for filename in sorted(os.listdir(RESULTS_DIR)):
    if not (filename.startswith("b1_") and filename.endswith(".md")) or "summary" in filename:
        continue

    filepath = os.path.join(RESULTS_DIR, filename)
    with open(filepath, "r") as f:
        content = f.read()

    parts = filename.replace(".md", "").split("_")
    if len(parts) < 3:
        continue

    framework = parts[1] if len(parts) > 1 else "-"
    llm = parts[2] if len(parts) > 2 else "-"
    evaluator = parts[3] if len(parts) > 3 else "-"
    scores = {"Task": "—", "Clarity": "—", "Recovery": "—", "Autonomy": "—", "Total": "—"}
    time_taken = "—"

    match = re.findall(r"\|\s*Task Execution\s*\|\s*(\d+)", content)
    if match:
        scores["Task"] = match[0]

    match = re.findall(r"\|\s*Output Clarity\s*\|\s*(\d+)", content)
    if match:
        scores["Clarity"] = match[0]

    match = re.findall(r"\|\s*Error Recovery\s*\|\s*(\d+)", content)
    if match:
        scores["Recovery"] = match[0]

    match = re.findall(r"\|\s*Autonomy.*?\|\s*(\d+)", content)
    if match:
        scores["Autonomy"] = match[0]

    # Total score
    total = 0
    for k in ["Task", "Clarity", "Recovery", "Autonomy"]:
        if scores[k] != "—":
            total += int(scores[k])
    scores["Total"] = str(total)

    match = re.findall(r"\*\*Time to complete:\*\*\s*([\d.]+)", content)
    if match:
        time_taken = match[0]

    row = f"| {framework.title()} | {llm.upper()} | {evaluator.title()} | {scores['Task']} | {scores['Clarity']} | {scores['Recovery']} | {scores['Autonomy']} | {scores['Total']} | {time_taken} |"
    rows.append(row)

with open(SUMMARY_FILE, "w") as f:
    f.write("# Benchmark 1 Agentic Framework Summary\n\n")
    f.write(header)
    f.write(divider)
    f.write("\n".join(rows))

print(f"✅ Summary written to {SUMMARY_FILE}")
