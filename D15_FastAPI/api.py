# api.py
from typing import List
from fastapi import FastAPI, File, Form, UploadFile
import os
import shutil
from app.routers.user_router import router as user_router
from app.routers.ocr_router import router as ocr_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome NhatNghe FastAPI"}


app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(ocr_router, tags=["Ocr Tools"], prefix="/api/v1/ocr")

ROOT_DIRECTORY = os.getcwd()
@app.post("/upload-single", tags=["Upload file"])
def upload_single_file(image: UploadFile = File(...)):
    try:
        # Upload file vào thư mục data
        full_path = os.path.join(ROOT_DIRECTORY, "data",
                                 image.filename)
        with open(full_path, "wb") as myfile:
            shutil.copyfileobj(image.file, myfile)
        return {
            "message": f"File {image.filename} đã được upload."
        }
    except Exception as e:
        print(e)


@app.post("/upload-multiple", tags=["Upload file"])
def upload_multi_file(images: List[UploadFile] = File(...)):
    for image in images:
        full_path = os.path.join(ROOT_DIRECTORY, "data",
                                 image.filename)
        with open(full_path, "wb") as myfile:
            shutil.copyfileobj(image.file, myfile)
