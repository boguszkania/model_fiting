import numpy as np
import os
import glob
import matplotlib.pyplot as plt

dir_path = "C:\\Users\\ljxx5v\\Desktop\\"
data_paths = ["zFAS_obj0_fails_and_lsFit_bootstrap_bins-count=200_resample-size=300000.csv",
              "zFAS_obj0_fails_and_lsFit_bootstrap_bins-count=200_resample-size=600000.csv",
              "zFAS_obj0_fails_and_lsFit_bootstrap_bins-count=200_resample-size=900000.csv",
              "zFAS_obj0_fails_and_lsFit_bootstrap_bins-count=200_resample-size=1200000.csv",
              "zFAS_obj0_fails_and_lsFit_bootstrap_bins-count=200_resample-size=1471840.csv",
              "zFAS_obj0_fails_and_lsFit_bootstrap_bins-count=200_resample-size=1800000.csv"]

data_paths = ["zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=5000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=10000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=15000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=20000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=25000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=30000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=35000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=38743.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=45000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=50000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=55000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=60000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=65000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=70000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=75000.csv",
              "zFAS_obj0_fog_fails_and_lsFit_bootstrap_bins-count=200_resample-size=80000.csv"]

data_size = [300000, 600000, 900000, 1200000, 1500000, 1800000]
data_size = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 38743, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]

full_data_paths = glob.glob(dir_path + "snow_data\\*.csv")
full_data_paths.sort(key=os.path.getmtime)
data_size = [int(k.split("=")[2][:-4]) for k in full_data_paths]

data = []
conf_int_low = []
conf_int_high = []
conf_int_width = []

# for data_ctr in range(len(data_paths)):
#     curr_file_path = dir_path + data_paths[data_ctr]
data_ctr = 0
for curr_file_path in full_data_paths:
    in_file = open(curr_file_path, "r")
    data_lines = in_file.readlines()
    del data_lines[0]
    data.append([])

    # print("reading file: " + str(curr_file_path))

    for l in data_lines:
        curr_value = float(l.split(",")[0])
        data[data_ctr].append(curr_value)

    in_file.close()
    data[data_ctr] .sort()
    curr_two_and_half_percent_count = round(0.025 * len(data[data_ctr]))
    conf_int_low.append(data[data_ctr][curr_two_and_half_percent_count])
    conf_int_high.append(data[data_ctr][len(data[data_ctr])-curr_two_and_half_percent_count])
    conf_int_width.append(conf_int_high[data_ctr] - conf_int_low[data_ctr])
    print(data_size[data_ctr], conf_int_width[data_ctr])
    data_ctr += 1


plt.figure(1, figsize=(10, 5))
plt.plot(data_size, conf_int_width)
plt.show()

# color_names = ['r', 'g', 'b', 'm', "c", 'grey']
# bins_count = 50
# plt.figure(1, figsize=(10, 5))
# plt.hist(data, zorder=1, bins=bins_count, alpha=1.0, stacked=True, density=True)
# for data_ctr in range(len(data_paths)):
#     #plt.hist(data[data_ctr], zorder=1, bins=bins_count, alpha=1.0, color='w', edgecolor=color_names[data_ctr], stacked=True)
#     plt.axvline(x=conf_int_low[data_ctr], color=color_names[data_ctr])
#     plt.axvline(x=conf_int_high[data_ctr], color=color_names[data_ctr])
# plt.show()
