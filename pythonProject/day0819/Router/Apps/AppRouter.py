from fastapi import FastAPI
import uvicorn
from app01.urls import cart
from app02.urls import shop

app = FastAPI()

app.include_router(cart, prefix="/cart", tags=["Cart"])
app.include_router(shop, prefix="/shop", tags=["Shop"])

if __name__ == '__main__':
    uvicorn.run("AppRouter:app", host='127.0.0.1', port=8002, log_level='debug', reload=True)