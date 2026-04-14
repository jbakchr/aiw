import typer
from pathlib import Path

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
def update_readme(file: Path):
    """
    Update a README.md file based on recent changes (mocked for now).
    """

    if not file.exists():
        typer.echo(f"❌ File not found: {file}")
        raise typer.Exit(code=1)

    if not file.is_file():
        typer.echo(f"❌ Not a file: {file}")
        raise typer.Exit(code=1)

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
    updated_readme = generate(prompt)

    typer.echo("\n✅ Suggested README update:")
    typer.echo("-" * 40)
    typer.echo(updated_readme)
    typer.echo("-" * 40)
