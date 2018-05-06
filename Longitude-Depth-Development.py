import matplotlib.pyplot as plt
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
data_n = file_n.variables['temp'][:, 0:11, 95:105, :]
file_n.close()

file_s = netCDF4.Dataset('/Users/Bruno/Desktop/00610101.ocean_month.nc')
lat_s = file_s.variables['yt_ocean'][:]
lon_s = file_s.variables['xt_ocean'][:]
data_s = file_s.variables['temp'][:, 0:11, 95:105, :]
file_s.close()


def plot_longitude_depth(da, ax=None, shift=True):
    """plots an array of lat by lon on a coastline map"""

    da[da == 0] = 'nan'

    final = np.mean(da, axis=1)
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
    return g


fig = plt.figure(0, (20, 8))
grid = ImageGrid(fig, 111, nrows_ncols=(3, 4), axes_pad=0.5, cbar_mode='single', cbar_location="right")
for i in range(12):
    plt.sca(grid[i])
    plot_longitude_depth(data_n[i] - data_s[24+i])
    plt.title(MONTHS[i+1])

plt.colorbar(cax=grid[11].cax, orientation="vertical")
plt.suptitle("Longitude-Depth Development")
plt.tight_layout()
plot_margin = 0.25
x0, x1, y0, y1 = plt.axis()
plt.axis((x0 - plot_margin, x1 + plot_margin, y0 - plot_margin, y1 + plot_margin))
plt.show()
