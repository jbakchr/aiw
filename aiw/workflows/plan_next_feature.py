from dataclasses import dataclass
from pathlib import Path

from aiw.llm.ollama import generate
from aiw.prompts.document_review import build_document_review_prompt


@dataclass
class PlanNextFeatureResult:
    plan_text: str
    reviewer_notes: str


def run_plan_next_feature(file: Path, model: str) -> PlanNextFeatureResult:
    """
    Analyze a roadmap and propose the next small, high-impact feature
    in a step-by-step manner.
    """
    roadmap_content = file.read_text()

    prompt = build_document_review_prompt(
        document_name="NEXT FEATURE PLAN",
        document_content=roadmap_content,
        goals=[
            "Identify the single next most valuable feature to implement",
            "Prefer small, incremental steps over large refactors",
            "Base the recommendation strictly on the roadmap content",
            "Explain the reasoning briefly and clearly",
            "Avoid inventing long-term or speculative features",
        ],
    )

    raw_output = generate(prompt, model=model)

    if "=== UPDATED NEXT FEATURE PLAN ===" not in raw_output:
        raise ValueError("LLM output missing UPDATED NEXT FEATURE PLAN section")

    plan_part, _, notes_part = raw_output.partition("=== REVIEWER NOTES ===")

    plan_text = (
        plan_part
        .replace("=== UPDATED NEXT FEATURE PLAN ===", "")
        .strip()
    )

    reviewer_notes = notes_part.strip()

    return PlanNextFeatureResult(
        plan_text=plan_text,
        reviewer_notes=reviewer_notes,
    )