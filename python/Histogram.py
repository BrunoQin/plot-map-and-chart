import matplotlib.pyplot as plt
import numpy as np
import matplotlib

i1 = 4
i2 = 10
i3 = 28

won = True
array = []
for line in open("../file/best-july.txt"):
    if won:
        index=i=tempI=iq=0
        if line[5]=='s':
            tempI = int(line[4])
            if line[11]=='-':
                index = int(line[iq+i2])
                i = iq+i3
            else:								#if line[11]!='-'&&line[12]=='-'
                index = int(line[iq+i2:iq+i2+2])
                i = iq+i3+1
        else:
            tempI = int(line[4:6])
            iq=1
            if line[12]=='-':
                index = int(line[iq+i2])
                i = iq+i3
            else:								#if line[11]!='-'&&line[12]=='-'
                index = int(line[iq+i2:iq+i2+2])
                i = iq+i3+1

        temp = float(line[i:len(line)-1])
        array.append(temp)
        won = False
    else:
        won = True

print(array)

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
# 随机生成（10000,）服从正态分布的数据
data = np.array(array)
"""
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
plt.hist(data, bins=40, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("区间")
# 显示纵轴标签
plt.ylabel("频数/频率")
# 显示图标题
plt.title("频数/频率分布直方图")
plt.show()

