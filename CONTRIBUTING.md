# Contributing

Thanks for considering a contribution to ScaffoldGuard.

## Start Here

- Open an issue before large behavior changes so the scope can be discussed.
- Keep pull requests focused on one fix, feature, or documentation improvement.
- Include tests for behavior changes.
- Update documentation when commands, generated output, templates, or workflows change.
- Do not include secrets, private data, local virtual environments, or generated runtime artifacts.

## Development Setup

```bash
git clone https://github.com/damienbenveniste/ScaffoldGuard.git
cd ScaffoldGuard
uv sync --all-groups
```

Run the main validation gate before opening a pull request:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy src tests
uv run pyright
uv run pytest tests --cov=scaffold_guard --cov-report=term-missing --cov-fail-under=95
uv run mkdocs build --strict
```

## Pull Requests

Pull requests must pass CI before merge. The `main` branch is protected, so
changes land through pull requests rather than direct pushes.

The maintainer may ask for changes, split a large pull request, or close changes
that do not fit the current project scope.

