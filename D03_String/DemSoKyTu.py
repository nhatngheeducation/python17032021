chuoi = input("Nhap chuoi: ")

# Định nghĩa mảng thống kê kí tự nhập
mang = dict()
for ky_tu in chuoi:
    mang[ky_tu] = chuoi.count(ky_tu)
print("Số lượng ký tự: ")
print(mang)

# Thống kê chữ hoa, chữ thường, số, kí tự đặc biệt
so_luong_kitu_hoa = 0
so_luong_kitu_thuong = 0
so_luong_kitu_so = 0
so_luong_kitu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.isupper():
        so_luong_kitu_hoa += 1
    elif ky_tu.islower():
        so_luong_kitu_thuong += 1
    elif ky_tu.isnumeric():
        so_luong_kitu_so += 1
    else:
        so_luong_kitu_dac_biet += 1
print(f"Chữ thường {so_luong_kitu_thuong}")
print(f"Chữ số {so_luong_kitu_so}")
print(f"Ký tự đặc biệt {so_luong_kitu_dac_biet}")

# Dem xem co bao nhieu tu
print("Chuoi ban dau: ", chuoi)
print(chuoi.count("=="))
while chuoi.count("==") > 0:
    chuoi = chuoi.replace("==", "=")
print("Chuoi sau replace: ", chuoi)
mang_cac_tu = chuoi.split("=")
print(f"Có {len(mang_cac_tu)} từ. Đó là {','.join(mang_cac_tu)}")
print(mang_cac_tu)