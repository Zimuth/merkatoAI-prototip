from app.core.supabase import supabase

def create_store(
    user_id:str,
    store_name:str
):
    store = (
        supabase
        .table("stores")
        .insert(
            {
                "owner_id": user_id,
                "name": store_name
            }
        )
        .execute()
    )
    supabase\
        .table("users")\
        .update(
            {
                "role":"owner"
            }
        )\
        .eq(
            "id",
            user_id
        )\
        .execute()
    return store.data