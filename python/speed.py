import matplotlib.pyplot as plt
import numpy as np
import math

step = np.array(range(40)).reshape(40, 1)
print(step.shape)
## this.c1 = 0.2 * Math.pow(Math.sin((Math.PI / 2) * (1 - n / STEP)), 2);
values_c1 = np.sin((math.pi / 4) * (1 - step / 40)) ** 2
## this.c2 = 0.2 * Math.pow(Math.sin((Math.PI * n) / (2 * STEP)), 2);
values_c2 = np.sin((math.pi * step / 2) / (2 * 40)) ** 2

step.reshape(1, 40)
values_c1.reshape(1, 40)
values_c2.reshape(1, 40)

plt.title('Adaption value development')
plt.xlabel('step')
plt.xticks([1, 6, 11, 16, 21, 26, 31, 36, 41], [1, 6, 11, 16, 21, 26, 31, 36, 41])
plt.ylabel('adaption value')

plt.plot(step, values_c1, 'b', label='c1')
plt.plot(step, values_c2, 'g', label='c2')


plt.legend(bbox_to_anchor=[0.25, 1])
# plt.grid()
plt.show()
