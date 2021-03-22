chuoi = input("Nhap chuoi: ")

# Định nghĩa mảng thống kê kí tự nhập
mang = dict()
for ky_tu in chuoi:
    mang[ky_tu] = chuoi.count(ky_tu)
print("Số lượng ký tự: ")
print(mang)