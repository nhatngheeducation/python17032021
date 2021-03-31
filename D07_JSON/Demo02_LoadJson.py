import json

json_obj = None
with open("hocvien.json", "r") as file:
    json_str = file.read()
    print(json_str)
    json_obj = json.loads(json_str)
    print(json_obj)

print(type(json_obj))
if json_obj is not None:
    print(json_obj["hoTen"])
    print(json_obj["dienThoai"])
    print(f"Đăng ký {len(json_obj['khoaHoc'])} khóa học")
    for khoa_hoc in json_obj['khoaHoc']:
        print(f"{khoa_hoc['ten']} - KG {khoa_hoc['ngayKg']}")