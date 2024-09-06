from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/', tags=['root'], summary="this is summary", description='this is description',
         response_description='this is response description')
def index():
    return 'Hello World'


if __name__ == '__main__':
    uvicorn.run("QuickStart:app", host='127.0.0.1', port=8080, log_level=True, reload=True)
