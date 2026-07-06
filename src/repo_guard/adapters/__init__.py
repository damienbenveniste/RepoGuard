"""Agent adapter template selection."""

from repo_guard.adapters.base import AgentAdapter, adapters_for
from repo_guard.adapters.claude import ClaudeAdapter
from repo_guard.adapters.codex import CodexAdapter
from repo_guard.adapters.cursor import CursorAdapter

__all__ = [
    "AgentAdapter",
    "ClaudeAdapter",
    "CodexAdapter",
    "CursorAdapter",
    "adapters_for",
]
