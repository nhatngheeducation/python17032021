"""
Nhập vào số nguyên. In ra chuỗi số đảo ngược, cách nhau bởi dấu " "
VD: 1279 ===> 9 7 2 1
"""
while True:
    try:
        so_nguyen = int(input("Nhập số nguyên: "))

        # Cách 1: dùng hàm
        chuoi_dao = ' '.join(reversed(str(so_nguyen)))
        print("Cách 1: ", chuoi_dao)

        # Cách 2: chia lấy nguyên, chia lấy dư cho 10
        so = []
        tmp = so_nguyen
        while tmp > 0:
            so.append(tmp % 10)
            tmp = tmp // 10
        print(f"{so_nguyen} đảo ngược {' '.join(so)}")

        break
    except Exception as ex:
        print("Lỗi", ex)
        continue