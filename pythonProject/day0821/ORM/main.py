from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_api
app = FastAPI()

register_tortoise(
    app=app,
    config=TORTOISE_ORM
)

app.include_router(student_api, prefix="/student", tags=["学生接口"])

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True, log_level='debug')
