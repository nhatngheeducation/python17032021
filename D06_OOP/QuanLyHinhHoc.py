from math import *
class HinhHoc:
    dien_tich = 0
    chu_vi = 0

    def __str__(self):
        return f"S = {self.dien_tich}, P = {self.chu_vi}"

    def tinh_dien_tich_chu_vi(self):
        pass

class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich_chu_vi(self):
        self.dien_tich = self.dai * self.rong
        self.chu_vi = (self.dai + self.rong) * 2

    def __str__(self):
        return f"HCN D = {self.dai}, R = {self.rong} có " + \
                f"{HinhHoc.__str__(self)}"

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich_chu_vi(self):
        self.dien_tich = self.ban_kinh ** 2 * pi;
        self.chu_vi = self.ban_kinh * 2 * pi;

    def __str__(self):
        return f"Tron R = {self.ban_kinh} có " + \
                f"{HinhHoc.__str__(self)}"