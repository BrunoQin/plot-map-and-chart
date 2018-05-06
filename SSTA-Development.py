import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
import netCDF4

MONTHS = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

file_n = netCDF4.Dataset('/Users/Bruno/Desktop/3_29_ocean.nc')
lat_n = file_n.variables['yt_ocean'][:]
lon_n = file_n.variables['xt_ocean'][:]
data_n = file_n.variables['sst'][:, :, :]
file_n.close()

file_s = netCDF4.Dataset('/Users/Bruno/Desktop/63.nc')
lat_s = file_s.variables['yt_ocean'][:]
lon_s = file_s.variables['xt_ocean'][:]
data_s = file_s.variables['sst'][:, :, :]
file_s.close()


def plot_ssta(da, ax=None, shift=True):
    """plots an array of lat by lon on a coastline map"""

    m = Basemap(projection="cyl", llcrnrlon=-279.5, urcrnrlon=79.5, llcrnrlat=-81.5, urcrnrlat=89.5, resolution='c')

    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral',lake_color='aqua')
    m.drawcoastlines(linewidth=0.1)

    m.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0], linewidth=0.3, color='k', fontsize=10)
    m.drawmeridians(np.arange(-180, 180, 60), labels=[0, 0, 0, 1], linewidth=0.1, color='k', fontsize=10)

    xx = np.linspace(-279.5, 79.5, 360)
    yy = np.linspace(-81.5, 89.5, 200)
    lon, lat = np.meshgrid(xx, yy)
    x, y = m(lon, lat)
    da[da == 0] = 'nan'
    m.pcolormesh(x, y, da, shading='flat', cmap=plt.cm.jet)
    return m


fig = plt.figure(0, (20, 8))
grid = ImageGrid(fig, 111, nrows_ncols=(3, 4), axes_pad=0.5, cbar_mode='single', cbar_location="right")
for i in range(12):
    plt.sca(grid[i])
    plot_ssta(data_n[i] - data_s[i])
    plt.title(MONTHS[i+1])

plt.colorbar(cax=grid[0].cax, orientation="vertical")
plt.suptitle("SSTA Development")
# plt.tight_layout()
plot_margin = 0.25
x0, x1, y0, y1 = plt.axis()
plt.axis((x0 - plot_margin, x1 + plot_margin, y0 - plot_margin, y1 + plot_margin))
plt.show()
