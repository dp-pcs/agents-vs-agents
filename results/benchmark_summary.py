import os
import re

RESULTS_DIR = "results"
SUMMARY_FILE = os.path.join(RESULTS_DIR, "benchmark_summary.md")

header = "| Framework | LLM | Evaluator | Task | Clarity | Recovery | Autonomy | Total | Time (s) |\n"
divider = "|-----------|-----|-----------|------|---------|----------|----------|--------|----------|\n"
rows = []

for filename in sorted(os.listdir(RESULTS_DIR)):
    if not filename.endswith(".md") or "summary" in filename:
        continue

    filepath = os.path.join(RESULTS_DIR, filename)
    with open(filepath, "r") as f:
        content = f.read()

    parts = filename.replace(".md", "").split("_")
    if len(parts) < 3:
        continue

    framework, llm, evaluator = parts[0], parts[1], parts[2]
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

    # Updated total score calculation per user request
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
    f.write("# Agentic Framework Benchmark Summary\n\n")
    f.write(header)
    f.write(divider)
    f.write("\n".join(rows))

print(f"✅ Summary written to {SUMMARY_FILE}")