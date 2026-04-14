import typer

app = typer.Typer(help="AI Workbench – a personal CLI for thinking with AI")

@app.command()
def hello():
    """Sanity check command"""
    typer.echo("✅ AI Workbench is installed and working")
