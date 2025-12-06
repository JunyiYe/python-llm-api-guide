"""
Example: Multi-turn conversation (keeping chat history).
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Initialize message history
messages = []

# First turn
print("User: What are the main features of Python?")
messages.append({"role": "user", "content": "What are the main features of Python?"})

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=messages
)

assistant_reply = response.choices[0].message.content
print(f"Assistant: {assistant_reply}\n")
messages.append({"role": "assistant", "content": assistant_reply})

# Second turn - the model remembers the previous conversation
print("User: Which of those features makes it good for beginners?")
messages.append({"role": "user", "content": "Which of those features makes it good for beginners?"})

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=messages
)

assistant_reply = response.choices[0].message.content
print(f"Assistant: {assistant_reply}")
