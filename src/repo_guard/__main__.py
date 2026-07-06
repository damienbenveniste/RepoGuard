"""Module entry point for `python -m repo_guard`."""

from repo_guard.cli import app


def main() -> None:
    """Run the Typer application."""
    app()


if __name__ == "__main__":
    main()
