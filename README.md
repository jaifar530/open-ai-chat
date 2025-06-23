# OpenAI Chat Agent

This repository provides a simple command line interface to communicate with the OpenAI ChatCompletion API.

## Requirements

- Python 3.8+
- An OpenAI API key

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Set your API key in the `OPENAI_API_KEY` environment variable or pass `--api-key` on the command line.

Run the CLI with an initial prompt:

```bash
./chat_cli.py "Hello!"
```

You can include an optional system message and choose a specific model:

```bash
./chat_cli.py --system "You are a helpful assistant" --model gpt-3.5-turbo "What's the weather like?"
```

The assistant's reply will be printed to the terminal.
