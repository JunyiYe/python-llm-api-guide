"""
Display questions and answers from responses.json file.
"""

import json

# Load responses from JSON file
with open("responses.json", "r") as f:
    data = json.load(f)

results = data["results"]
parameters = data["parameters_used"]

print("=" * 60)
print("Q&A Results")
print("=" * 60)
print()

# Display parameters used
print("Parameters Used:")
print("-" * 60)
for key, value in parameters.items():
    print(f"  {key}: {value}")
print()

# Display each question and answer
print("Questions & Answers:")
print("-" * 60)
for i, item in enumerate(results, 1):
    print(f"\n{i}. Question: {item['question']}")
    print(f"   Answer: {item['answer']}")
    if "tokens_used" in item:
        print(f"   Tokens: {item['tokens_used']}")

print()
print("=" * 60)
print(f"Total: {data['total_questions']} questions processed")
print("=" * 60)
