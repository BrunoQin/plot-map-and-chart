import numpy as np
import matplotlib.pyplot as plt

# 2000-2500, 2500-3000, 3000-3500, 3500-4000, 4000-4500, 4500-5000, 5000-5500, 5500-6000, 6000-6500, 6500-7000,
# 7000-7500, 7500-8000, 8000-8500, 8500-9000, 9000-9500, 9500-10000, 10000-10500, 10500-11000, 11000-11500, 11500-12000,
# 12000-12500, 12500-13000, 13000-13500


d1 = [49, 59, 63, 67, 72, 103, 94, 52, 44, 39, 87, 91, 88, 77, 47, 45, 29, 39, 30, 13, 6, 6, 0]
d2 = [38, 53, 48, 49, 50, 55, 49, 49, 42, 48, 89, 98, 110, 92, 62, 51, 41, 42, 49, 47, 17, 12, 9]

values1 = []
values2 = []
for i in range(len(d1)):
    for j in range(d1[i]):
        values1.append((2000 + 500 * i) + 1)

for i in range(len(d2)):
    for j in range(d2[i]):
        values2.append((2000 + 500 * i) + 1)

d1 = values1
d2 = values2


d1 = np.array(d1)
d2 = np.array(d2)

all_data = np.array([d1, d2]).reshape(1200, 2)
labels = ['x1', 'x2']

bplot = plt.boxplot(all_data, patch_artist=True, labels=labels)  # 设置箱型图可填充
plt.title('Rectangular box plot')

colors = ['pink', 'lightblue'] #, 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)  # 为不同的箱型图填充不同的颜色

# plt.grid(True, axis=1)
plt.xlabel('Two separate samples')
plt.ylabel('Observed values')
plt.show()
