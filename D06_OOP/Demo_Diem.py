from Diem import Diem3D, Diem

diem_a = Diem()
# Có 2 cách gọi hàm Xuat
diem_a.Xuat()   # Cách thông dụng
Diem.Xuat(diem_a)
diem_a.x = 10
diem_a.y = -9.9
diem_a.Xuat()
diem_b = Diem()
diem_b.x = 12
diem_b.y = -9.9
print("Khoảng cách từ điểm A đến điểm B là: ",
      diem_b.tinh_khoang_cach(diem_a))

diem_c = Diem(12, 3)
diem_d = Diem(101) # (101, 0)
print(diem_d)
print(f"Khoảng cách từ C{diem_c} đến điểm D{diem_d} là ",
      diem_c.tinh_khoang_cach(diem_d))

a_3d = Diem3D(1,2,3)
print(a_3d)
a_3d.dich_chuyen(1,1,1)
print(a_3d)