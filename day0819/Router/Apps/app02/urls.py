from fastapi import APIRouter

shop = APIRouter()

@shop.get('/')
def index():
    return {'message': 'Hello World'}
