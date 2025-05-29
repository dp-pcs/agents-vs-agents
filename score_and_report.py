import os
import time
import requests
from glob import glob

# === CONFIG ===
NORMALIZED_DIR = os.path.join(os.path.dirname(__file__), 'results', 'normalized')
SUMMARY_REPORT = os.path.join(os.path.dirname(__file__), 'results', 'benchmark_report.md')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_MODEL = 'claude-3-sonnet-20240229'

SCORING_PROMPT = '''
You are an expert business plan evaluator. Given the following business plan, score it on a scale of 1-3 for each category:
- Completeness (Does it cover all sections and details expected in a professional business plan?)
- Rationale Quality (Does it clearly explain the reasoning for each decision and show logical connections?)
- Structure Quality (Is it well-organized, readable, and follows a standard business plan format?)

For each, provide a brief explanation for the score.

Respond in the following JSON format:
{
  "completeness": <score>,
  "completeness_explanation": "...",
  "rationale_quality": <score>,
  "rationale_explanation": "...",
  "structure_quality": <score>,
  "structure_explanation": "..."
}
'''

HEADERS = {
    'x-api-key': ANTHROPIC_API_KEY,
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
}

# === SCORING ===
def score_plan(plan_md):
    prompt = SCORING_PROMPT + '\n---\n' + plan_md[:6000]  # Truncate if too long
    data = {
        "model": ANTHROPIC_MODEL,
        "max_tokens": 512,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers=HEADERS,
        json=data,
        timeout=60
    )
    response.raise_for_status()
    content = response.json()["content"]
    if isinstance(content, list):
        text = "\n".join([block.get("text", "") for block in content])
    else:
        text = str(content)
    # Try to extract JSON
    import json
    try:
        j = json.loads(text[text.index('{'):text.rindex('}')+1])
        return j
    except Exception:
        return {"error": "Could not parse score JSON", "raw": text}

# === MAIN ===
def main():
    md_files = glob(os.path.join(NORMALIZED_DIR, 'normalized_*_dynamic_orchestration.md'))
    results = []
    for md_path in md_files:
        with open(md_path, 'r') as f:
            content = f.read()
        print(f"Scoring: {md_path}")
        try:
            score = score_plan(content)
        except Exception as e:
            score = {"error": str(e)}
        results.append({"file": os.path.basename(md_path), "score": score})
        time.sleep(1.5)  # Avoid rate limits
    # Write summary report
    with open(SUMMARY_REPORT, 'w') as f:
        f.write("# Multi-Agent Orchestration Benchmark Report\n\n")
        f.write("| Framework | Completeness | Rationale | Structure |\n")
        f.write("|-----------|--------------|-----------|-----------|\n")
        for res in results:
            fw = res["file"].replace('normalized_','').replace('_dynamic_orchestration.md','').capitalize()
            s = res["score"]
            if 'error' in s:
                f.write(f"| {fw} | ERROR | ERROR | ERROR |\n")
            else:
                f.write(f"| {fw} | {s.get('completeness','?')} | {s.get('rationale_quality','?')} | {s.get('structure_quality','?')} |\n")
        f.write("\n---\n\n## Detailed Explanations\n\n")
        for res in results:
            fw = res["file"].replace('normalized_','').replace('_dynamic_orchestration.md','').capitalize()
            s = res["score"]
            f.write(f"### {fw}\n")
            if 'error' in s:
                f.write(f"ERROR: {s['error']}\n\nRaw Output:\n{s.get('raw','')}\n\n")
            else:
                f.write(f"- **Completeness ({s['completeness']}):** {s['completeness_explanation']}\n")
                f.write(f"- **Rationale ({s['rationale_quality']}):** {s['rationale_explanation']}\n")
                f.write(f"- **Structure ({s['structure_quality']}):** {s['structure_explanation']}\n\n")
    print(f"\n✅ Benchmark report written to {SUMMARY_REPORT}")

if __name__ == '__main__':
    main()
