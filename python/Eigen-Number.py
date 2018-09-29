import matplotlib.pyplot as plt
import numpy as np

steps = [60, 70, 80, 90]
convergence_step = [19, 18, 17, 14]
num_eigen = [84, 119, 165, 221]


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(steps, convergence_step, 'b', label='average convergence step')
ax1.set_ylabel('steps')
ax1.set_title("relation between average convergence step and number of eigen value")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(steps, num_eigen, 'r', label='average convergence step')
ax2.set_ylabel('number of eigen value')
# ax2.axhline(0.8, color='green', linestyle="--")

plt.show()
