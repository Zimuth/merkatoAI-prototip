from fastapi import APIRouter, UploadFile, File
from app.services.storage_service import upload_image
from app.ai.vision import analyze_image

router = APIRouter(
    prefix="/products-ai",
    tags=["Product AI"]
)

@router.post("/analyze")
def analyze_product(
    file:UploadFile = File(...)
):
    image_url = upload_image(
        file.file
    )
    result = analyze_image(
        file.file
    )
    return {
        "image_url":
        image_url,
        "suggestion":
        result
    }