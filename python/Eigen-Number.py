import matplotlib.pyplot as plt

dimension = [60, 70, 80, 90]
convergence_step = [34, 29.4, 27.3, 26]
num_eigen = [150, 160, 220, 325]


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(dimension, convergence_step, 'b', label='Average convergence step')
ax1.set_ylabel('Average convergence steps')
ax1.set_title("Average convergence step and accumulative ratio")
ax1.set_xlabel('Accumulative ratio')

ax2 = ax1.twinx()  # this is the important function
ax2.plot(dimension, num_eigen, 'r', label='average convergence step')
ax2.set_ylabel('Number of eigen value')

plt.show()
