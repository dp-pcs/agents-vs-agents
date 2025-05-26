from frameworks.autogen_educator import run_autogen_educator_task
import os

print("📚 Running AutoGen Educator Benchmark")

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from frameworks.autogen_educator import run_autogen_educator_task
import time
start = time.time()
# Run the AutoGen education planning task
try:
    result = run_autogen_educator_task()
except NotImplementedError as e:
    result = str(e)
end = time.time()
duration = end - start
# Save the result
os.makedirs("results", exist_ok=True)
with open("results/educator_autogen.md", "w") as f:
    f.write(result)
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f"\u2705 Benchmark complete. Output saved to results/educator_autogen.md\n⏱️ Duration: {duration:.2f} seconds")
