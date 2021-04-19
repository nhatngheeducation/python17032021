from fastapi import FastAPI
from models.KhachHang import khach_hang
import json
import os

app = FastAPI()

@app.get("/khachhang/{maso}", tags=["customers"])
def lay_khach_hang(maso):
    filename = f"./data/{maso}.json"
    if os.path.exists(filename):
        with open(filename, "r") as myfile:
            return {
                "success": True,
                "data": myfile.read()
            }
    return  {"success": False, "message":"Lỗi"}

@app.post("/khachhang", tags=["customers"])
def them_khach_hang(data : khach_hang):
    mydata = {
        "ma_so": data.ma_so,
        "ma_so": data.ma_so,
        "active": data.active,
        "doanh_so" : data.doanh_so,
        "email": data.email
    }
    jsonStr = json.dumps(mydata, indent=4)
    with open(f"./data/{data.ma_so}.json", "w") as file:
        file.write(jsonStr)

@app.get("/")
def read_root():
    return {"Hello": "Nhất Nghệ"}

@app.get("/hello")
def read_root(name):
    return {"message": f"Xin chào bạn {name}"}