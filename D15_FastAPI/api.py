# api.py
from typing import List
import mysql.connector
from fastapi import FastAPI, File, Form, UploadFile
import os
import shutil
from app.models.NguoiDungModel import NguoiDung


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

@app.post("/upload-multiple", tags=["Upload file"])
def upload_multi_file(images: List[UploadFile] = File(...)):
    for image in images:
        full_path = os.path.join(ROOT_DIRECTORY, "data",
                                 image.filename)
        with open(full_path, "wb") as myfile:
            shutil.copyfileobj(image.file, myfile)


@app.get("/user", tags=["Users"])
def get_all_user():
    # import mysql.connector
    mydb = mysql.connector.connect(
        host="sql6.freemysqlhosting.net",
        user="sql6407749",
        password="dMuLKDMrDB",
        database="sql6407749"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nguoidung")
    myresult = mycursor.fetchall()
    users = []
    for nd in myresult:
        users.append(NguoiDung(
            HoTen = nd[3],
            Email = nd[4],
            Username = nd[1]
        ))

    return users