import numpy as np
import matplotlib.pyplot as plt
import random

# 7000-7700, 7700-8400, 8400-9100, 9100-9800, 9800-10500, 10500-11200,
# 11200-11900, 11900-12600, 12600-13300, 13300-14000,


d1 = [3, 17, 29, 39, 33, 26, 16, 0, 0, 0]
d2 = [0, 0, 0, 0, 0, 21, 37, 46, 31, 27]

values1 = []
values2 = []
for i in range(len(d1)):
    for j in range(d1[i]):
        values1.append((7000 + 700 * i) + random.randint(0, 699))

for i in range(len(d2)):
    for j in range(d2[i]):
        values2.append((8100 + 700 * i) + random.randint(0, 699))


d1 = np.array(values1)
d2 = np.array(values2)

all_data = np.array([d1, d2]).T
labels = ['PSO', 'DPPSO']

bplot = plt.boxplot(all_data, patch_artist=True, labels=labels)  # 设置箱型图可填充
plt.title('Convergence adaption value box plot')

colors = ['pink', 'lightblue'] #, 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)  # 为不同的箱型图填充不同的颜色

# plt.grid(True, axis=1)
# plt.xlabel('Two separate samples')
plt.ylabel('Convergence adaption value')
plt.show()
