from app.core.supabase import supabase
import uuid

BUCKET = "product-images"

def upload_image(
    file
):
    filename = (
        str(uuid.uuid4())
        +
        ".jpg"
    )
    content = file.read()
    
    response = (
        supabase
        .storage
        .from_(BUCKET)
        .upload(
            filename,
            content
        )
    )
    url = (
        supabase
        .storage
        .from_(BUCKET)
        .get_public_url(
            filename
        )
    )
    return url