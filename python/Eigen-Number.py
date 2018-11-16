import matplotlib.pyplot as plt

dimension = [60, 70, 80, 90]
convergence_step = [34, 29.4, 27.3, 26]
num_eigen = [150, 160, 220, 325]


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(dimension, convergence_step, 'b', label='average convergence step')
ax1.set_ylabel('steps')
ax1.set_title("relation between average convergence step and number of eigen value")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(dimension, num_eigen, 'r', label='average convergence step')
ax2.set_ylabel('number of eigen value')

plt.show()
