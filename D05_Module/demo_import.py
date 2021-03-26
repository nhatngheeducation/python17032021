import os.path as mypath
import math
from datetime import date, timedelta

d = date.today()
d += timedelta(days=12)
print(d.strftime('%d/%m/%Y'))

ban_kinh = 3.19
dien_tich = ban_kinh ** 2 * math.pi
print("R =", ban_kinh, ", S =", dien_tich)

print(mypath.abspath(__file__))
