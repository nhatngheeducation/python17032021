import csv

with open("demo_csv1.csv", "w", encoding="utf-8") as file:
    objcsv = csv.writer(file, delimiter=",")
    # Ghi theo hàng
    objcsv.writerow(["STT", "Họ tên", "Điện thoại"])
    objcsv.writerow([1, "Lê Anh, Hùng", "0909895147"])
    objcsv.writerow([2, "Lê Hùng, Anh", "0909895145"])

# Ghi dict xuống file csv
data = [
    { "MaHH": 1, "TenHH": "Tivi Toshiba", "Gia": 132452},
    { "MaHH": 2, "TenHH": "Tủ lạnh", "Gia": 232452},
    { "MaHH": 3, "TenHH": "Máy giặc", "Gia": 432452},
]
