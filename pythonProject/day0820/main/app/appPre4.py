from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

appPre4 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@appPre4.post("/region", response_model=UserOut)
def create_user(user: UserIn):
    # 存数据库
    return user
