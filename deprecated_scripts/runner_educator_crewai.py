# runner_educator_crewai.py

from frameworks.crewai_educator import run_crewai_educator_task
import os
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from frameworks.crewai_educator import run_crewai_educator_task
import time

start = time.time()
print(" Running CrewAI Educator Benchmark")

# Run the CrewAI education planning task
result = run_crewai_educator_task()
end = time.time()
duration = end - start
# Save the result
os.makedirs("results", exist_ok=True)
with open("results/educator_crewai.md", "w") as f:
    f.write(result)
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f" Benchmark complete. Output saved to results/educator_crewai.md\n Duration: {duration:.2f} seconds")