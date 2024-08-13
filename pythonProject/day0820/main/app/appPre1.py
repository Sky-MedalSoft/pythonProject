from fastapi import APIRouter, Form

appPre1 = APIRouter()
@appPre1.post("/regin")
def reg(username: str = Form(), password: str = Form()):
    print(f"username: {username}, password: {password}")
    return {
        "username": username,
        "password": password
    }