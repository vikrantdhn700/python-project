from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users
from app.routers import products
from app.routers import orders


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Mini E-Commerce API",
    description="FastAPI + Neon PostgreSQL E-Commerce Backend",
    version="1.0.0"
)


app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
