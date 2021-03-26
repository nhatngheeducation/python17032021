file = open("bang_cuu_chuong.txt", "w")
N = int(input("Nhap so: "))
for i in range(1, 11):
    chuoi = f"{N} x {i} = {N*i}\n"
    file.write(chuoi)
file.close()

file = open("bang_cuu_chuong.txt", "r")
dong = file.readlines()
for row in dong:
    print(row)
file.close()

import os
if os.path.exists("bang_cuu_chuong.txt"):
    os.remove("bang_cuu_chuong.txt")
