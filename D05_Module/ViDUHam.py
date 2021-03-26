# flake8
# def tinh_dien_tich_hcn(dai = 10, rong): # Sai
def tinh_dien_tich_hcn(dai, rong = 1):
    print("Dài", dai, "rộng", rong)
    print("S=", dai * rong)

# Demo
tinh_dien_tich_hcn(7, 4)
tinh_dien_tich_hcn(7)

# def tinh_toan(a = 10, b, c = 7): # Sai
def tinh_toan(a = 10, b = 5, c = 7):
    print("a=", a, ", b =", b, ", c =", c)
    return (a + b)**c;
# Tham số mặc định tính liên tục từ phải tính qua
print(tinh_toan())
print(tinh_toan(19))
print(tinh_toan(19, 2))
print(tinh_toan(19, 2, 3))