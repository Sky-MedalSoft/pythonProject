import os.path

from fastapi import APIRouter, File, UploadFile

appPre2 = APIRouter()


@appPre2.post("/file")
async def file(file: bytes = File()):
    print("file", file)
    return {
        "file": len(file)
    }


@appPre2.post("/file2")
async def file2(file: UploadFile = File(...)): \
        # 确保目录存在
    upload_dir = "img"
    os.makedirs(upload_dir, exist_ok=True)

    # 构建文件的完整路径
    file_path = os.path.join(upload_dir, file.filename)

    # 将文件内容写入到指定路径
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    print("file2", file)

    return {
        "file2": file.filename
    }