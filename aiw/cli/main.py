import typer
from pathlib import Path

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