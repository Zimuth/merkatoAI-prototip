from app.core.supabase import supabase

def add_to_cart(
    user_id:str,
    product_id:str,
    quantity:int
):
    existing = (
        supabase
        .table("cart_items")
        .select("*")
        .eq(
            "user_id",
            user_id
        )
        .eq(
            "product_id",
            product_id
        )
        .execute()
    )
    if existing.data:
        new_quantity = (
            existing.data[0]["quantity"]
            +
            quantity
        )
        updated = (
            supabase
            .table("cart_items")
            .update(
                {
                    "quantity":
                    new_quantity
                }
            )
            .eq(
                "id",
                existing.data[0]["id"]
            )
            .execute()
        )
        return updated.data
    item = (
        supabase
        .table("cart_items")
        .insert(
            {
                "user_id":user_id,
                "product_id":product_id,
                "quantity":quantity
            }
        )
        .execute()
    )
    return item.data

def get_cart(
    user_id:str
):
    cart = (
        supabase
        .table("cart_items")
        .select(
            """
            id,
            quantity,
            products(
                id,
                name,
                price,
                image_url
            )
            """
        )
        .eq(
            "user_id",
            user_id
        )
        .execute()
    )
    return cart.data