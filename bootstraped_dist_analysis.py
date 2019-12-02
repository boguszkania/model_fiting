import numpy as np
import os
import glob
import matplotlib.pyplot as plt

dir_path = "C:\\Users\\ljxx5v\\Desktop\\"

full_data_paths = glob.glob(dir_path + "early_prog\\second_try\\*.csv")
full_data_paths.sort(key=os.path.getmtime)
data_size = [int(k.split("=")[2][:-4]) for k in full_data_paths]

data = []
conf_int_low = []
conf_int_high = []
conf_int_width = []


data_ctr = 0
for curr_file_path in full_data_paths:
    in_file = open(curr_file_path, "r")
    data_lines = in_file.readlines()
    del data_lines[0]
    data.append([])

    for l in data_lines:
        curr_value = float(l.split(",")[0])
        data[data_ctr].append(curr_value)

    in_file.close()
    data[data_ctr].sort()
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
