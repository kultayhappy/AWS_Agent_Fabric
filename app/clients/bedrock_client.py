"""
Amazon Bedrock client.
"""

from __future__ import annotations

import json

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from app.config import Config


class BedrockClient:
    """
    Wrapper around Amazon Bedrock Runtime.
    """

    def __init__(self) -> None:

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=Config.AWS_REGION,
        )

    def generate(
    self,
    system_prompt: str,
    user_prompt: str,
    ) -> str:
        """
        Send a request to Amazon Bedrock and return the model response.
        """

        try:
            response = self.client.converse(
                modelId=Config.MODEL_ID,
                system=[
                    {
                        "text": system_prompt
                    }
                ],
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": user_prompt
                            }
                        ],
                    }
                ],
            )

            return response["output"]["message"]["content"][0]["text"]

        except (ClientError, BotoCoreError) as error:

            raise RuntimeError(
            f"Bedrock request failed: {error}"
        ) from error
        """
        Send prompt to Amazon Bedrock and return model response.
        """

        request = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        try:

            response = self.client.converse(
                modelId=Config.MODEL_ID,
                messages=request["messages"],
            )

            return response["output"]["message"]["content"][0]["text"]

        except (ClientError, BotoCoreError) as error:
            raise RuntimeError(
                f"Bedrock request failed: {error}"
            ) from error