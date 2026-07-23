from typing import List, Union, Literal
from pydantic import BaseModel


# -------------------------
# Vision Content Types
# -------------------------

class ImageURL(BaseModel):
    url: str


class TextPart(BaseModel):
    type: Literal["text"]
    text: str


class ImagePart(BaseModel):
    type: Literal["image_url"]
    image_url: ImageURL


ContentPart = Union[TextPart, ImagePart]


# -------------------------
# Chat Message
# -------------------------

class Message(BaseModel):
    role: str
    content: Union[str, List[ContentPart]]


# -------------------------
# OpenAI Chat Request
# -------------------------

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    stream: bool = False