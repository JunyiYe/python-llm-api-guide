# Python LLM API Guide

Simple, practical examples on how to use Large Language Model (LLM) APIs with Python.

## Quick Start

### 1. Install OpenAI Library

```bash
pip install openai python-dotenv
```

### 2. Set Up Your API Key

Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

**Option A: Using environment variable**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Option B: Using .env file**
```bash
cp .env.example .env
# Edit .env and add your API key
```

### 3. Run Examples

```bash
# Basic example
python examples/openai/basic_example.py

# Streaming example
python examples/openai/streaming_example.py
```

## Examples

### OpenAI GPT-5.1

This repository includes simple examples for:

- **Basic API calls** - Send a message and get a response
- **Batch queries** - Process multiple questions from JSON and save responses
- **Conversations** - Multi-turn conversation with chat history

See the [examples/openai](./examples/openai/) folder for code.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .env.example
└── examples/
    └── openai/
        ├── README.md
        ├── basic_example.py
        ├── batch_queries.py
        ├── conversation_example.py
        └── queries.json
```

## License

MIT
