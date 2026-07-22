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

Your ONLY job is to select the best model.

Reply with ONLY ONE of these exact model names:

{QWEN}
{DEEPSEEK}
{HERMES}
{GEMMA}

Routing Rules:

{QWEN}
- Programming
- Python
- C
- C++
- Java
- JavaScript
- HTML
- CSS
- SQL
- Coding
- Algorithms
- Data Structures
- Debugging
- Software Engineering
- APIs
- Git
- Linux
- Terminal
- Competitive Programming

{DEEPSEEK}
- Mathematics
- Logical reasoning
- Critical thinking
- Multi-step reasoning
- Planning
- Puzzles
- Brain teasers
- Analysis
- Proofs
- Decision making

{HERMES}
- Creative writing
- Stories
- Fiction
- Novels
- Essays
- Articles
- Blogs
- Poems
- Scripts
- Emails
- Resume writing
- Rewriting text
- Grammar correction
- Summaries
- Professional writing
- Roleplay

{GEMMA}
- Greetings
- Casual conversation
- General questions
- Small talk
- Everyday knowledge
- Simple explanations

Rules:

- Reply ONLY with the model name.
- No explanations.
- No punctuation.
- No markdown.
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

        print(f"[Router Output] {model}")

        model_lower = model.lower()

        if QWEN.lower() in model_lower:
            return QWEN

        if DEEPSEEK.lower() in model_lower:
            return DEEPSEEK

        if HERMES.lower() in model_lower:
            return HERMES

        if GEMMA.lower() in model_lower:
            return GEMMA

    except Exception as e:
        print(f"[Router Error] {e}")

    return GEMMA


if __name__ == "__main__":

    while True:

        prompt = input("\nPrompt: ")

        if prompt.lower() == "exit":
            break

        print(classify(prompt))