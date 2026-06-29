from fastapi import APIRouter, UploadFile, File
from app.ai.vision import analyze_image
import shutil

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/analyze")
def analyze(
    file:UploadFile = File(...)
):
    path = (
        "temp_"
        +
        file.filename
    )
    with open(path,"wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )
    result = analyze_image(
        path
    )
    return {
        "message":
        "Imagen analizada",
        "prediction":
        result
    }