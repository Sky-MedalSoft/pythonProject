from fastapi import APIRouter, Request

appPre3 = APIRouter()


@appPre3.post("/")
def items(request: Request):
    return {
        "url": request.url,
        "cookies": request.cookies,
        "客户端IP": request.client.host,
        "客户端浏览器": request.headers.get("User-Agent")
    }
