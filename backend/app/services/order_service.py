from app.core.supabase import supabase

def create_order(
    user_id:str
):
    cart = (
        supabase
        .table("cart_items")
        .select(
            """
            quantity,
            products(
                id,
                price
            )
            """
        )
        .eq(
            "user_id",
            user_id
        )
        .execute()
    )
    items = cart.data
    if not items:
        raise Exception(
            "Carrito vacío"
        )
    total = sum(
        item["quantity"]
        *
        item["products"]["price"]
        for item in items
    )
    order = (
        supabase
        .table("orders")
        .insert(
            {
                "user_id":user_id,
                "total":total,
                "status":"completed"
            }
        )
        .execute()
    )
    order_id = order.data[0]["id"]
    for item in items:
        supabase.table(
            "order_items"
        ).insert(
            {
                "order_id":order_id,
                "product_id":
                item["products"]["id"],
                "quantity":
                item["quantity"],
                "price":
                item["products"]["price"]
            }
        ).execute()
    # Vaciar carrito después de completar compra
    supabase.table(
        "cart_items"
    ).delete().eq(
        "user_id",
        user_id
    ).execute()

    return order.data