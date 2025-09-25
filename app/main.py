from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, items, interactions, recommend
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hyper-Personalization API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(interactions.router)
app.include_router(recommend.router)
