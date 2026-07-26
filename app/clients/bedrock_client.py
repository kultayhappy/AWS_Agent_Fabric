"""
Amazon Bedrock client.
"""

from __future__ import annotations

from botocore.exceptions import BotoCoreError
from botocore.exceptions import ClientError

import boto3

from app.config import Config


class BedrockClient:
    """
    Amazon Bedrock Converse API client.
    """

    def __init__(self) -> None:

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=Config.AWS_REGION,
        )

    def generate(
        self,
        system_prompt: str,
        messages: list[dict],
    ) -> str:
        """
        Generate an assistant response.
        """

        try:

            response = self.client.converse(

                modelId=Config.MODEL_ID,

                system=[
                    {
                        "text": system_prompt
                    }
                ],

                messages=messages,

            )

            return (
                response["output"]
                ["message"]
                ["content"][0]
                ["text"]
            )

        except (ClientError, BotoCoreError) as error:

            raise RuntimeError(
                f"Bedrock request failed: {error}"
            ) from error