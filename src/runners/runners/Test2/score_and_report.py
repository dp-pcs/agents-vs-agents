import os
import time
import json
import requests
from glob import glob
import re

# === CONFIG ===
RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')
NORMALIZED_DIR = os.path.join(RESULTS_DIR, 'normalized')
SUMMARY_REPORT = os.path.join(os.path.dirname(__file__), 'results', 'benchmark_report.md')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_MODEL = 'claude-3-sonnet-20240229'

SCORING_PROMPT = '''
You are an expert business plan evaluator. Given the following business plan, score it on a scale of 0-3 for each category:

- Completeness (Does it cover all sections and details expected in a professional business plan, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion, and a rationale at the top?)
  - 0: Missing most required sections
  - 1: Missing several key sections or most sections lack depth
  - 2: Contains most sections with adequate detail
  - 3: Comprehensive with all required sections and appropriate detail

- Rationale Quality (Does it clearly explain why certain agents were used and others were not? Does it mention the BaseballCoachAgent and explain why it was excluded? Does it explain the reasoning behind strategic decisions?)
  - 0: No rationale provided
  - 1: Minimal rationale with little explanation
  - 2: Adequate rationale with some explanation of decisions
  - 3: Excellent rationale with clear explanations for all key decisions

- Structure Quality (Is it well-organized, readable, and follows a standard business plan format with clear markdown sections in the required order?)
  - 0: Poorly structured, difficult to follow
  - 1: Basic structure but with organizational issues
  - 2: Good structure with clear sections
  - 3: Excellent structure with professional formatting and logical flow

For each, provide a brief explanation for the score.

Additional considerations:
- For Completeness: Check if there's a rationale section at the top and if it mentions which agents were used and not used
- For Structure Quality: Check for consistent headers, logical flow between sections, and appropriate formatting

Respond in the following JSON format:
{
  "completeness": <score>,
  "completeness_explanation": "...",
  "rationale_quality": <score>,
  "rationale_explanation": "...",
  "structure_quality": <score>,
  "structure_explanation": "...",
  "baseball_coach_handling": <0 if not mentioned, 1 if mentioned but not explained, 2 if mentioned as excluded with explanation>
}
'''

HEADERS = {
    'x-api-key': ANTHROPIC_API_KEY,
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
}

# === SCORING ===
def score_plan(plan_md):
    # Extract any mentions of BaseballCoachAgent before truncating
    baseball_mentions = re.findall(r'(?i)baseball\s*coach\s*agent', plan_md)
    baseball_context = "BaseballCoachAgent mentioned" if baseball_mentions else "BaseballCoachAgent not mentioned"
    
    # Check if BaseballCoachAgent is explicitly excluded
    baseball_excluded = bool(re.search(r'(?i)(?:not\s+us(?:ed|ing)|exclud(?:ed|ing)|irrelevant)[^.]*?baseball', plan_md))
    
    # Truncate content but ensure we keep important parts (rationale + beginning)
    prompt = SCORING_PROMPT + '\n---\nImportant context: ' + baseball_context
    
    # Try to extract and keep the rationale section
    rationale_match = re.search(r'(?:#+ *Rationale[^\n]*\n+|\*\*Rationale[^\n]*\n+|Rationale:)([^\n].*?)(?=\n#|\n\*\*|\Z)', plan_md, re.DOTALL)
    
    if rationale_match:
        rationale = rationale_match.group(1).strip()
        # Keep first 3000 chars of plan with rationale at beginning
        plan_content = f"RATIONALE SECTION:\n{rationale}\n\nREST OF DOCUMENT (truncated):\n{plan_md[:6000]}"
    else:
        # Just send first part of document
        plan_content = plan_md[:8000]
    
    prompt += '\n\n' + plan_content
    
    data = {
        "model": ANTHROPIC_MODEL,
        "max_tokens": 1024,  # Increased for more detailed explanations
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
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
        try:
            start_idx = text.find('{')
            end_idx = text.rfind('}') + 1
            if start_idx >= 0 and end_idx > start_idx:
                json_str = text[start_idx:end_idx]
                j = json.loads(json_str)
                
                # Add our own assessment of BaseballCoachAgent handling if not provided
                if "baseball_coach_handling" not in j:
                    if baseball_excluded:
                        j["baseball_coach_handling"] = 2  # Explicitly excluded with explanation
                    elif baseball_mentions:
                        j["baseball_coach_handling"] = 1  # Mentioned but not explained
                    else:
                        j["baseball_coach_handling"] = 0  # Not mentioned
                        
                return j
            else:
                return {"error": "Could not find JSON brackets", "raw": text}
                
        except Exception as e:
            return {"error": f"Could not parse score JSON: {str(e)}", "raw": text}
            
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

# === MAIN ===
def main():
    md_files = glob(os.path.join(NORMALIZED_DIR, 'normalized_*_dynamic_orchestration.md'))
    results = []
    
    for md_path in md_files:
        with open(md_path, 'r') as f:
            content = f.read()
            
        # Extract framework name
        framework = os.path.basename(md_path).replace('normalized_b2_', '').replace('_dynamic_orchestration.md', '')
            
        print(f"Scoring: {framework} ({md_path})")
        try:
            score = score_plan(content)
            score["framework"] = framework
        except Exception as e:
            score = {"error": str(e), "framework": framework}
            
        results.append({"file": os.path.basename(md_path), "score": score, "framework": framework})
        time.sleep(1.5)  # Avoid rate limits
    
    # Write summary report
    with open(SUMMARY_REPORT, 'w') as f:
        f.write("# Multi-Agent Orchestration Benchmark Report\n\n")
        
        # Write summary table with all metrics
        f.write("## Overall Scores\n\n")
        f.write("| Framework | Completeness | Rationale | Structure | BaseballCoach Handling |\n")
        f.write("|-----------|--------------|-----------|-----------|------------------------|\n")
        
        for res in results:
            framework = res["framework"].capitalize()
            s = res["score"]
            
            if 'error' in s:
                f.write(f"| {framework} | ERROR | ERROR | ERROR | ERROR |\n")
            else:
                baseball = s.get('baseball_coach_handling', '?')
                baseball_rating = {0: "Not mentioned", 1: "Mentioned", 2: "Properly excluded"}
                baseball_display = f"{baseball} ({baseball_rating.get(baseball, 'Unknown')})"
                
                f.write(f"| {framework} | {s.get('completeness','?')} | {s.get('rationale_quality','?')} | {s.get('structure_quality','?')} | {baseball_display} |\n")
        
        # Calculate the aggregate scores
        f.write("\n## Framework Rankings\n\n")
        valid_results = [r for r in results if 'error' not in r['score']]
        if valid_results:
            framework_scores = {}
            for res in valid_results:
                framework = res["framework"].capitalize()
                s = res["score"]
                if 'completeness' in s and 'rationale_quality' in s and 'structure_quality' in s:
                    total_score = int(s['completeness']) + int(s['rationale_quality']) + int(s['structure_quality']) 
                    framework_scores[framework] = total_score
            
            # Sort and display rankings
            rankings = sorted(framework_scores.items(), key=lambda x: x[1], reverse=True)
            f.write("| Rank | Framework | Total Score |\n")
            f.write("|------|-----------|-------------|\n")
            for i, (fw, score) in enumerate(rankings, 1):
                f.write(f"| {i} | {fw} | {score}/15 |\n")
        
        # Detailed explanations
        f.write("\n---\n\n## Detailed Evaluations\n\n")
        for res in results:
            framework = res["framework"].capitalize()
            s = res["score"]
            f.write(f"### {framework}\n\n")
            
            if 'error' in s:
                f.write(f"**ERROR:** {s['error']}\n\n")
                if 'raw' in s:
                    f.write(f"**Raw Output:**\n```\n{s['raw'][:500]}...\n```\n\n")
            else:
                f.write(f"#### Completeness: {s.get('completeness', '?')}/3\n{s.get('completeness_explanation', 'No explanation provided.')}\n\n")
                f.write(f"#### Rationale Quality: {s.get('rationale_quality', '?')}/3\n{s.get('rationale_explanation', 'No explanation provided.')}\n\n")
                f.write(f"#### Structure Quality: {s.get('structure_quality', '?')}/3\n{s.get('structure_explanation', 'No explanation provided.')}\n\n")
                
                baseball = s.get('baseball_coach_handling', '?')
                if baseball == 2:
                    baseball_text = "BaseballCoachAgent was properly excluded with explanation"
                elif baseball == 1:
                    baseball_text = "BaseballCoachAgent was mentioned but not properly explained"
                elif baseball == 0:
                    baseball_text = "BaseballCoachAgent was not mentioned at all"
                else:
                    baseball_text = "Unknown BaseballCoachAgent handling"
                
                f.write(f"#### BaseballCoachAgent Handling: {baseball_text}\n\n")
                
                # Total score
                if all(k in s for k in ['completeness', 'rationale_quality', 'structure_quality']):
                    total = int(s['completeness']) + int(s['rationale_quality']) + int(s['structure_quality'])
                    f.write(f"**Total Score: {total}/15**\n\n")
    
    print(f"\n✅ Benchmark report written to {SUMMARY_REPORT}")

if __name__ == '__main__':
    main()