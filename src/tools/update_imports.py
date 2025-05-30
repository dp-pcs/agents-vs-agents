import os
import re
from pathlib import Path

# Define the rules for updating import statements
IMPORT_PATTERNS = [
    (re.compile(r'^(from|import)\s+frameworks(\b|\.)'), r'\1 src.frameworks'),
    (re.compile(r'^(from|import)\s+shared(\b|\.)'), r'\1 src.shared'),
]

# Recursively scan for .py files
def find_python_files(root_dir):
    for path in Path(root_dir).rglob('*.py'):
        yield path

# Update imports in a file
def update_imports_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    updated = False
    new_lines = []
    for line in lines:
        original_line = line
        for pattern, replacement in IMPORT_PATTERNS:
            # Only replace at the start of the line, preserve indentation
            match = pattern.match(line.lstrip())
            if match:
                indent = line[:len(line) - len(line.lstrip())]
                line = indent + pattern.sub(replacement, line.lstrip(), count=1)
                updated = True
        new_lines.append(line)

    if updated:
        # Backup original file
        backup_path = str(filepath) + '.bak'
        os.rename(filepath, backup_path)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated imports in {filepath} (backup at {backup_path})")

if __name__ == '__main__':
    repo_root = Path(__file__).parent.parent
    for py_file in find_python_files(repo_root):
        # Skip files in .venv, __pycache__, or hidden directories
        parts = py_file.parts
        if any(part.startswith('.') or part == '__pycache__' or part == 'venv' for part in parts):
            continue
        update_imports_in_file(py_file)
