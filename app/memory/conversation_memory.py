"""
Conversation memory.
"""

from __future__ import annotations

from app.models.chat_message import ChatMessage


class ConversationMemory:
    """
    Stores the current conversation history.

    This class is responsible only for storing
    and retrieving messages.

    It does NOT:

    - enforce conversation limits;
    - communicate with Amazon Bedrock;
    - contain business logic.
    """

    def __init__(self) -> None:

        self._messages: list[ChatMessage] = []

    # ---------------------------------------------------------
    # Add messages
    # ---------------------------------------------------------

    def add_user_message(self, text: str) -> None:
        """
        Add a user message.
        """

        self._messages.append(
            ChatMessage(
                role="user",
                text=text,
            )
        )

    def add_assistant_message(self, text: str) -> None:
        """
        Add an assistant message.
        """

        self._messages.append(
            ChatMessage(
                role="assistant",
                text=text,
            )
        )

    # ---------------------------------------------------------
    # Information
    # ---------------------------------------------------------

    def message_count(self) -> int:
        """
        Returns total number of stored messages.
        """

        return len(self._messages)

    def turn_count(self) -> int:
        """
        Returns the number of completed conversation turns.

        One turn consists of:

        User
        Assistant
        """

        assistant_messages = 0

        for message in self._messages:

            if message.is_assistant():
                assistant_messages += 1

        return assistant_messages

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    def get_messages(self) -> list[dict]:
        """
        Convert messages into Amazon Bedrock format.
        """

        return [
            message.to_bedrock()
            for message in self._messages
        ]

    # ---------------------------------------------------------
    # Maintenance
    # ---------------------------------------------------------

    def clear(self) -> None:
        """
        Remove all messages.
        """

        self._messages.clear()