# Quickstart

## Install

After PyPI publication, run the CLI with `uvx`:

```bash
uvx scaffold-guard version
```

For local release testing, build the wheel and run it directly:

```bash
uv build
uvx --from dist/scaffold_guard-0.1.0-py3-none-any.whl scaffold-guard version
```

## Create A Project

```bash
uvx scaffold-guard init my_project --agent all
cd my_project
uv sync --all-groups
uv run scaffold-guard check
uv run scaffold-guard validate --quick
```

Use one adapter when you only need one agent surface:

```bash
uvx scaffold-guard init codex_demo --agent codex
uvx scaffold-guard init claude_demo --agent claude
uvx scaffold-guard init cursor_demo --agent cursor
```

## Preview Or Refresh Files

```bash
scaffold-guard init demo --dry-run
scaffold-guard compile-rules --path demo --dry-run
scaffold-guard compile-rules --path demo --force
```

`compile-rules` refuses to overwrite manually edited instruction files unless
`--force` is supplied or the file has the generated marker.
