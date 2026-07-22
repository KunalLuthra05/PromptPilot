from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
import uuid

from app.router import process_prompt
from app.openai_routes import router as openai_router

app = FastAPI(title="PromptPilot")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/chat")
async def chat(
    prompt: str = Form(...),
    image: UploadFile | None = File(None)
):

    image_path = None

    if image:

        extension = os.path.splitext(image.filename)[1]
        filename = f"{uuid.uuid4()}{extension}"

        image_path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    try:

        return process_prompt(
            prompt=prompt,
            image_path=image_path
        )

    finally:

        if image_path and os.path.exists(image_path):
            os.remove(image_path)


# Register OpenAI-compatible routes
app.include_router(openai_router)