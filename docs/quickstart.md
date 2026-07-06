# Quickstart

## Run The CLI

Run ScaffoldGuard without installing it globally:

```bash
uvx scaffold-guard version
uvx scaffold-guard init my_project --agent all
```

For repeated use, install the CLI as a `uv` tool:

```bash
uv tool install scaffold-guard
scaffold-guard version
scaffold-guard init my_project --agent all
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

If you installed the tool with `uv tool install scaffold-guard`, use
`scaffold-guard init ...` instead of `uvx scaffold-guard init ...`.
Generated projects include `scaffold-guard` in the `dev` dependency group, so
`uv run scaffold-guard ...` works after `uv sync --all-groups`.

Use one adapter when you only need one agent surface:

```bash
uvx scaffold-guard init codex_demo --agent codex
uvx scaffold-guard init claude_demo --agent claude
uvx scaffold-guard init cursor_demo --agent cursor
```

## Preview Or Refresh Files

Preview a new project without writing files:

```bash
uvx scaffold-guard init demo --dry-run
```

Refresh managed instruction files from inside a generated project:

```bash
uv run scaffold-guard compile-rules --dry-run
uv run scaffold-guard compile-rules --force
```

`compile-rules` refuses to overwrite manually edited instruction files unless
`--force` is supplied or the file has the generated marker.
