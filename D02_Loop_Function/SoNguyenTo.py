# Nhập vào 1 số N
# Xuất ra số N đó có phải số nguyên tố hay không
# In các số nguyên tố nhỏ hơn N
# In N số nguyên tố đầu tiên

N = 0
while True:
    try:
        N = int(input("Nhap so nguyen duong <= 100: "))
        if N > 0 and N <= 100:
            break # Thoat vong lap
    except:
        print("Khong phai so nguyen")

print(f"Da nhap N = {N}")


def La_So_Nguyen_To(X: int):
    """
    Kiểm tra X có phải là Số nguyên tố không
    :param X: Giá trị cần kiểm tra
    :return: True or False
    """
    if X < 2:
        return False
    la_so_nguyen_to = True
    i = 2
    while i < X:
        if X % i == 0: # Chia het (chia du 0)
            la_so_nguyen_to = False
            break
        i = i + 1
    return la_so_nguyen_to

kq = f"{N} la So Ngto" if La_So_Nguyen_To(N) else f"{N} ko la so ngto"
print(kq)

# In các số nguyên tố nhỏ hơn N
step = 2
print(f"Cac so nguyen to nho hon {N} la: ")
while step < N:
    if La_So_Nguyen_To(step):
        print(step)
    step = step + 1

# In ra N so nguyen to dau tien
# count = 0
step = 2
danhsach = [] # Mang list
while len(danhsach) < N:
    if La_So_Nguyen_To(step):
        danhsach.append(step)
        # count = count + 1
    step = step + 1
print(danhsach)
print(len("NhatNghe"))