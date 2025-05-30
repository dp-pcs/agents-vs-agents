import os

def load_prompt(prompt_path=None):
    """
    Load the evaluation prompt from the given file path.
    If no path is provided, load from the default location in evaluators/prompts/evaluation_prompt_template.txt.
    """
    if prompt_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        prompt_path = os.path.join(base_dir, "evaluators", "prompts", "evaluation_prompt_template.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()
