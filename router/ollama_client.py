import requests
from conversation import (
    add_user_message,
    add_assistant_message,
    get_messages
)

OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_model(model, prompt):

    # Add the user's message
    add_user_message(prompt)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": get_messages(),
            "stream": False
        }
    )

    response.raise_for_status()

    answer = response.json()["message"]["content"]

    # Save the assistant's reply
    add_assistant_message(answer)

    return answer