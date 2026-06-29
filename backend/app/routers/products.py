from fastapi import APIRouter
from app.services.product_service import create_product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/")
def create(
    data:dict
):
    result = create_product(
        data["store_id"],
        data
    )
    return {
        "message":
        "Producto creado",
        "data":
        result
    }