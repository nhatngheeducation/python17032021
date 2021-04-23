# api.py
from fastapi import FastAPI, File, Form, UploadFile
import os
import shutil


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome NhatNghe FastAPI"}


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