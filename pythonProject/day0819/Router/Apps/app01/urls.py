from fastapi import APIRouter

cart = APIRouter()

@cart.get("/")
def index():
    return {"message": "Hello World"}