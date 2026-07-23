"""
Application entry point.
"""

from app.services.chat_service import ChatService


def main() -> None:

    chat = ChatService()

    print("=" * 60)
    print("AWS Agent Fabric")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:

            print("\nGoodbye!")

            break

        try:

            answer = chat.ask(question)

            print(f"\nAI: {answer}")

        except Exception as error:

            print(f"\nError: {error}")


if __name__ == "__main__":
    main()