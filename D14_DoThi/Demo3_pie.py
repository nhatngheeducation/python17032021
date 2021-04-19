import matplotlib.pyplot as plt
import numpy as np

data_labels=["333", "Tiger", "Ken", "Bud"]
y = np.array([95, 25, 25, 15])
myexplode = [0.1, 0, 0, 0] # ĐỘ HỞ
plt.pie(y, labels=data_labels, explode=myexplode)
plt.legend(title="BIA")
plt.show()