from fastapi import APIRouter
from app.services.cart_service import add_to_cart
from app.services.cart_service import get_cart

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post("/add")
def add(
    data:dict
):
    result = add_to_cart(
        data["user_id"],
        data["product_id"],
        data["quantity"]
    )
    return {
        "message":
        "Producto agregado al carrito",
        "cart":
        result
    }

@router.get("/{user_id}")
def view_cart(
    user_id:str
):
    result = get_cart(
        user_id
    )
    return {
        "cart":result
    }