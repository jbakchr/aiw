# aiw — Personal AI Workbench (CLI‑first)

**aiw** is a personal, CLI‑first AI workbench for thinking, planning, and working alongside large language models in a **structured, repeatable, and inspectable way**.

Instead of chatting with AI in a browser, `aiw` brings AI into the terminal and treats it like a **developer tool**:

- explicit inputs
- clear intent
- inspectable output
- safe application to real files

`aiw` is built first and foremost to be _useful_, not flashy.

---

## What aiw is (today)

Right now, `aiw` helps with two very concrete tasks:

1. **Maintaining and improving documentation** (e.g. `README.md`)
2. **Deciding what to work on next** based on an existing roadmap

Both are things developers do repeatedly — and often inefficiently.

---

## Key ideas

- **CLI‑first** — works where you already work
- **Local‑first AI** — powered by Ollama, no cloud dependency or cost
- **Preview before apply** — nothing is written unless you explicitly ask for it
- **Structured output** — AI suggestions and commentary are clearly separated
- **Incremental refinement** — features grow from real usage, not speculation

---

## Installation (development setup)

```bash
pipx install -e .
```

> `aiw` is currently intended primarily for personal use and development.

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) running locally
- At least one local model pulled, e.g.:

```bash
ollama pull llama3
```

or a faster alternative like:

```bash
ollama pull mistral
```

---

## Usage

### 1. Update a README.md safely

`aiw` can analyze and improve an existing `README.md`, showing you exactly what would change **before** applying anything.

#### Preview changes (default)

```bash
aiw run update-readme README.md
```

What you get:

- A **colorized unified diff**
- Clear visibility into what will be added, removed, or rewritten
- Optional reviewer notes with further improvement ideas

Nothing is written to disk.

#### Apply the changes

```bash
aiw run update-readme README.md --apply
```

What happens:

- The same diff preview is shown
- Only the **clean README content** is written
- Reviewer commentary is **never** included in the file

#### Choose a different model

```bash
aiw run update-readme README.md --model mistral
```

This is useful if you want faster responses for smaller tasks.

---

### 2. Decide what to implement next

Given an existing `ROADMAP.md`, `aiw` can suggest the **next small, high‑impact feature**, broken down into manageable steps.

```bash
aiw run plan-next-feature ROADMAP.md
```

What you get:

- A concrete recommendation for _what to build next_
- Step‑by‑step justification
- Optional reviewer notes with alternative ideas or caveats

This command is **non‑destructive** — it does not modify any files.

---

## Why aiw exists

Typical AI tools:

- lose context
- mix output with commentary
- encourage disposable interactions

`aiw` takes a different approach.

It treats AI as:

- **infrastructure**, not magic
- something you run intentionally
- something whose output you inspect, reuse, and apply carefully

Think of it as:

> _“a structured interface between my thinking and an LLM.”_

---

## Current scope (intentionally limited)

`aiw` does **not** aim to be:

- an AI chat client
- a general agent framework
- a replacement for existing tools

The focus is:

- a small number of workflows
- refined through real use
- that compound value over time

---

## Roadmap & direction

The roadmap lives in ROADMAP.md and evolves based on actual usage.

New features are only added when:

- existing workflows are clearly useful
- real friction is observed
- incremental improvements make sense

---

## Status

`aiw` is in active use and iteration.

It is expected to change, but changes are driven by **experience**, not novelty.

---

## License

Currently for personal use and experimentation.  
Licensing will be revisited if broader sharing becomes relevant.
