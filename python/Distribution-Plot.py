from matplotlib import pyplot as plt
import numpy as np

# 2000-2500, 2500-3000, 3000-3500, 3500-4000, 4000-4500, 4500-5000, 5000-5500, 5500-6000, 6000-6500, 6500-7000,
# 7000-7500, 7500-8000, 8000-8500, 8500-9000, 9000-9500, 9500-10000, 10000-10500, 10500-11000, 11000-11500, 11500-12000,
# 12000-12500, 12500-13000, 13000-13500


d1 = [29, 39, 63, 87, 102, 113, 94, 52, 44, 57, 69, 71,
      88, 91, 77, 65, 49, 0, 0, 0, 0, 0, 0]
d2 = [0, 1, 2, 1, 2, 2, 3, 5, 22, 38, 44, 52,
      68, 80, 91, 101, 116, 120, 116, 114, 97, 79, 34]

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


# 绘制堆叠的直方图
def overlaid_histogram(data1, data1_name, data1_color, data2, data2_name, data2_color, x_label, y_label, title):
    # 归一化数据区间，对齐两个直方图的bins
    max_nbins = 23
    data_range = [2000, 13500]
    binwidth = (data_range[1] - data_range[0]) / max_nbins
    bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)  # 生成直方图bins区间

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins=bins, color=data1_color, alpha=1, label=data1_name)
    ax.hist(data2, bins=bins, color=data2_color, alpha=0.75, label=data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc='best')


# Call the function to create plot
overlaid_histogram(data1=np.array(d1),
                   data1_name='PPSO',
                   data1_color='#539caf',
                   data2=np.array(d2),
                   data2_name='DPPSO',
                   data2_color='#7663b0',
                   x_label='Adaption value',
                   y_label='Number of particles',
                   title='Distribution of the adaption values')

plt.show()
