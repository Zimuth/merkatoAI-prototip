from fastapi import APIRouter
from app.core.supabase import supabase

router = APIRouter(
    prefix="/marketplace",
    tags=["Marketplace"]
)

@router.get("/products")
def get_products():
    products = (
        supabase
        .table("products")
        .select("*")
        .execute()
    )
    return {
        "products":
        products.data
    }