"""
Kiểm tra chuỗi có đối xứng không?
abcba       ==> True
Abcbe       ==> False
AbcddcbA    ==> True
"""
print(5/2)
print(int(5/2))
chuoi = input("Nhap chuoi")
la_chuoi_doi_xung = True
for i in range(0, int(len(chuoi)/2)):
    if chuoi[i].lower() != chuoi[-i-1].lower():
        la_chuoi_doi_xung = False
        break
if la_chuoi_doi_xung:
    print(f"{chuoi} : đối xứng")
else:
    print(f"{chuoi} : không đối xứng")

# Dao chuoi
# Cách 1
print("Chuoi dao nguoc", ''.join(reversed(chuoi)))
# Cách 2
my_reverse =[]
for i in range(0, len(chuoi)):
    my_reverse.append(chuoi[-i-1])
print(my_reverse)
print(''.join(my_reverse))
#Cách 3
print(chuoi[::-1])
print("Chuoi: ", chuoi[:-1])

print(chuoi[2::], chuoi[2:])
print(chuoi[-2::], chuoi[-2:])

t = chuoi.encode("utf-8")
print(t)
print(t.decode('utf-8'))