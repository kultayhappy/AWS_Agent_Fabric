"""
Prompt management.
"""

from __future__ import annotations


class PromptManager:
    """
    Manages prompts used by the AI Agent.
    """

    def get_system_prompt(self) -> str:
        """
        Returns the default system prompt.
        """

        return (
            "You are AWS Agent Fabric, a professional AI assistant. "
            "Your goal is to provide accurate, clear, production-ready "
            "answers. "
            "If you are unsure about something, say so honestly. "
            "Prefer AWS best practices, clean architecture, and Python code."
        )