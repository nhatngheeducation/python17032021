# Ket hop list voi dict, mỗi sản phẩm là 1 dict
# gồm mã, tên, giá
from builtins import input

ds_san_pham = [
    {"masp": 1, "tensp": "Iphone X", "giaban": 21090000},
    {"masp": 2, "tensp": "Samsung Gear", "giaban": 1009000},
    {"masp": 3, "tensp": "Dell XPS", "giaban": 31000000},
    {"masp": 4, "tensp": "Galaxy Tab 9", "giaban": 13009000}
]

print("DANH SÁCH SẢN PHẨM")
for sanpham in ds_san_pham:
    # print(sanpham)
    sp = []
    for key in sanpham:
        sp.append(str(sanpham[key]))
    # print(sp)
    print(", ".join(sp))

# Tạo dict tmp chứa hàng hóa
tmp = dict()
for sp in ds_san_pham:
    tmp[sp.get('masp')] = sp
print(tmp)

# Đi chợ mua hàng hóa
mua = {}
while True:
    ma_sp = int(input("Nhập mã sản phẩm: "))
    # Tìm xem trong danh sách có mã sản phẩm này ko?
    if tmp.get(ma_sp): # Tìm thấy
        mua[ma_sp] = int(input("Số lượng: "))
    else:
        print(f"Không tìm thấy mã {ma_sp}")
    mua_tiep = input("Mua tiếp không? (C/K)")
    if mua_tiep.upper() == "K":
        break

# In bảng tính tiền
tong_tien = 0
if len(mua) == 0:
    print("Bạn không chọn mua")
else:
    for masp in mua:
        sp_tmp = tmp.get(masp)
        print(f"{sp_tmp.get('tensp')}: ",
              f"{sp_tmp.get('giaban')} x ",
              f"{mua.get(masp)}")
        tong_tien += sp_tmp.get('giaban') * mua.get(masp)
    print(f"Tổng tiền thanh toán: {tong_tien}")        
