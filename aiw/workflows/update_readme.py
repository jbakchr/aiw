from dataclasses import dataclass
from pathlib import Path
import difflib

from aiw.llm.ollama import generate


@dataclass
class UpdateReadmeResult:
    updated_readme: str
    diff_text: str


def run_update_readme(file: Path, model: str) -> UpdateReadmeResult:
    """
    Generate an updated README and a unified diff preview.
    """
    readme_content = file.read_text()

    prompt = f"""
You are a helpful software engineering assistant.

The following is the current README.md for a CLI tool.
Please suggest an improved version that:
- reflects recent development accurately
- improves clarity and structure
- keeps the tone pragmatic and technical
- does NOT invent features that do not exist

README CONTENT:
----------------
{readme_content}
----------------
"""

    updated_readme = generate(prompt, model=model)

    original_lines = readme_content.splitlines(keepends=True)
    updated_lines = updated_readme.splitlines(keepends=True)

    diff = difflib.unified_diff(
        original_lines,
        updated_lines,
        fromfile=str(file),
        tofile=f"{file} (updated)",
    )

    diff_text = "".join(diff)

    return UpdateReadmeResult(
        updated_readme=updated_readme,
        diff_text=diff_text,
    )