import os
import re
from glob import glob
import json

# Standard template sections
SECTIONS = [
    "Rationale",  # Important: Include rationale section explicitly 
    "Executive Summary",
    "Market Analysis",
    "Product Strategy",
    "Go-to-Market Plan",
    "Financial Projections",
    "Team & Roles",
    "Risks & Mitigation",
    "12-Week Rollout Timeline",
    "Conclusion"
]

# More robust section header regex to handle various formatting styles
SECTION_HEADER_RE = re.compile(r"^#+\s*(?:[IVX0-9.\- ]+)?\s*([A-Za-z &]+)(?:\s*$[^)]*$)?(?:\s*[-:\u2013\u2014].*)?\$", re.IGNORECASE | re.MULTILINE)

# Special regex for rationale section - often found at the beginning or under specific headers
RATIONALE_RE = re.compile(r'(?:^|\n)(?:#+ *(?:Rationale|Reasoning|Explanation)[^\n]*\n+|\*\*Rationale[^\n]*\n+|Rationale:)([^\n].*?)(?=\n#|\n\*\*|\Z)', re.DOTALL)


def extract_sections(markdown):
    """Extract sections from markdown into a dict with improved rationale detection."""
    # First try to extract the rationale section
    rationale_match = RATIONALE_RE.search(markdown)
    sections = {}
    if rationale_match:
        sections["rationale"] = rationale_match.group(1).strip()
    
    # Extract other sections
    current = None
    current_key = None
    lines = markdown.splitlines()
    for line in lines:
        m = SECTION_HEADER_RE.match(line.strip())
        if m:
            # Use only the main section name
            section_name = m.group(1).strip().lower()
            # Handle special case for rationale if in a header
            if "rationale" in section_name:
                current_key = "rationale"
            else:
                current_key = section_name
            current = []
            sections[current_key] = current
        elif current_key:
            current.append(line)
    
    # Convert lists to joined strings
    for k in sections:
        if isinstance(sections[k], list):
            sections[k] = '\n'.join([l for l in sections[k] if l.strip()])
    
    # Check for BaseballCoachAgent mentions - important for evaluation
    baseball_mentions = []
    baseball_patterns = [
        r'(?i)baseball\s*coach\s*agent',
        r'(?i)\b(?:not\s+us(?:ed|ing)|exclud(?:ed|ing)|irrelevant)[^.]*?baseball'
    ]
    
    for pattern in baseball_patterns:
        matches = re.finditer(pattern, markdown)
        for match in matches:
            # Get a bit of context around the mention
            start = max(0, match.start() - 100)
            end = min(len(markdown), match.end() + 100)
            context = markdown[start:end]
            baseball_mentions.append({
                "text": match.group(0),
                "context": context,
                "position": match.start()
            })
    
    # Store baseball mentions if found
    if baseball_mentions:
        sections["baseball_coach_handling"] = json.dumps(baseball_mentions)
    
    return sections


def normalize_output(md_content):
    """Map markdown content to standard template with improved section matching."""
    found = extract_sections(md_content)
    normalized = {}
    
    # Extract metadata like duration and agent turns
    metadata = {}
    duration_match = re.search(r'\*\*Time to complete:\*\*\s*([\d.]+)\s*seconds', md_content)
    if duration_match:
        metadata["duration"] = duration_match.group(1)
    
    agent_turns_match = re.search(r'\*\*Agent turns:\*\*\s*(\d+)', md_content)
    if agent_turns_match:
        metadata["agent_turns"] = agent_turns_match.group(1)
    
    if metadata:
        normalized["metadata"] = json.dumps(metadata)
    
    # Special handling for baseball coach mentions
    if "baseball_coach_handling" in found:
        normalized["baseball_coach_handling"] = found["baseball_coach_handling"]
    
    for section in SECTIONS:
        section_key = section.lower()
        # Try direct match first
        if section_key in found:
            normalized[section] = found[section_key]
            continue
            
        # Try fuzzy matching with different techniques
        match = None
        
        # 1. Check for substring
        for k in found:
            if section_key in k or k in section_key:
                match = k
                break
                
        # 2. Check for word overlap
        if not match:
            section_words = set(section_key.split())
            best_match = None
            best_score = 0
            for k in found:
                k_words = set(k.split())
                overlap = len(section_words.intersection(k_words))
                if overlap > best_score:
                    best_score = overlap
                    best_match = k
            if best_score > 0:
                match = best_match
        
        normalized[section] = found.get(match, '_No output_')
    
    return normalized


def save_normalized(normalized, out_path):
    with open(out_path, 'w') as f:
        # First write any metadata
        if "metadata" in normalized:
            metadata = json.loads(normalized["metadata"])
            f.write("# Metadata\n\n")
            for k, v in metadata.items():
                f.write(f"- **{k.capitalize()}**: {v}\n")
            f.write("\n\n")
        
        # Write baseball coach handling if available
        if "baseball_coach_handling" in normalized:
            f.write("# BaseballCoachAgent Handling\n\n")
            mentions = json.loads(normalized["baseball_coach_handling"])
            for mention in mentions:
                f.write(f"- **{mention['text']}**\n")
                f.write(f"  Context: \"...{mention['context']}...\"\n\n")
        
        # Write standard sections
        for section in SECTIONS:
            f.write(f"# {section}\n\n{normalized[section]}\n\n")


def main():
    results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results'))
    md_files = glob(os.path.join(results_dir, 'b2_*_dynamic_orchestration.md'))
    out_dir = os.path.join(results_dir, 'normalized')
    os.makedirs(out_dir, exist_ok=True)
    
    for md_path in md_files:
        with open(md_path, 'r') as f:
            content = f.read()
        normalized = normalize_output(content)
        base = os.path.basename(md_path)
        out_path = os.path.join(out_dir, f'normalized_{base}')
        save_normalized(normalized, out_path)
        print(f"✅ Normalized: {md_path} -> {out_path}")

if __name__ == '__main__':
    main()