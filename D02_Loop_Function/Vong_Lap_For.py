danhsachmon = ["Cơm", "Phở", "Hủ tiếu", "Mì quảng"]
for mon in danhsachmon:
    print(mon)

# Thư viện chọn số ngẫu nhiên
import random
i = random.randint(0, len(danhsachmon) - 1)
# i = random.randint(0, 4)
print("Chọn đại món", danhsachmon[i])


# Sinh 1 bộ số (không trùng) vietlotte (6 số) 6/55
# Tìm số lớn nhất trong bộ đó
vietlott655 = []
while len(vietlott655) < 6:
    lucky_number = random.randint(1, 55)
    if lucky_number in vietlott655:
        continue
    vietlott655.append(lucky_number)

print("Bộ số của bạn", vietlott655)
max_number = vietlott655[0] # Phan tu dau
for number in vietlott655:
    if number > max_number:
        max_number = number
print(f"Số lớn nhất là {max_number}")