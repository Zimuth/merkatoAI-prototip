from fastapi import APIRouter
from app.services.order_service import create_order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/checkout")
def checkout(
    data:dict
):
    result = create_order(
        data["user_id"]
    )

    return {
        "message":
        "Compra realizada",
        "order":
        result
    }