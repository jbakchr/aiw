# aiw — Development Roadmap

This roadmap exists to provide **direction, not obligation**.

It evolves based on real usage of `aiw`, not on speculative feature planning.
Completed phases remain documented to preserve context and learning.

---

## Guiding Star

Build a CLI-first tool that makes it easier to think, decide, and build with AI,
starting from real, everyday developer tasks.

The measure of success is not feature count, but whether `aiw` becomes a tool
I reach for instinctively during development work.

---

## Phase 1 — Foundation ✅

**Status:** Completed

- Repository created
- Python package structure
- Global CLI installation (`aiw`)
- Typer-based command system
- Basic help and command dispatch

**Outcome:**  
`aiw` runs anywhere on the system and provides a stable base to build on.

---

## Phase 2 — Run Concept ✅

**Status:** Completed

- `aiw run` command namespace
- `aiw run create` command
- Clear CLI interaction model
- Early prompt execution flow

**Outcome:**  
The core interaction pattern of the tool is established.

---

## Phase 3 — File Input & Real Artifacts ✅

**Status:** Completed

- Support for `@file` input (e.g. `@README.md`)
- Graceful error handling for missing or invalid files
- Clear display of inputs being processed

**Outcome:**  
`aiw` operates directly on real files already used in daily work.

---

## Phase 4 — AI Integration (Local‑First) ✅

**Status:** Completed

- Real LLM integration via Ollama
- Local-first, cost-free AI usage
- Model selection via `--model`
- Simple and explicit interaction surface

**Outcome:**  
`aiw` produces genuinely useful output without cloud dependency or complexity.

---

## Phase 5 — Named Workflows ✅

**Status:** In active use

Implemented workflows:

- `update-readme`
  - Safe diff preview
  - Optional `--apply`
  - Colorized unified diff
  - Structured output with reviewer notes
- `plan-next-feature`
  - Roadmap-based decision support
  - Step-by-step, incremental recommendations

**Outcome:**  
AI usage in `aiw` is intentional, repeatable, and aligned with real tasks.

---

## Phase 6 — Workflow Refinement & Leverage (Current Focus)

**Goals:**

- Improve clarity and trust in existing workflows
- Reduce friction in repeated use
- Extract shared patterns as they emerge naturally

Possible directions:

- Prompt refinement based on real output quality
- Optional persistence of plans or decisions
- Small UX improvements driven by daily usage

**Non-goal:**  
Adding new workflows without first maximizing the usefulness of existing ones.

---

## Phase 7 — Persistence (Optional, Exploratory)

**Goal:**  
Give memory to the system _only if it proves valuable in practice_.

Ideas to revisit if needed:

- Storing past runs
- Inspecting and comparing outputs over time
- Light history for planning decisions

---

## Phase 8 — Evaluation & Direction Check

At this point, explicitly reassess:

- Is `aiw` genuinely useful on a weekly or daily basis?
- Does the CLI remain the right interface?
- Should the tool stay personal, or be shareable?

Only then consider:

- broader documentation
- polishing UX for others
- distribution strategy

---

## Final Note

This roadmap is not a commitment.
It is a **compass**.

Actual usage always wins.
