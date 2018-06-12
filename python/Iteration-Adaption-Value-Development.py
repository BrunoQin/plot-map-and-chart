import matplotlib.pyplot as plt
import numpy as np


values = [14905, 13885,	18342, 11203, 12778, 15431,	12109, 15278, 16163, 14623, \
          13557, 13619, 14988, 18769, 17982, 18383, 17914, 17952, 17431, 18217]
steps = np.array(range(20)) + 1


plt.title('Adaption value development')
plt.xlabel('step')
plt.ylabel('adaption value')
plt.xticks(steps, steps)

plt.plot(steps, values, 'b', label='adaption value')


plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()
