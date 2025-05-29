import markdown2

with open("results/benchmark_summary.md", "r") as f:
    md = f.read()

html = markdown2.markdown(md)

with open("results/benchmark_summary.html", "w") as f:
    f.write(html)