import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print("URL:", url)
print("KEY:", key[:20])

if not url or not key:
    raise Exception(
        "Faltan variables de Supabase"
    )

supabase = create_client(
    url,
    key
)