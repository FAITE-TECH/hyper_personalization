from fastapi import FastAPI
from app.routers import users, items, interactions, recommend
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hyper-Personalization API")

app.include_router(users.router)
app.include_router(items.router)
app.include_router(interactions.router)
app.include_router(recommend.router)
