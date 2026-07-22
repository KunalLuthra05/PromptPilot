messages = []


def add_user_message(content):
    messages.append({
        "role": "user",
        "content": content
    })


def add_assistant_message(content):
    messages.append({
        "role": "assistant",
        "content": content
    })


def get_messages():
    return messages


def clear_chat():
    messages.clear()