# Định nghĩa lớp PhanSo
from math import gcd
class PhanSo:
    def __init__(self, tu = 0, mau = 1):
        self.TuSo = tu
        self.MauSo = mau

    def __str__(self):
        return f"{self.TuSo}/{self.MauSo}"

    def rut_gon(self):
        uoc_so_chung = gcd(self.TuSo, self.MauSo)
        self.TuSo = int(self.TuSo / uoc_so_chung)
        self.MauSo = int(self.MauSo / uoc_so_chung)

    def cong(self, ps_khac):
        result = PhanSo()
        result.TuSo = self.TuSo *ps_khac.MauSo \
                      + self.MauSo * ps_khac.TuSo
        result.MauSo = self.MauSo * ps_khac.MauSo
        result.rut_gon()
        return result

    def __add__(self, ps_khac):
        result = PhanSo()
        result.TuSo = self.TuSo * ps_khac.MauSo \
                      + self.MauSo * ps_khac.TuSo
        result.MauSo = self.MauSo * ps_khac.MauSo
        result.rut_gon()
        return result
