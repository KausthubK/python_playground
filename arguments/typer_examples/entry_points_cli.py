from typing import Optional
import typer


example_app = typer.Typer()


@example_app.command()
def say_hello(name: Optional[str] = None):
    if name:
        typer.echo(f"Hello {name}")
    else:
        typer.echo("Hello World")


@example_app.command()
def say_goodbye(name: Optional[str] = None):
    if name:
        typer.echo(f"Goodbye {name}")
    else:
        typer.echo("Goodbye World")


if __name__ == "__main__":
    example_app()