import os
from typing import List, Optional

import openai

class OpenAIChatAgent:
    """Simple agent for interacting with the OpenAI ChatCompletion API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("An OpenAI API key must be provided via argument or OPENAI_API_KEY env variable")
        openai.api_key = self.api_key
        self.model = model

    def chat(self, messages: List[dict], **kwargs) -> str:
        """Send messages to the chat completion endpoint and return the assistant's reply."""
        response = openai.ChatCompletion.create(model=self.model, messages=messages, **kwargs)
        return response["choices"][0]["message"]["content"]
