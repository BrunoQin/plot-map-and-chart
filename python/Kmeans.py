import numpy as np

i1 = 4
i2 = 10
i3 = 28

won = True
july = []
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
        july.append(temp)
        won = False
    else:
        won = True

july_data = []
for i in range(30):
    for line in open("../file/july/" + str(i) + "_s.txt"):
        line = line.strip()
        if line != "":
            if line[0]=='s':
                temp = float(line[16:len(line)-1])
            else:
                temp = float(line)
            july_data.append(temp)
july_data = np.array(july_data)
july_data = np.reshape(july_data, (-1, 330)).T
print(july_data.shape)

oct = []
for line in open("../file/best-oct.txt"):
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
        oct.append(temp)
        won = False
    else:
        won = True

oct_data = []
for i in range(30):
    for line in open("../file/oct/" + str(i) + "_s.txt"):
        line = line.strip()
        if line != "":
            if line[0]=='s':
                temp = float(line[16:len(line)-1])
            else:
                temp = float(line)
            oct_data.append(temp)
oct_data = np.array(oct_data)
oct_data = np.reshape(oct_data, (-1, 330)).T
print(oct_data.shape)

jan = []
for line in open("../file/best-jan.txt"):
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
        jan.append(temp)
        won = False
    else:
        won = True

jan_data = []
for i in range(30):
    for line in open("../file/jan/" + str(i) + "_s.txt"):
        line = line.strip()
        if line != "":
            if line[0]=='s' and line[14]=='s':
                temp = float(line[16:len(line)-1])
            elif line[0]=='s' and line[15] == 's':
                temp = float(line[17:len(line)-1])
            elif line[0]=='s' and line[16] == 's':
                temp = float(line[17:len(line)-1])
            else:
                temp = float(line)
            jan_data.append(temp)
jan_data = np.array(jan_data)
jan_data = np.reshape(jan_data, (-1, 330)).T
print(jan_data.shape)

apr = []
for line in open("../file/best-apr.txt"):
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
        apr.append(temp)
        won = False
    else:
        won = True

apr_data = []
for i in range(30):
    for line in open("../file/apr/" + str(i) + "_s.txt"):
        line = line.strip()
        if line != "":
            if line[0]=='s':
                temp = float(line[16:len(line)-1])
            else:
                temp = float(line)
            apr_data.append(temp)
apr_data = np.array(apr_data)
apr_data = np.reshape(apr_data, (-1, 330)).T
print(apr_data.shape)

july = np.array(july)
july = np.reshape(july, (-1, 30)).T
july = np.reshape(july, (1, -1))

oct = np.array(oct)
oct = np.reshape(oct, (-1, 30)).T
oct = np.reshape(oct, (1, -1))

for i in range(20):
    jan.append(-222)
jan = np.array(jan)
jan = np.reshape(jan, (-1, 30)).T
jan = np.reshape(jan, (1, -1))
jan = jan[~np.isnan(jan)]
jan = np.reshape(jan, (1, -1))

for i in range(20):
    apr.append(np.nan)
apr = np.array(apr)
apr = np.reshape(apr, (-1, 30)).T
apr = np.reshape(apr, (1, -1))
apr = apr[~np.isnan(apr)]
apr = np.reshape(apr, (1, -1))

# july, oct, jan, apr, july_data, oct_data, jan_data, apr_data

data = np.hstack((july_data, oct_data))
data = np.hstack((data, jan_data))
data = np.hstack((data, apr_data))
data = data.T

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
y_pred = KMeans(n_clusters=2, random_state=9).fit_predict(data)
pca = PCA(n_components=3)
pca.fit(data)
data = pca.transform(data)

fig = plt.figure()
ax = Axes3D(fig)
plt.scatter(data[:, 0], data[:, 1], data[:, 2], c=y_pred)
plt.show()

