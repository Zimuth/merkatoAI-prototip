from fastapi import APIRouter, HTTPException
from app.services.auth_service import (register_user,login_user)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(
    data:dict
):
    try:
        result = register_user(
            data["email"],
            data["password"],
            data["full_name"]
        )
        return {
            "message":
            "Usuario creado",
            "data":result
        }
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

@router.post("/login")
def login(
    data:dict
):
    try:
        result = login_user(
            data["email"],
            data["password"]
        )
        return {
            "message":
            "Login correcto",
            "data":result
        }
    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )