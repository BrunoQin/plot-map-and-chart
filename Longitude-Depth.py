import matplotlib.pyplot as plt
import numpy as np
import netCDF4

file = netCDF4.Dataset('/Users/Bruno/Desktop/ocean_temp_salt_6.nc')
lat = file.variables['yaxis_1'][:]
lon = file.variables['xaxis_1'][:]
data = file.variables['temp'][0, 0:11, 95:105, :]
file.close()

data[data == 0] = 'nan'

final = np.mean(data, axis=1)
final = final[:, 50:200]

xx = np.linspace(0, 150, 150)
yy = np.linspace(0, 11, 11)
Lon, Lat = np.meshgrid(xx, yy)

g = plt.contourf(Lon, Lat, final, 8, alpha=.75, cmap=plt.cm.jet)
plt.contour(Lon, Lat, final, 8, colors='black', linewidth=.5)

plt.xlim((0, 150))
plt.ylim((11, 0))
# #设置坐标轴名称
plt.xlabel('Longitude')
plt.ylabel('Depth')
# #设置坐标轴刻度
my_x_ticks = np.arange(0, 150, 29.99)
my_y_ticks = np.arange(11, 0, -2)
plt.xticks(my_x_ticks, ['130°E', '160°E', '170°W', '140°W', '110°W', '80°W'])
plt.yticks(my_y_ticks)
plt.colorbar(g)

plt.title('Latitude average Longitude-Depth Sea temperature anomaly', fontsize=9)
plt.show()
