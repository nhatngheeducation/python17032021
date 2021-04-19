# Vi du ve duong
import matplotlib.pyplot as plt
import numpy as np
import random

n = random.randint(5, 50)
x = []
y = []
for i in range(0, n):
    x.append(random.randint(1, 200))
    y.append(random.randint(1, 200))

xpoints = np.array(x)
ypoints = np.array(y)
plt.subplot(3, 2, 1)
plt.plot(xpoints, ypoints)
plt.title("DEMO 1")
plt.xlabel("So nguoi")
plt.ylabel("Thu nhap")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(3, 2, 4)
plt.title("DEMO 2")
plt.plot(x,y)

plt.show()