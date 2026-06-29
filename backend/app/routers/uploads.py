from fastapi import APIRouter, UploadFile, File
from app.services.storage_service import upload_image

router = APIRouter(
    prefix="/upload",
    tags=["Storage"]
)

@router.post("/")
def upload(
    file:UploadFile = File(...)
):
    url = upload_image(
        file.file
    )
    return {
        "image_url":url
    }