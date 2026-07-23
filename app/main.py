"""
Application entry point.
"""

from app.config import Config


def main() -> None:
    """Application entry point."""

    print("=" * 50)
    print("AWS Agent Fabric")
    print("=" * 50)

    print(f"Region : {Config.AWS_REGION}")
    print(f"Model  : {Config.MODEL_ID}")

    print("\nProject initialized successfully.")


if __name__ == "__main__":
    main()