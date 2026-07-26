"""
Internal chat message model.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """
    Represents one message inside the application.

    This model is independent of any LLM provider
    (Amazon Bedrock, OpenAI, Anthropic, etc.).
    """

    role: str
    text: str

    def is_user(self) -> bool:
        """
        Returns True if the message belongs to the user.
        """
        return self.role == "user"

    def is_assistant(self) -> bool:
        """
        Returns True if the message belongs to the assistant.
        """
        return self.role == "assistant"

    def to_bedrock(self) -> dict:
        """
        Convert the internal message into
        Amazon Bedrock Converse API format.
        """

        return {
            "role": self.role,
            "content": [
                {
                    "text": self.text
                }
            ],
        }