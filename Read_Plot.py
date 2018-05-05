import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import netCDF4

file = netCDF4.Dataset('/Users/Bruno/Desktop/ocean_temp_salt_0.nc')

lat = file.variables['yaxis_1'][:]

lon = file.variables['xaxis_1'][:]

data = file.variables['temp'][0, 0, :, :]
file.close()

m = Basemap(llcrnrlon=-279.5, urcrnrlon=79.5, llcrnrlat=-81.5, urcrnrlat=89.5, resolution='c')

m.drawcoastlines(linewidth=0.1)
m.fillcontinents(color='coral', lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

m.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0], linewidth=0.3, color='k', fontsize=10)
m.drawmeridians(np.arange(-180, 180, 60), labels=[0, 0, 0, 1], linewidth=0.1, color='k', fontsize=10)

xx = np.linspace(-279.5, 79.5, 360)
yy = np.linspace(-81.5, 89.5, 200)
Lon, Lat = np.meshgrid(xx, yy)
x, y = m(Lon, Lat)
cs = m.pcolormesh(x, y, data, shading='flat', cmap=plt.cm.jet)
cbar = m.colorbar(cs)
cbar.outline.set_linewidth(1)
plt.title('Global Sea surface temperature anomaly', fontsize=9)
plt.show()
