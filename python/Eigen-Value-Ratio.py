import matplotlib.pyplot as plt
import numpy as np


ratio = [80.02, 81.35, 82.34, 82.90, 83.35, 84.03, 85.08, 85.79, 86.78, 87.21,
         88.95, 89.08, 88.79, 89.97, 90.80, 90.34, 90.21, 90.31, 90.01, 90.33,
         90.33, 90.56, 90.25, 90.21, 90.58, 90.68, 90.03, 90.45, 90.30, 90.56,
         90.43, 90.34, 90.56, 90.67, 90.47, 90.36, 90.45, 90.47, 90.23, 90.35]


steps = np.array(range(40)) + 1


plt.title('Adaption value development')
plt.xlabel('step')
plt.ylabel('adaption value')
plt.xticks(steps, steps)

plt.plot(steps, ratio, 'b', label='adaption value')


# plt.legend(bbox_to_anchor=[0.3, 1])
# plt.grid()
plt.show()
