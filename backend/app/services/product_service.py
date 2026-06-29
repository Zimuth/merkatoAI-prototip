from app.core.supabase import supabase

def create_product(
    store_id:str,
    data:dict
):
    product = (
        supabase
        .table("products")
        .insert(
            {
                "store_id":store_id,
                "name":data["name"],
                "description":data["description"],
                "category":data["category"],
                "price":data["price"],
                "stock":data["stock"],
                "image_url":data["image_url"]
            }
        )
        .execute()
    )
    return product.data