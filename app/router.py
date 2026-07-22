from app.classifier import classify
from app.ollama_client import ask_model
from app.logger import log_request

from app.config import (
    QWEN,
    DEEPSEEK,
    HERMES,
    GEMMA,
    VISION
)


def choose_model(prompt, image_path=None):
    """
    Decide which model should answer the prompt.
    """

    text = prompt.strip()

    # Manual Overrides
    if text.startswith("@qwen"):
        return QWEN

    if text.startswith("@deepseek"):
        return DEEPSEEK

    if text.startswith("@hermes"):
        return HERMES

    if text.startswith("@gemma"):
        return GEMMA

    if text.startswith("@vision"):
        return VISION

    # Image uploaded → Vision model
    if image_path:
        return VISION

    # Let the AI router choose
    return classify(prompt)


def process_prompt(prompt, image_path=None):

    model = choose_model(prompt, image_path)

    # Log the request
    log_request(
        prompt=prompt,
        model=model
    )

    answer = ask_model(
        model=model,
        prompt=prompt,
        image_path=image_path
    )

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