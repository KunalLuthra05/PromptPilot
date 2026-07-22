from classifier import classify
from ollama_client import ask_model

from config import (
    MODEL_MAP,
    CODING_KEYWORDS,
    REASONING_KEYWORDS,
    WRITING_KEYWORDS,
    QWEN,
    DEEPSEEK,
    HERMES,
    GEMMA
)


def choose_model(prompt):

    text = prompt.strip()
    lower = text.lower()

    # Manual Override
    if text.startswith("@qwen"):
        return QWEN

    if text.startswith("@deepseek"):
        return DEEPSEEK

    if text.startswith("@hermes"):
        return HERMES

    if text.startswith("@gemma"):
        return GEMMA

    # Coding
    for word in CODING_KEYWORDS:
        if word in lower:
            return QWEN

    # Reasoning
    for word in REASONING_KEYWORDS:
        if word in lower:
            return DEEPSEEK

    # Writing
    for word in WRITING_KEYWORDS:
        if word in lower:
            return HERMES

    # AI Classifier
    category = classify(prompt)

    return MODEL_MAP.get(category, GEMMA)


def process_prompt(prompt):

    model = choose_model(prompt)

    answer = ask_model(model, prompt)

    return {
        "model": model,
        "response": answer
    }


if __name__ == "__main__":

    while True:

        prompt = input("\nYou: ")

        if prompt.lower() == "exit":
            break

        result = process_prompt(prompt)

        print(f"\nUsing: {result['model']}")
        print("\nAI:\n")
        print(result["response"])