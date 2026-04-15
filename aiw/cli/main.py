from pathlib import Path
import difflib

import typer
from aiw.llm.ollama import generate

app = typer.Typer(help="AI Workbench – a personal CLI for thinking with AI")
run_app = typer.Typer(help="Run prompts and workflows")

app.add_typer(run_app, name="run")


@run_app.command("create")
def create(prompt: str):
    """
    Run a prompt or load it from a file using @file syntax.
    """

    original_input = prompt

    # Step 1: detect file reference
    if prompt.startswith("@"):
        file_path = Path(prompt[1:])

        if not file_path.exists():
            typer.echo(f"❌ File not found: {file_path}")
            raise typer.Exit(code=1)

        if not file_path.is_file():
            typer.echo(f"❌ Not a file: {file_path}")
            raise typer.Exit(code=1)

        prompt = file_path.read_text()
        typer.echo(f"📄 Using file contents as prompt: {file_path}")

    typer.echo("\n🧠 Running prompt:")
    typer.echo("-" * 40)
    typer.echo(prompt)
    typer.echo("-" * 40)
    typer.echo("\n(Mock response)")
    typer.echo("This is where an AI-generated response will go.")




@run_app.command("update-readme")
def update_readme(
    file: Path,
    model: str = typer.Option(
        "llama3",
        help="Ollama model to use (e.g. llama3, llama3:8b, mistral)",
    ),
    apply: bool = typer.Option(
        False,
        "--apply",
        help="Overwrite the README with the generated content",
    ),
):
    """
    Update a README.md file based on recent changes.
    """

    if not file.exists():
        typer.echo(f"❌ File not found: {file}")
        raise typer.Exit(code=1)

    if not file.is_file():
        typer.echo(f"❌ Not a file: {file}")
        raise typer.Exit(code=1)

    # 1️⃣ Read original content
    readme_content = file.read_text()

    prompt = f"""
    You are a helpful software engineering assistant.

    The following is the current README.md for a CLI tool.
    Please suggest an improved version that:
    - reflects recent development accurately
    - improves clarity and structure
    - keeps the tone pragmatic and technical
    - does NOT invent features that do not exist

    README CONTENT:
    ----------------
    {readme_content}
    ----------------
    """

    typer.echo("\n🤖 Generating updated README using Ollama...")
    typer.echo(f"🤖 Using Ollama model: {model}\n")

    # 2️⃣ Generate updated content
    updated_readme = generate(prompt, model=model)

    # 3️⃣ Compute diff
    original_lines = readme_content.splitlines(keepends=True)
    updated_lines = updated_readme.splitlines(keepends=True)

    diff = difflib.unified_diff(
        original_lines,
        updated_lines,
        fromfile=str(file),
        tofile=f"{file} (updated)",
    )
    diff_text = "".join(diff)

    # 4️⃣ Show diff preview
    typer.echo("\n🧾 Diff preview:")
    typer.echo("-" * 40)

    if diff_text.strip():
        typer.echo(diff_text)
    else:
        typer.echo("No changes detected.")

    typer.echo("-" * 40)

    # 5️⃣ Apply or not
    if apply:
        file.write_text(updated_readme)
        typer.echo("\n✅ README.md written to disk.")
    else:
        typer.echo("\nℹ️  Preview only. Run with --apply to overwrite the file.")
    
