"""
Conversation limit exception.
"""


class ConversationLimitError(Exception):
    """
    Raised when the maximum conversation length
    has been reached.
    """

    def __init__(self, max_turns: int) -> None:
        self.max_turns = max_turns

        super().__init__(
            f"Conversation limit reached ({max_turns} turns)."
        )