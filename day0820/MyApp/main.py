from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index")
def index(request: Request):
    name = "start"
    age = 14    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "name": name,
            "age": age
        }
    )


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, log_level='debug', reload=True)
