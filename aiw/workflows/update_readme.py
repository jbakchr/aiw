from dataclasses import dataclass
from pathlib import Path
import difflib

from aiw.llm.ollama import generate


@dataclass
class UpdateReadmeResult:
    updated_readme: str
    diff_text: str
    reviewer_notes: str


def run_update_readme(file: Path, model: str) -> UpdateReadmeResult:
    """
    Generate an updated README and a unified diff preview,
    while separating reviewer notes from document content.
    """
    readme_content = file.read_text()

    prompt = f"""
You are a helpful software engineering assistant.

Your task is to produce TWO sections:

SECTION A — UPDATED README
- This section must contain ONLY the full revised README.md content.
- Do NOT include commentary, feedback, or meta text.
- Do NOT explain what you changed.
- Output valid Markdown.

SECTION B — REVIEWER NOTES
- This section may contain suggestions, feedback, or follow-up ideas.
- This section will NOT be written to disk.

Use EXACT section headers:
=== UPDATED README ===
=== REVIEWER NOTES ===

README CONTENT:
----------------
{readme_content}
----------------
"""

    raw_output = generate(prompt, model=model)

    if "=== UPDATED README ===" not in raw_output:
        raise ValueError("LLM output missing UPDATED README section")

    updated_part, _, notes_part = raw_output.partition("=== REVIEWER NOTES ===")

    updated_readme = (
        updated_part
        .replace("=== UPDATED README ===", "")
        .strip()
    )

    reviewer_notes = notes_part.strip()

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
        reviewer_notes=reviewer_notes,
    )