from fastapi import FastAPI
from app.routers import users
from app.routers import auth
from app.routers import stores

# Crea el servidor FastAPI
app = FastAPI(
    title="MerkatoAI API",
    description="Backend del marketplace inteligente con IA",
    version="1.0.0"
)

app.include_router(
    users.router
)
app.include_router(
    auth.router
)
app.include_router(
    stores.router
)

#Significa que cuando alguien visite: localhost:8000/ ejecuta la función.
@app.get("/")
def root():
    return {
        "message": "API funcionando correctamente"
    }