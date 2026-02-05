from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes import auth

from app.database import Base, engine
from app.routes import farmer, buyer, product

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AgroLink Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(farmer.router)
app.include_router(buyer.router)
app.include_router(product.router)
app.include_router(auth.router)

