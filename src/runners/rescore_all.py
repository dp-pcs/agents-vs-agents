import os
import sys
import subprocess
from glob import glob

def rescore_all():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    benchmark_root = os.path.abspath(os.path.join(os.getcwd(), 'results', 'benchmark2'))

    print(f"📂 Looking for benchmark results in: {benchmark_root}")

    benchmark_dirs = sorted(glob(os.path.join(benchmark_root, 'benchmark2_2025-*')))
    print(f"📄 Found {len(benchmark_dirs)} benchmark runs to rescore.")

    if not benchmark_dirs:
        print("❌ No benchmark2 result directories found.")
        return

    for dir_path in benchmark_dirs:
        print(f"\n🔄 Rescoring: {dir_path}")
        try:
            subprocess.run([
                sys.executable,
                "-m",
                "src.runners.benchmark2.b2_full_pipeline_run",
                dir_path,
                "--score-only"
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to rescore {dir_path}: {e}")

if __name__ == '__main__':
    rescore_all()