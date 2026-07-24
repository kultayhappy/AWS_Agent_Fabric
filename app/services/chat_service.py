"""
Chat service.
"""

from app.clients.bedrock_client import BedrockClient
from app.prompts.prompt_manager import PromptManager

class ChatService:
    """
    AI Chat service.
    """

    def __init__(self) -> None:

        self.bedrock = BedrockClient()
        self.prompts = PromptManager()

    def ask(self, question: str) -> str:

        system_prompt = self.prompts.get_system_prompt()

        return self.bedrock.generate(
            system_prompt=system_prompt,
            user_prompt=question,
        )