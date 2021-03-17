hoten="Lê Hoàng"
hoTen="Lê Hoàng"
ho_ten="Lê Hoàng"   # Tốt nhất snake_case

# Nhập vào họ tên, tuổi
ho_ten = input("Tên của bạn:")
print(f"Chào anh/chị {ho_ten}")
print(type(ho_ten))

try:
    tuoi = int(input("Tuổi: "))
    print(type(tuoi))
except Exception as e:
    print("Có lỗi", e)
finally:
    print("Kết thúc")

diem_so = 7.8
la_nam_nhuan = True
la_nam_nhuan = False


# Định nghĩa hàm in bảng cửu chương
'''Ghi chú 1 dòng'''
"""
dòng 1
dòng 2
"""
def in_bang_cuu_chuong(n, m):
    """

    :param n:
    :param m:
    :return:
    """
    pass