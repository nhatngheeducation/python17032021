'''
Nhập vào 1 chuỗi
Xuất chuỗi gồm kí tự chữ thường phía trước, chữ hoa phía sau
'''
chuoi = input("Nhập chuỗi: ")
mang_chu_thuong = []
mang_chu_hoa = []
for ky_tu in chuoi:
    if ky_tu.islower():
        mang_chu_thuong.append(ky_tu)
    elif ky_tu.isupper():
        mang_chu_hoa.append(ky_tu)
print(mang_chu_thuong + mang_chu_hoa)
print("Xuất chuỗi:", ''.join(mang_chu_thuong + mang_chu_hoa))