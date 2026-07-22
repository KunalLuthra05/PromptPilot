from fastapi import APIRouter

from app.gateway import handle_chat_completion
from app.models import ChatCompletionRequest

router = APIRouter(prefix="/v1", tags=["OpenAI API"])


# -------------------------
# Models Endpoint
# -------------------------

@router.get("/models")
async def list_models():

    return {
        "object": "list",
        "data": [
            {
                "id": "auto",
                "object": "model",
                "owned_by": "PromptPilot"
            },
            {
                "id": "qwen",
                "object": "model",
                "owned_by": "PromptPilot"
            },
            {
                "id": "deepseek",
                "object": "model",
                "owned_by": "PromptPilot"
            },
            {
                "id": "hermes",
                "object": "model",
                "owned_by": "PromptPilot"
            },
            {
                "id": "gemma",
                "object": "model",
                "owned_by": "PromptPilot"
            },
            {
                "id": "vision",
                "object": "model",
                "owned_by": "PromptPilot"
            }
        ]
    }


# -------------------------
# Chat Completions
# -------------------------

@router.post("/chat/completions")
async def chat_completions(request: ChatCompletionRequest):

    return handle_chat_completion(request)