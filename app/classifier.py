import requests

from app.config import (
    ROUTER,
    QWEN,
    DEEPSEEK,
    HERMES,
    GEMMA
)

OLLAMA_URL = "http://localhost:11434/api/chat"


SYSTEM_PROMPT = f"""
You are an AI model router.

Choose ONLY ONE model from this list:

{QWEN}
{DEEPSEEK}
{HERMES}
{GEMMA}

Rules:

- Coding, debugging, programming → {QWEN}
- Logic, reasoning, mathematics → {DEEPSEEK}
- Emails, writing, resumes → {HERMES}
- General conversation → {GEMMA}

Reply ONLY with the model name.
No explanation.
"""


def classify(prompt: str) -> str:

    payload = {
        "model": ROUTER,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        response.raise_for_status()

        model = response.json()["message"]["content"].strip()

        valid_models = [
            QWEN,
            DEEPSEEK,
            HERMES,
            GEMMA
        ]

        if model in valid_models:
            return model

    except Exception:
        pass

    return GEMMA


if __name__ == "__main__":

    while True:

        prompt = input("\nPrompt: ")

        if prompt.lower() == "exit":
            break

        print(classify(prompt))