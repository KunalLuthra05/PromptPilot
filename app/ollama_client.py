import base64
import requests

from app.conversation import (
    add_user_message,
    add_assistant_message,
    get_messages
)

OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_model(model, prompt, image_path=None):
    """
    Send a prompt to an Ollama model.
    Supports both text and optional image input.
    """

    add_user_message(prompt)

    messages = get_messages()

    if image_path:

        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        messages[-1]["images"] = [image_data]

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": messages,
            "stream": False
        }
    )

    response.raise_for_status()

    answer = response.json()["message"]["content"]

    add_assistant_message(answer)

    return answer