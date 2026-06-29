from fastapi import APIRouter

from app.core.supabase import supabase


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users():

    response = (
        supabase
        .table("users")
        .select("*")
        .execute()
    )

    return response.data