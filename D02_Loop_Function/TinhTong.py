"""
Nhập số nguyên dương 0 < N <= 100
Tính tổng các số lẻ từ 1 đến N
"""

N = 0
while True:
    try:
        N = int(input("Nhap so nguyen duong <= 100: "))
        if N > 0 and N <= 100:
            break # Thoat vong lap
    except:
        print("Khong phai so nguyen")

print(f"Da nhap N = {N}")

# Tinh tong gia tri cac so le tu 1 den N
S = 0
i = 1
while i <= N :
    S = S + i
    i = i + 2
print(f"Tong cac so le tu 1 den N la {S}")
