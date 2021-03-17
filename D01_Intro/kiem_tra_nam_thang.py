"""
Nhập năm, tháng
Xuất là năm nhuận hay không và tháng đó có nhiêu ngày?
"""
nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))

la_nam_nhuan = False
if nam % 400 == 0 :
    la_nam_nhuan = True
elif (nam % 4 == 0) and nam % 100 != 0:
    la_nam_nhuan = True
# else:
#     la_nam_nhuan = False

ket_qua = "là" if la_nam_nhuan else "không là"

if la_nam_nhuan:
    print(f"năm {nam} là năm nhuận")
else:
    print(f"năm {nam} không là năm nhuận")

# Không có switch case ==> định nghĩa dạng dict (key ==> value)
switcher = {
    1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10 : 31, 11: 30, 12: 31,
    2: 29 if la_nam_nhuan else 28
}
so_ngay = switcher.get(thang)
print(f"Tháng {thang} có {so_ngay} ngày")

# list: chỉ số là con số 0, 1, 2,....
thang_31ngay = [1, 3, 5, 7, 8, 10, 12]
print(thang_31ngay[0])
if thang in thang_31ngay:
    print(f"Tháng {thang} có 31 ngày")