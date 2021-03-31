# Cài thư viện request: pip install requests
import requests
import json

data = []
# Lấy thông tin tỉnh thành từ api
# https://thongtindoanhnghiep.co/api/city
URL_EP = "https://thongtindoanhnghiep.co/api/"
def get_data_from_api(url):
    my_request = requests.get(url)
    if my_request.status_code == 200:
        return my_request.json()
    else:
        return None

cities = get_data_from_api(f"{URL_EP}city")
if cities != None:
    for city in cities["LtsItem"]:
        new_city = {
            "matinh": city["ID"], "tentinh":city["Title"],
            "short_name": city["SolrID"]
        }
        # Lấy ds quận quyện
        quan_huyenurl = f"{URL_EP}city/{city['ID']}/district"
        qh_data = get_data_from_api(quan_huyenurl)
        if qh_data != None:
            list_quan_quyen = []
            for quan in qh_data:
                list_quan_quyen.append({
                    "maqh": quan["ID"], "tenqh": quan["Title"],
                    "short_name": quan["SolrID"]
                })
            # Thêm vào tỉnh đang xét
            new_city["quan_huyen"] = list_quan_quyen
        data.append(new_city)

print(data)
# Lưu data lấy được xuống file
with open("thong_tin_doanh_nghiep.json", "w",
          encoding="utf-8") as file:
    file.write(json.dumps(
        data, indent=4, ensure_ascii=False
    ))
