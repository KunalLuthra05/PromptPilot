import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are an AI classifier.

Your ONLY job is to classify the user's request.

Possible outputs are ONLY:

CODING
REASONING
WRITING
GENERAL
VISION

Rules:
- Reply with ONLY one word.
- Do NOT explain.
- Do NOT answer the user's question.
- Do NOT use punctuation.
"""


def classify(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "gemma3:4b",
            "prompt": SYSTEM_PROMPT + "\n\nUser: " + prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip().upper()


if __name__ == "__main__":

    while True:

        prompt = input("\nYou: ")

        if prompt.lower() == "exit":
            break

        result = classify(prompt)

        print("\nClassification:", result)