from fastapi import FastAPI
from pydantic import BaseModel

from router import process_prompt

app = FastAPI(title="AI Router")


class Prompt(BaseModel):
    prompt: str


@app.post("/chat")
def chat(data: Prompt):

    return process_prompt(data.prompt)