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

print(july.shape)
print(oct.shape)
print(jan.shape)
print(apr.shape)

print(july_data.shape)
print(oct_data.shape)
print(jan_data.shape)
print(apr_data.shape)


data = None
percentage = 0.6
print(np.max(july))
print(np.max(oct))
print(np.max(jan))
print(np.max(apr))
for i in range(180):
    if july[0, i] / np.max(july) >= percentage:
        if data is None:
            data = np.array(july_data[:, i:(i+1)])
        else:
            data = np.hstack((data, july_data[:, i:(i+1)]))

for i in range(180):
    if oct[0, i] / np.max(oct) >= percentage:
        if data is None:
            data = np.array(oct_data[:, i:(i+1)])
        else:
            data = np.hstack((data, oct_data[:, i:(i+1)]))

for i in range(400):
    if jan[0, i] / np.max(jan) >= percentage:
        if data is None:
            data = np.array(jan_data[:, i:(i+1)])
        else:
            data = np.hstack((data, jan_data[:, i:(i+1)]))

for i in range(190):
    if apr[0, i] / np.max(apr) >= percentage:
        if data is None:
            data = np.array(apr_data[:, i:(i+1)])
        else:
            data = np.hstack((data, apr_data[:, i:(i+1)]))

print(data.shape)

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from pandas import Series, DataFrame

data = data.T
df2 = DataFrame(data[:, 0:10], index=range(len(data)),
               columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
df2.to_csv('../file/fakedata-60.txt', sep='\t', index=True)
print(df2)

# y_pred = KMeans(n_clusters=2, random_state=9).fit_predict(data)
pca = PCA(n_components=10)
pca.fit(data)
data = pca.transform(data)

print(data.shape)



df = DataFrame(data, index=range(len(data)),
               columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

df.to_csv('../file/data-60.txt', sep='\t', index=True)
print(df)



