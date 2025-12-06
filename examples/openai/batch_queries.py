"""
Example: Load questions from JSON and save responses to JSON file.
Demonstrates API parameters like temperature, max_tokens, and optional reasoning.
"""

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Prompt template
PROMPT_TEMPLATE = """Answer the following question concisely:

Question: {question}"""

def print_first_prompt(questions):
    """Print the first prompt to show how the template works."""
    if questions:
        first_prompt = PROMPT_TEMPLATE.format(question=questions[0])
        print("First Prompt Example:")
        print("-" * 50)
        print(first_prompt)
        print("-" * 50)
        print()

# Load questions from JSON file
with open("examples/openai/questions.json", "r") as f:
    data = json.load(f)

questions = data["questions"]
results = []

# Print the first prompt as an example
print_first_prompt(questions)

print("Processing questions ...")
print("-" * 50)

for i, question in enumerate(questions, 1):
    print(f"{i}. Question: {question}")
    
    # Create prompt using template
    prompt = PROMPT_TEMPLATE.format(question=question)
    
    # Call API with parameters
    response = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "user", "content": prompt}
        ],
        # === API PARAMETERS ===
        temperature=0.0,           # 0.0: Deterministic - always picks most likely token (best for accuracy) [0,2]
        max_completion_tokens=4096,            # Maximum length of response (the maximum is 4096 tokens for gpt-5.1)
        top_p=0.5,                # 0.5: Only considers top 50% likely tokens (more accurate, less random)
        # reasoning_effort="medium", # Optional: Enable extended reasoning. Values: "low", "medium", "high"
    )
    
    answer = response.choices[0].message.content
    print(f"   Answer: {answer}\n")
    
    # Store result with metadata
    results.append({
        "question": question,
        "answer": answer,
        "tokens_used": response.usage.completion_tokens
    })

# Save results to JSON file
output_data = {
    "results": results,
    "total_questions": len(results),
    "parameters_used": {
        "model": "gpt-5.1",
        "temperature": 0.0,
        "max_completion_tokens": 4096,
        "top_p": 0.5
    }
}

with open("examples/openai/responses.json", "w") as f:
    json.dump(output_data, f, indent=2)

print("-" * 50)
print(f"✓ Saved {len(results)} responses to responses.json")
