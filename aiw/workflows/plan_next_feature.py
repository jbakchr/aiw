from dataclasses import dataclass
from pathlib import Path

from aiw.llm.ollama import generate
from aiw.prompts.document_review import build_document_review_prompt



@dataclass
class PlanNextFeatureResult:
    plan_text: str



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
            "Propose exactly ONE concrete next change to implement (not a theme, not a refactor category)",
            "The change must be implementable in 1–2 focused coding sessions",
            "Do NOT propose persistence, storage, or new subsystems",
            "Base the recommendation strictly on what already exists in the codebase",
        ],
        required_output_format="""
            NEXT ACTION:
            <one-sentence summary>

            WHAT TO CHANGE:
            - <file or area>
            - <specific change>

            WHY THIS NEXT:
            <2–3 sentences>
            """.strip(),
    )

    raw_output = generate(prompt, model=model)

    required_sections = [
        "NEXT ACTION:",
        "WHAT TO CHANGE:",
        "WHY THIS NEXT:",
    ]

    for section in required_sections:
        if section not in raw_output:
            raise ValueError(f"LLM output missing required section: {section}")

    plan_text = raw_output.strip()
    reviewer_notes = ""

    
    return PlanNextFeatureResult(
        plan_text=plan_text
    )
