def build_document_review_prompt(
    document_name: str,
    document_content: str,
    *,
    role: str = "software engineering assistant",
    goals: list[str] | None = None,
    required_output_format: str | None = None,
) -> str:
    """
    Build a structured prompt for reviewing and revising a document,
    with a strict separation between document output and reviewer notes.
    """

    goals_text = ""
    if goals:
        goals_text = "\n".join(f"- {goal}" for goal in goals)


    output_format_text = ""
    if required_output_format:
        output_format_text = f"""
    REQUIRED OUTPUT FORMAT (must follow exactly):
    {required_output_format}
    """


    return f"""
        You are a helpful {role}.

        Your task is to produce TWO sections:

        SECTION A — UPDATED {document_name.upper()}
        ...
        SECTION B — REVIEWER NOTES
        ...

        REVISION GOALS:
        {goals_text if goals_text else "Follow best practice and improve clarity without inventing content."}

        {output_format_text}

        ORIGINAL DOCUMENT:
        ----------------
        {document_content}
        ----------------
        """.strip()