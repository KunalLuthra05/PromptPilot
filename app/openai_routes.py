from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.router import process_prompt

router = APIRouter(prefix="/v1", tags=["OpenAI API"])


# -------------------------
# Models Endpoint
# -------------------------

@router.get("/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {"id": "auto", "object": "model", "owned_by": "PromptPilot"},
            {"id": "qwen", "object": "model", "owned_by": "PromptPilot"},
            {"id": "deepseek", "object": "model", "owned_by": "PromptPilot"},
            {"id": "hermes", "object": "model", "owned_by": "PromptPilot"},
            {"id": "gemma", "object": "model", "owned_by": "PromptPilot"},
            {"id": "vision", "object": "model", "owned_by": "PromptPilot"},
        ],
    }


# -------------------------
# Request Models
# -------------------------

class Message(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    stream: bool = False


# -------------------------
# Chat Completions
# -------------------------

@router.post("/chat/completions")
async def chat_completions(request: ChatCompletionRequest):

    if not request.messages:
        return {
            "error": {
                "message": "No messages provided."
            }
        }

    user_prompt = request.messages[-1].content

    result = process_prompt(user_prompt)

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