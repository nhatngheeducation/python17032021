import csv
import json

filename = ".\data\DS_CapTinh_Quan_Huyen_Phuong_Xa_20_09_2020.csv"
# Thống kê tỉnh/TP có nhiêu phường xã
result = {}
# {
#     "Cà Mau":{
#         "XaPhuong": 7
#     }
# }
with open(filename, "r", encoding="utf-8") as myfile:
    csv_obj = csv.DictReader(myfile, delimiter=",")
    tmp = {}
    for item in csv_obj:
        tinh = item["\ufeffTỉnh Thành Phố"]
        if tinh in tmp:
            tmp[tinh] = tmp[tinh] + 1
        else:
            tmp[tinh] = 1

    print(tmp)
    json_str = json.dumps(tmp, indent=4, ensure_ascii=False)
    print(json_str)
    with open("ThongKeTinh.json", "w",
              encoding="utf-8") as jsonfile:
        jsonfile.write(json_str)


