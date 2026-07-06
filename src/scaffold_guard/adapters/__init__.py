"""Agent adapter template selection."""

from scaffold_guard.adapters.base import AgentAdapter, adapters_for
from scaffold_guard.adapters.claude import ClaudeAdapter
from scaffold_guard.adapters.codex import CodexAdapter
from scaffold_guard.adapters.cursor import CursorAdapter

__all__ = [
    "AgentAdapter",
    "ClaudeAdapter",
    "CodexAdapter",
    "CursorAdapter",
    "adapters_for",
]
