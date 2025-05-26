from frameworks.langchain_educator import run_langchain_educator_task
import os
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from frameworks.langchain_educator import run_langchain_educator_task
import time

start = time.time()
print(" Running LangChain Educator Benchmark")

# Run the LangChain education planning task
result = run_langchain_educator_task()
end = time.time()
duration = end - start
# Save the result
os.makedirs("results", exist_ok=True)
with open("results/educator_langchain.md", "w") as f:
    f.write(result)
    f.write(f"\n\n**Time to complete:** {duration:.2f} seconds\n")
print(f"\u2705 Benchmark complete. Output saved to results/educator_langchain.md\n Duration: {duration:.2f} seconds")
