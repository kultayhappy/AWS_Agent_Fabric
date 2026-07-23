"""
Chat service.
"""

from app.clients.bedrock_client import BedrockClient


class ChatService:
    """
    AI Chat service.
    """

    def __init__(self) -> None:

        self.bedrock = BedrockClient()

    def ask(self, question: str) -> str:

        return self.bedrock.generate(question)