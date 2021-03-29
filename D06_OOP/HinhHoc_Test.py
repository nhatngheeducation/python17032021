from QuanLyHinhHoc import *

hh = HinhHoc()
hh.tinh_dien_tich_chu_vi()
print(hh)
hcn = HinhChuNhat(7.7, 3)
hcn.tinh_dien_tich_chu_vi()
print(hcn)
ht = HinhTron(4.5)
ht.tinh_dien_tich_chu_vi()
print(ht)

mang_hinh = []
mang_hinh.append(hcn)
mang_hinh.append(ht)
for hinh_item in mang_hinh:
    hinh_item.tinh_dien_tich_chu_vi()
    print(hinh_item)