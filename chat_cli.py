#!/usr/bin/env python3
"""Command line interface for the OpenAI chat agent."""
import argparse
import json

from open_ai_chat.agent import OpenAIChatAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Chat with OpenAI's API")
    parser.add_argument("prompt", help="Initial prompt to send to the assistant")
    parser.add_argument("--model", default="gpt-3.5-turbo", help="OpenAI model name")
    parser.add_argument("--api-key", dest="api_key", help="OpenAI API key. If omitted, OPENAI_API_KEY env variable is used")
    parser.add_argument("--system", dest="system_message", default=None, help="Optional system message to instruct the assistant")
    args = parser.parse_args()

    agent = OpenAIChatAgent(api_key=args.api_key, model=args.model)

    messages = []
    if args.system_message:
        messages.append({"role": "system", "content": args.system_message})
    messages.append({"role": "user", "content": args.prompt})

    try:
        reply = agent.chat(messages)
        print(reply)
    except Exception as exc:
        print(f"Error communicating with OpenAI API: {exc}")


if __name__ == "__main__":
    main()
