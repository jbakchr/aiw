# aiw — Development Roadmap

This roadmap exists to provide **direction, not obligation**.

It is intentionally lightweight and may change as real usage reveals what is actually valuable.

---

## Guiding star

> Build a CLI tool that makes it easier to think, decide, and build with AI,
> starting from real, everyday developer tasks.

---

## Phase 1 — Foundation ✅

**Status:** Completed

- [x] Repository created
- [x] Python package structure
- [x] Global CLI installation (`aiw`)
- [x] Typer-based command system
- [x] Basic help and command dispatch

Outcome:

> `aiw` runs anywhere on the system and provides a stable base to build on.

---

## Phase 2 — Run Concept ✅

**Status:** Completed

- [x] `aiw run` command namespace
- [x] `aiw run create` command
- [x] Basic prompt execution flow (mocked)
- [x] Clear CLI interaction model

Outcome:

> The core interaction pattern of the tool is established.

---

## Phase 3 — File Input (Next)

**Goal:**
Make `aiw` useful for real work by allowing direct interaction with files.

Planned:

- [ ] Support `@file` input (e.g. `@README.md`)
- [ ] Graceful error handling for missing/invalid files
- [ ] Clear display of inputs being processed

Outcome:

> `aiw` can operate on real artifacts already used in daily work.

---

## Phase 4 — First AI Integration

**Goal:**
Replace mock responses with a real LLM provider.

Planned:

- [ ] Minimal LLM abstraction
- [ ] Single provider (initially)
- [ ] Configuration via environment variables
- [ ] Keep interface boring and explicit

Outcome:

> `aiw` produces genuinely useful output while keeping architecture simple.

---

## Phase 5 — Named Workflows

**Goal:**
Turn recurring tasks into reusable workflows.

Planned ideas:

- `update-readme`
- `plan-next-feature`
- `explain-code`
- `refine-text`

Outcome:

> AI usage becomes intentional and repeatable.

---

## Phase 6 — Persistence (Optional)

**Goal:**
Give memory to the system _only if it proves useful_.

Possible additions:

- storing past runs
- inspecting outputs later
- comparing results over time

Outcome:

> `aiw` compounds value instead of producing disposable output.

---

## Phase 7 — Evaluation & Direction Check

At this point, reassess:

- Is `aiw` useful daily?
- Is the CLI the right interface?
- Should the tool remain personal or be shared?

Only then consider:

- polishing UX
- documentation for others
- distribution strategy

---

## Final note

This roadmap is not a promise.
It is a **compass**.

Actual usage always wins.

---
