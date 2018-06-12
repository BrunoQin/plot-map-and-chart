import matplotlib.pyplot as plt
import numpy as np
import netCDF4

file_n = netCDF4.Dataset('/Users/Bruno/Desktop/0_3_ocean.nc')
data_n = file_n.variables['temp'][:, 0, :, :]
file_n.close()

file_s = netCDF4.Dataset('/Users/Bruno/Desktop/sst_ave300Y.nc')

MONTHS = {
    0: "sst_jan_ave",
    1: "sst_feb_ave",
    2: "sst_mar_ave",
    3: "sst_april_ave",
    4: "sst_may_ave",
    5: "sst_june_ave",
    6: "sst_july_ave",
    7: "sst_agu_ave",
    8: "sst_sep_ave",
    9: "sst_oct_ave",
    10: "sst_nov_ave",
    11: "sst_dec_ave"
}

nino4 = []
nino3 = []
for i in range(12):
    data_s = file_s.variables[MONTHS[i]][:, :]

    nino4_data = data_n[i, 83:108, 79:129] - data_s[83:108, 79:129]
    nino4.append(np.mean(nino4_data))

    nino3_data = data_n[i, 83:108, 129:189] - data_s[83:108, 129:189]
    nino3.append(np.mean(nino3_data))

file_s.close()

group_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.title('Nino3 & Nino4 index development')
plt.xlabel('Month')
plt.ylabel('index')

x = range(12)

plt.plot(x, nino3, 'b', label='nino3 index')
plt.plot(x, nino4, 'r--', label='nino4 index')
plt.xticks(x, group_labels, rotation=45)

plt.axhline(0.5, color='black')
# plt.axhline(-0.5, color='r', linestyle="--")

plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()
