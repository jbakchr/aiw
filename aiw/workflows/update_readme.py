from dataclasses import dataclass
from pathlib import Path
import difflib

from aiw.llm.ollama import generate
from aiw.prompts.document_review import build_document_review_prompt


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

    prompt = build_document_review_prompt(
        document_name="README.md",
        document_content=readme_content,
        goals=[
            "Reflect recent development accurately",
            "Improve clarity and structure",
            "Keep a pragmatic, technical tone",
            "Do not invent features that do not exist",
            ],
    )


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