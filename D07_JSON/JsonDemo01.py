import json

# Khai báo kiểu dict ==> json ==> lưu xuống file
hoc_vien = {
    "hoTen":"Nhất Nghệ",
    "dienThoai": 939123456,
    "gioiTinh": False, # True: nam, False: nữ
    "khoaHoc": [
        { "ten" : "Python", "ngayKg": "19/03/2021"},
        { "ten" : "WebAPI", "ngayKg": "22/03/2021"},
        { "ten" : "ASP.NET Core", "ngayKg": "29/03/2021"},
    ]
}
json_str = json.dumps(hoc_vien, indent = 4)
print(json_str)
with open("hocvien.json", "w") as file:
    file.write(json_str)