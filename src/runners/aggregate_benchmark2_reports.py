import os
import re
import json
from glob import glob
from collections import defaultdict

RESULTS_PARENT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../results/benchmark2'))
REPORT_PATTERN = os.path.join(RESULTS_PARENT, 'benchmark2_*', 'benchmark_report.md')

# Regex patterns to extract scores from markdown tables
SCORE_ROW_PATTERN = re.compile(r'^\|\s*(\w+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|')
HEADER_PATTERN = re.compile(r'^\|\s*Framework\s*\|', re.IGNORECASE)

framework_scores = defaultdict(list)

for report_path in glob(REPORT_PATTERN):
    with open(report_path, 'r') as f:
        lines = f.readlines()
    # Find the score table
    in_table = False
    for line in lines:
        if HEADER_PATTERN.match(line):
            in_table = True
            continue
        if in_table:
            if line.strip().startswith('|---'):
                continue
            if not line.strip().startswith('|'):
                break  # End of table
            m = SCORE_ROW_PATTERN.match(line)
            if m:
                framework = m.group(1)
                scores = list(map(int, m.groups()[1:]))
                framework_scores[framework].append(scores)

# Compute averages
summary = '| Framework | Completeness | Rationale | Structure |\n'
summary += '|-----------|--------------|-----------|-----------|\n'

for framework, scores_list in framework_scores.items():
    if not scores_list:
        continue
    n = len(scores_list)
    avg_scores = [sum(x[i] for x in scores_list) / n for i in range(3)]
    summary += f'| {framework} | {avg_scores[0]:.2f} | {avg_scores[1]:.2f} | {avg_scores[2]:.2f} |\n'

output_path = os.path.join(RESULTS_PARENT, 'compiled_benchmark_reports.md')
with open(output_path, 'w') as f:
    f.write('# Aggregated Benchmark2 Results\n\n')
    f.write(f'Aggregated from {len(framework_scores)} frameworks across {len(glob(REPORT_PATTERN))} runs.\n\n')
    f.write(summary)

print(f'✅ Aggregated report written to {output_path}')
