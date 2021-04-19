import matplotlib.pyplot as plt
import numpy as np

labels = np.array(["Lua", "Gao", "Mi", "Duong"])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([3.3, 7.5, 1.9, 8.3])
index = np.arange(4)
width = 0.2
plt.bar(index, y1, color="red", width=0.2, label="Q1")
plt.bar(index+width, y2, color="blue", width=0.2, label="Q2")
plt.title("Thong ke doanh so")
plt.legend(loc='best')
plt.xlabel("Thuc pham")
plt.ylabel("San luong (tan)")
plt.xticks(index+width/2, labels)
plt.show()