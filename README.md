# aiw — Personal AI Workbench (CLI-first)

**aiw** is a personal, CLI-first AI workbench for thinking, planning, and working alongside large language models in a structured and reusable way.

Unlike typical AI chat interfaces, `aiw` treats interactions with AI as **intentional, reproducible actions**:

- prompts are explicit,
- inputs are real files or text you already work with,
- outputs are something you can inspect, reuse, and improve over time.

The primary goal of `aiw` is to **reduce friction in everyday engineering and knowledge work**, starting with myself as the main user.

---

## Why aiw exists

Using AI through chat-based tools often leads to:

- lost context
- repeated prompts
- no memory of what worked well
- hard-to-reproduce results

`aiw` exists to flip that model.

Instead of chatting, you:

- **run prompts**,
- **against real artifacts** (README files, code, notes, roadmaps),
- **from the command line**,
- with the intent that good workflows can be reused and evolved.

Think of `aiw` as:

> “a small, boring, reliable interface between my thinking and AI”.

---

## Core principles

- **CLI-first**  
  `aiw` lives where development already happens: the terminal.

- **Personal-first**  
  It is built to solve my own real problems before trying to be general.

- **Incremental complexity**  
  Features are added only when they are felt as missing.

- **Reproducibility over novelty**  
  Being able to rerun and inspect past interactions matters more than new tricks.

- **AI as infrastructure, not magic**  
  Models are interchangeable; workflows and structure matter more.

---

## Current status

`aiw` is in **early development**.

Right now, it provides:

- a globally runnable CLI (`aiw`)
- a basic command structure
- the foundation for running prompt-based workflows

The system intentionally starts simple and grows only through real usage.

---

## Example (early, illustrative)

```bash
aiw run create "Explain dependency injection simply"
```

Future examples may include:

- updating a README based on recent changes
- deciding what feature to implement next
- explaining unfamiliar code files
- drafting technical text with consistent style

---

## Non-goals (for now)

- Fancy UI
- Chat-based interaction
- Multi-user features
- Agent frameworks
- Prompt marketplaces

If those ever happen, they will be **earned**.

---

## License

This project is currently for personal use and exploration.
Licensing will be decided later if and when that becomes relevant.

---
