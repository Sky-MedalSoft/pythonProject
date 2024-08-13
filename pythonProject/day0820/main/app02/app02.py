from datetime import date
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

app02 = APIRouter()


class User(BaseModel):
    name: str
    age: int
    birth: date
    friends: List[int]


@app02.post("/data")
async def get_data(user: User):
    return user
