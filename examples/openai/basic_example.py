"""
Basic example: How to call OpenAI API and get a response.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Send a message and get response
response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "user", "content": "What is Python? Explain in one sentence."}
    ]
)

# Print the response
print("Response:")
print(response.choices[0].message.content)
