# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome NhatNghe FastAPI"}


@app.post("/upload-single", tags=["Upload file"])
def upload_single_file():
    pass