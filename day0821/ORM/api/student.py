import json

from fastapi import APIRouter, Request
from models import *
from pydantic import BaseModel

from day0821.ORM.models import Student
from fastapi.templating import Jinja2Templates
student_api = APIRouter()

templates = Jinja2Templates(directory="templates")

@student_api.get('/')
async def get_student():
    students = await Student.all()
    for student in students:
        print(student.name)
    return {"message": "This is the student API"}

@student_api.get('/index.html')
async def get_index(request: Request):
    students = await Student.all()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "students": students
        }
    )


@student_api.post('/')
async def post_student(student_in):
    student_in = json.loads(student_in)
    print(student_in)

    await Student.create(name=student_in.name,)

    return {"操作": "增加一个学生"}


@student_api.put('/')
async def put_student():
    return {"message": "This is the student API"}


@student_api.delete('/')
async def delete_student():
    return {"message": "This is the student API"}


@student_api.get('/{student_id}')
async def get_student_by_id(student_id: int):
    return {"message": f"This is the student API for student with id = {student_id} "}
