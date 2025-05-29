import os
import re
from glob import glob

# Standard template sections
SECTIONS = [
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

# Robust section header regex: allow for numbering, agent names, parentheticals, dashes, colons, etc.
SECTION_HEADER_RE = re.compile(r"^#+\s*([IVX0-9.\- ]+)?\s*([A-Za-z &]+)(?:\s*\([^)]*\))?(?:\s*[-:\u2013\u2014].*)?$", re.IGNORECASE | re.MULTILINE)


def extract_sections(markdown):
    """Extract sections from markdown into a dict. Handles extra numbering, agent names, etc."""
    sections = {}
    current = None
    current_key = None
    lines = markdown.splitlines()
    for line in lines:
        m = SECTION_HEADER_RE.match(line.strip())
        if m:
            # Use only the main section name (group 2)
            current_key = m.group(2).strip().lower()
            current = []
            sections[current_key] = current
        elif current_key:
            current.append(line)
    # Convert lists to joined strings
    for k in sections:
        sections[k] = '\n'.join([l for l in sections[k] if l.strip()])
    return sections


def normalize_output(md_content):
    """Map markdown content to standard template, filling missing with _No output_. Uses fuzzy/partial matching."""
    found = extract_sections(md_content)
    normalized = {}
    for section in SECTIONS:
        section_key = section.lower()
        # Find the best match: exact, or substring, or fuzzy word match
        match = None
        for k in found:
            if section_key == k:
                match = k
                break
        if not match:
            for k in found:
                if section_key in k:
                    match = k
                    break
        if not match:
            # Fuzzy: match if all words in section are in the header
            section_words = set(section_key.split())
            for k in found:
                k_words = set(k.split())
                if section_words <= k_words or section_words.intersection(k_words) == section_words:
                    match = k
                    break
        normalized[section] = found.get(match, '_No output_')
    return normalized


def save_normalized(normalized, out_path):
    with open(out_path, 'w') as f:
        for section in SECTIONS:
            f.write(f"# {section}\n\n{normalized[section]}\n\n")


def main():
    # Find all result markdowns
    results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results'))
    md_files = glob(os.path.join(results_dir, '*_dynamic_orchestration.md'))
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
