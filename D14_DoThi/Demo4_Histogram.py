import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 250)
# x = np.random.randn(100) # tao 100 phan tu
print(x)

plt.hist(x, 7) # So tang
plt.show()