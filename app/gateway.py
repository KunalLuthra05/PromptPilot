from app.router import process_prompt


def handle_chat_completion(request):
    """
    Converts an OpenAI-compatible chat request
    into PromptPilot's internal format.
    Supports both text-only and vision requests.
    """

    if not request.messages:
        return {
            "error": {
                "message": "No messages provided."
            }
        }

    latest_message = request.messages[-1].content

    prompt = ""
    image_path = None

    # -------------------------
    # Text-only request
    # -------------------------
    if isinstance(latest_message, str):
        prompt = latest_message

    # -------------------------
    # Vision request
    # -------------------------
    else:
        for part in latest_message:

            if part.type == "text":
                prompt = part.text

            elif part.type == "image_url":
                image_path = part.image_url.url

    # Route through PromptPilot
    result = process_prompt(
        prompt=prompt,
        image_path=image_path
    )

    # Convert back to OpenAI format
    return {
        "id": "chatcmpl-promptpilot",
        "object": "chat.completion",
        "created": 0,
        "model": result["model"],
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": result["response"]
                },
                "finish_reason": "stop"
            }
        ]
    }