from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Nhất Nghệ"}

@app.get("/hello")
def read_root(name):
    return {"message": f"Xin chào bạn {name}"}