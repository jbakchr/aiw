def build_document_review_prompt(
    document_name: str,
    document_content: str,
    *,
    role: str = "software engineering assistant",
    goals: list[str] | None = None,
) -> str:
    """
    Build a structured prompt for reviewing and revising a document,
    with a strict separation between document output and reviewer notes.
    """

    goals_text = ""
    if goals:
        goals_text = "\n".join(f"- {goal}" for goal in goals)

    return f"""
You are a helpful {role}.

Your task is to produce TWO sections:

SECTION A — UPDATED {document_name.upper()}
- This section must contain ONLY the full revised document content.
- Do NOT include commentary, feedback, or meta text.
- Do NOT explain what you changed.
- Output valid Markdown.

SECTION B — REVIEWER NOTES
- This section may contain suggestions, feedback, or follow-up ideas.
- This section will NOT be written to disk.

Use EXACT section headers:
=== UPDATED {document_name.upper()} ===
=== REVIEWER NOTES ===

REVISION GOALS:
{goals_text if goals_text else "Follow best practice and improve clarity without inventing content."}

ORIGINAL DOCUMENT:
----------------
{document_content}
----------------
""".strip()