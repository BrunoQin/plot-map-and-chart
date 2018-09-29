import matplotlib.pyplot as plt
import numpy as np


dfspso_values = [9905, 8885, 13342, 6203, 7778, 10431,	7109, 10278, 11163, 11123,
                 11157, 12119, 12388, 13769, 12982, 13383, 12914, 12952, 12431, 13217,
                 13283, 12998, 12967, 13065, 13564, 13265, 13374, 13896, 13697, 13745,
                 13898, 13934, 13934, 13798, 13749, 13778, 13710, 13880, 13818, 13890]

pso_values = [6067, 9719, 7642, 6002, 9406, 6646, 8190, 9801, 12673, 8858,
              5711, 9542, 7843, 8811, 7202, 8812, 8423, 7182, 7750, 8255,
              8537, 8449, 8316, 8298, 9220, 8910, 9230, 8818, 9098, 8976,
              9308, 9587, 8902, 8976, 9367, 9227, 9398, 9546, 9529, 9607]

steps = np.array(range(40)) + 1


plt.title('Adaption value development')
plt.xlabel('step')
plt.ylabel('adaption value')
plt.xticks(steps, steps)

plt.plot(steps, dfspso_values, 'b', label='adaption value')
plt.plot(steps, pso_values, 'r', label='adaption value')


# plt.legend(bbox_to_anchor=[0.3, 1])
# plt.grid()
plt.show()
