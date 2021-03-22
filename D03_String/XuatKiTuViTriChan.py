'''
BT1: Nhập vào chuỗi ==> xuất các kí tự ở vị trí chẵn
'''

chuoi = input("Nhap vao chuoi: ")
print("Cac ki tu o vi tri chan")
# Cách 1
for i in range(0, len(chuoi)):
    if i % 2 == 0:
        print(chuoi[i])
# Cách 2
for i in range(0, len(chuoi), 2):
    print(chuoi[i])