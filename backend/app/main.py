from fastapi import FastAPI
from app.routers import users
from app.routers import auth
from app.routers import stores
from app.routers import products
from app.routers import ai
from app.routers import uploads
from app.routers import products_ai
from app.routers import products_publish
from app.routers import marketplace
from app.routers import cart
from app.routers import orders

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
app.include_router(
    products.router
)
app.include_router(
    ai.router
)
app.include_router(
    uploads.router
)
app.include_router(
    products_ai.router
)
app.include_router(
    products_publish.router
)
app.include_router(
    marketplace.router
)
app.include_router(
    cart.router
)
app.include_router(
    orders.router
)

#Significa que cuando alguien visite: localhost:8000/ ejecuta la función.
@app.get("/")
def root():
    return {
        "message": "API funcionando correctamente"
    }