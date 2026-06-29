from fastapi import APIRouter
from app.services.product_service import create_product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/publish")
def publish_product(
    data:dict
):
    product = create_product(
        data["store_id"],
        data
    )
    return {
        "message":
        "Producto publicado correctamente",
        "product":
        product
    }