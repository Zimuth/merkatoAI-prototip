from app.core.supabase import supabase

def register_user(
    email:str,
    password:str,
    full_name:str
):
    auth_response = (
        supabase.auth.sign_up(
            {
                "email":email,
                "password":password
            }
        )
    )
    user_id = auth_response.user.id
    profile = (
        supabase
        .table("users")
        .insert(
            {
                "auth_id":user_id,
                "email":email,
                "full_name":full_name,
                "role":"buyer"
            }
        )
        .execute()
    )
    return profile.data

def login_user(
    email:str,
    password:str
):
    response = (
        supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )
    )
    return {
        "access_token": response.session.access_token,
        "user_id": response.user.id
    }