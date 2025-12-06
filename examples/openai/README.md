# OpenAI Examples

Simple examples showing how to use OpenAI API with Python.

## Examples

### 1. `basic_example.py` - Basic API Call

Shows how to send a message to the API and get a response.

```bash
python examples/openai/basic_example.py
```

**Code:**
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "user", "content": "Your question here"}
    ]
)

print(response.choices[0].message.content)
```

### 2. `batch_queries.py` - Process Multiple Queries from JSON

Load multiple questions from a JSON file, send them to the API, and save all responses to a new JSON file.

```bash
python examples/openai/batch_queries.py
```

**Features:**
- Load questions from `questions.json`
- Use a prompt template to format questions
- Save all responses to `responses.json`
- Output file includes questions and answers

**questions.json format:**
```json
{
  "questions": [
    "What is Python?",
    "How do you create a list?",
    "Explain functions"
  ]
}
```

**responses.json output:****
```json
{
  "results": [
    {
      "question": "What is Python?",
      "answer": "Python is a high-level programming language..."
    }
  ],
  "total_questions": 1
}
```

### 3. `conversation_example.py` - Multi-turn Conversation

Keep chat history to have a back-and-forth conversation.

```bash
python examples/openai/conversation_example.py
```

**Key concept:** Keep a `messages` list and add to it after each response.

## Setup

1. **Install packages:**
   ```bash
   pip install openai python-dotenv
   ```

2. **Add your API key:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run an example:**
   ```bash
   python examples/openai/basic_example.py
   ```

## Get Your API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it to your `.env` file

That's it! You're ready to use the OpenAI API.
