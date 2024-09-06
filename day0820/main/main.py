from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from app01.app01 import app01
from app02.app02 import app02
from online_edu_system.app import appPre1
from online_edu_system.app import appPre2
from online_edu_system.app import appPre3
from online_edu_system.app import appPre4

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(app01, tags=["app01"])
app.include_router(app02, tags=["app02"])
app.include_router(appPre1, tags=["appPre1"])
app.include_router(appPre2, tags=["文件上传"])
app.include_router(appPre3,tags=["Request"])
app.include_router(appPre4,tags=["region"])

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, log_level='debug', reload=True)
