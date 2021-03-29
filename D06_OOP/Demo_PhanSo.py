from Fraction import PhanSo

ps1 = PhanSo(7, 4)
ps2 = PhanSo(7, -8)
print(ps1, ps2)
ps3 = PhanSo(4, 8)
print(ps3)
ps3.rut_gon()
print(ps3)
result = ps1 + ps2
print(f"{ps1} + {ps2} = {result}")