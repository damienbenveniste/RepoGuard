"""Tests for the package module entry point."""

import pytest

import repo_guard.__main__ as agent_main


def test_main_delegates_to_typer_app(monkeypatch: pytest.MonkeyPatch) -> None:
    """`python -m repo_guard` uses the same Typer application."""
    called = False

    def fake_app() -> None:
        nonlocal called
        called = True

    monkeypatch.setattr(agent_main, "app", fake_app)

    agent_main.main()

    assert called
