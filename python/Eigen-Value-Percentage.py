import matplotlib.pyplot as plt
import numpy as np

values = []
tem = 0
sum = []
for line in open("../file/s.ep2.txt"):
    values.append(float(line))
    tem += float(line)
    sum.append(tem)

for i in range(len(sum)):
    sum[i] = sum[i] / tem
    print(sum[i], i)

steps = np.array(range(len(values))) + 1


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(steps, values, 'b', label='eigen value')
ax1.set_ylabel('Eigen value')
ax1.set_title("Eigen value and accumulative ratio")
ax1.set_xlabel('Number of Eigen value')

ax2 = ax1.twinx()  # this is the important function
ax2.plot(steps, sum, 'r')
ax2.set_ylabel('Accumulative ratio')
ax2.axhline(0.8, color='green', linestyle="--")

plt.show()
