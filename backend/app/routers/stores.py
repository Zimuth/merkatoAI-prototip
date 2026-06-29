from fastapi import APIRouter
from app.services.store_service import create_store

router = APIRouter(
    prefix="/stores",
    tags=["Stores"]
)

@router.post("/")
def create(
    data:dict
):
    result = create_store(
        data["user_id"],
        data["store_name"]
    )
    return {
        "message":"Tienda creada",
        "data":result
    }