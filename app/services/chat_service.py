"""
Chat service.
"""

from __future__ import annotations

from app.clients.bedrock_client import BedrockClient
from app.config import Config
from app.exceptions.conversation_limit_error import ConversationLimitError
from app.memory.conversation_memory import ConversationMemory
from app.prompts.prompt_manager import PromptManager


class ChatService:
    """
    AI chat service.
    """

    def __init__(self) -> None:

        self._bedrock = BedrockClient()
        self._prompts = PromptManager()
        self._memory = ConversationMemory()

    def ask(self, question: str) -> str:
        """
        Process one user request.
        """

        # -------------------------------------------------
        # Проверяем лимит ДО начала нового хода диалога.
        # Если количество завершённых ходов уже достигло
        # установленного значения, новый запрос запрещается.
        # -------------------------------------------------

        if self._memory.turn_count() >= Config.MAX_CONVERSATION_TURNS:
            raise ConversationLimitError(
                Config.MAX_CONVERSATION_TURNS
            )

        # -------------------------------------------------
        # Сохраняем сообщение пользователя
        # -------------------------------------------------

        self._memory.add_user_message(question)

        # -------------------------------------------------
        # Получаем системный промпт
        # -------------------------------------------------

        system_prompt = self._prompts.get_system_prompt()

        # -------------------------------------------------
        # Отправляем историю разговора
        # -------------------------------------------------

        answer = self._bedrock.generate(
            system_prompt=system_prompt,
            messages=self._memory.get_messages(),
        )

        # -------------------------------------------------
        # Сохраняем ответ модели
        # -------------------------------------------------

        self._memory.add_assistant_message(answer)

        return answer

    def clear_memory(self) -> None:
        """
        Clear conversation history.
        """

        self._memory.clear()