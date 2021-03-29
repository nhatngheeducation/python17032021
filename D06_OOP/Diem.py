# Class Diem: biểu diễn trong mặt phẳng Oxy
# import math ==> math.sqrt()
from math import *
class Diem:
    x = 0
    y = 0

    # seft: Thành phần object chỉ chính lớp đó
    def Xuat(self):
        print(f"({self.x}, {self.y})")

    def dich_chuyen(self, dx, dy):
        self.x += dx
        self.y += dy

    def tinh_khoang_cach(self, diem_khac):
        dx = diem_khac.x - self.x
        dy = diem_khac.y - self.y
        return sqrt(dx ** 2 + dy ** 2)

    # Hàm tạo constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Hàm trả về kiểu chuỗi
    def __str__(self):
        return f"({self.x}, {self.y})"


# Định nghĩa lớp Diem3D kế thừa từ lớp Diem
class Diem3D(Diem):
    z = 0
    def __init__(self, x = 0, y = 0, z = 0):
        # Diem.__init__(self, x, y)
        # Từ khóa super chỉ lớp cha (Diem)
        Diem.__init__(self, x, y)
        self.z = z

    def dich_chuyen(self, dx, dy, dz):
        Diem.dich_chuyen(self, dx, dy)
        self.z += dz

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"