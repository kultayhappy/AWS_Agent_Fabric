"""
Application configuration.
"""


class Config:
    """
    Global application configuration.
    """

    # ------------------------------------------------------------------
    # AWS
    # ------------------------------------------------------------------

    AWS_REGION = "eu-north-1"

    MODEL_ID = "amazon.nova-lite-v1:0"

    # ------------------------------------------------------------------
    # Conversation
    # ------------------------------------------------------------------

    # Maximum completed conversation turns.
    #
    # One turn consists of:
    #
    # User
    # Assistant
    #
    # Example:
    #
    # MAX_CONVERSATION_TURNS = 10
    #
    # means:
    #
    # User
    # Assistant
    #
    # repeated 10 times.
    #
    MAX_CONVERSATION_TURNS = 2