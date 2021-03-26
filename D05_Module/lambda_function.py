# Định nghĩa hàm (x+y)^z
tinh_tong = lambda x,y,z: (x + y)**z

print(tinh_tong(1,1,2))
print(tinh_tong(3,1,3))

chao = lambda ten: print("Chào", ten)
chao("Hải")

# Filter: lọc bớt các phần tử trong mảng
# kết quả tạo Filter object ==> convert list
mang_so = [19, 21, 78, 24, 79, 34, 22, 46]
mang_moi = list(filter(lambda x: x % 3 == 0, mang_so))
print(mang_moi)

# map: thay đổi giá trí mạng ==> map obj ==> convert
new_array = list(map(lambda x: (x / 2) ** 2, mang_so))
print(new_array)