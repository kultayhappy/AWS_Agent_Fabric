"""
Application entry point.
"""

from __future__ import annotations

from app.config import Config
from app.exceptions.conversation_limit_error import ConversationLimitError
from app.services.chat_service import ChatService


def print_header() -> None:
    """
    Print application header.
    """

    print("=" * 50)
    print("AWS Agent Fabric")
    print("=" * 50)
    print(f"Region : {Config.AWS_REGION}")
    print(f"Model  : {Config.MODEL_ID}")
    print()


def print_help() -> None:
    """
    Print available commands.
    """

    print("Commands:")
    print("  /clear - Clear conversation history")
    print("  /exit  - Exit application")
    print()


def print_conversation_limit(max_turns: int) -> None:
    """
    Print conversation limit message.
    """

    print()
    print("=" * 50)
    print("Conversation limit reached.")
    print()
    print(f"Current limit : {max_turns} turns")
    print()
    print("To continue:")
    print("1. Open app/config.py")
    print("2. Increase MAX_CONVERSATION_TURNS")
    print("3. Restart application")
    print("=" * 50)
    print()


def main() -> None:
    """
    Application entry point.
    """

    chat = ChatService()

    print_header()
    print_help()

    while True:

        try:

            question = input("You: ").strip()

            if not question:
                continue

            if question.lower() == "/exit":
                print("\nGoodbye!")
                break

            if question.lower() == "/clear":
                chat.clear_memory()
                print("Conversation history cleared.\n")
                continue

            answer = chat.ask(question)

            print()
            print(f"AI: {answer}")
            print()

        except ConversationLimitError as error:

            print_conversation_limit(error.max_turns)
            break

        except KeyboardInterrupt:

            print("\n\nInterrupted by user.")
            break

        except Exception as error:

            print()
            print(f"Error: {error}")
            print()


if __name__ == "__main__":
    main()