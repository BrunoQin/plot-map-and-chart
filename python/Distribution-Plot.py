from matplotlib import pyplot as plt
import numpy as np

# 2000-2500, 2500-3000, 3000-3500, 3500-4000, 4000-4500, 4500-5000, 5000-5500, 5500-6000, 6000-6500, 6500-7000,
# 7000-7500, 7500-8000, 8000-8500, 8500-9000, 9000-9500, 9500-10000, 10000-10500, 10500-11000, 11000-11500, 11500-12000,
# 12000-12500, 12500-13000, 13000-13500


d1 = [49, 59, 63, 67, 72, 103, 94, 52, 44, 39, 87, 91, 88, 77, 47, 45, 29, 39, 30, 13, 6, 6, 0]
d2 = [38, 53, 48, 49, 50, 55, 49, 49, 42, 48, 89, 98, 110, 92, 62, 51, 41, 42, 49, 47, 17, 12, 9]

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
                   data1_name='PSO',
                   data1_color='#539caf',
                   data2=np.array(d2),
                   data2_name='DFSPSO',
                   data2_color='#7663b0',
                   x_label='adaption value',
                   y_label='Frequency',
                   title='Distribution of adaption value for two different algorithm')

plt.show()
