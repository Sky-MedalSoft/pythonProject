from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/app01/{id}")
# 默认传入类型为str，转化为int（使用类型声明  ）
def get_user(id: int):
    print(id)
    return {
        "user_id": id
    }
