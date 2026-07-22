from app.router import process_prompt


def handle_chat_completion(request):
    """
    Converts an OpenAI-compatible chat request
    into PromptPilot's internal format.
    """

    if not request.messages:
        return {
            "error": {
                "message": "No messages provided."
            }
        }

    # Get the latest user message
    prompt = request.messages[-1].content

    # Route through PromptPilot
    result = process_prompt(prompt)

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