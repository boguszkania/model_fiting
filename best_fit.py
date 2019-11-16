import matplotlib.pyplot as plt
import scipy.stats as st
import statsmodels as sm

data_path = "C:\\Bogusz\\aptiv_data\\tmp_zFAS_obj0.csv"
data = []
in_file = open(data_path, "r")
data_lines = in_file.readlines()
del data_lines[0]

for l in data_lines:
    curr_value = float(l.split(",")[2])
    if curr_value > 0:
        data.append(curr_value)

print("data loaded")
# ================================================================================

fig1, ax1 = plt.subplots(1,1, figsize=(12, 7))
ax1.tick_params(labelsize=16)
ax1.hist(data, bins=60, color="tab:blue", edgecolor="black", density=True)
ax1.tick_params(labelsize=16)


dist_names = ['weibull_min', 'johnsonsb', 'johnsonsu', 'powerlognorm']
dist_colors = ['green', 'red', 'brown', 'blue']
dist_starting_params = [{'fc':48365484.0, 'loc':-7508141.0, 'fscale':7508142.0},
                        {'fa':-1.03170883118204, 'fb':0.9944411963180599, 'floc':-0.09737034010334855, 'scale':1.0973928986180872},
                        {'fa':8.10184617181027, 'fb':1.9292029872102514, 'floc':1.0755983637699007, 'scale':0.010590720938423531},
                        {'fc':292.428463579101, 'fs':0.07368530357323744, 'floc':-6.899180096665539, 'scale':9.671250512347605}]


ctr = 0
for dist_name in dist_names:
    dist = getattr(st, dist_name)
    print(dist)
    param = dist.fit(data, **dist_starting_params[ctr])
    print(param)
    pdf_fitted = [dist.pdf(k/100, *param[:-2], loc=param[-2], scale=param[-1]) for k in range(100)]
    ax1.plot([k/100 for k in range(100)], pdf_fitted, label=dist_name, color=dist_colors[ctr], linewidth=3)
    ctr += 1

ax1.set_xlabel("IoU results", fontsize=16)
ax1.set_ylabel("data density", fontsize=16)
plt.legend(loc='upper left', fontsize=16)
plt.suptitle("Example of model search for performance data", fontsize=18)
plt.show()



# fig1, ax1 = plt.subplots(1,1, figsize=(12, 7))
# ax1.tick_params(labelsize=16)
# ax1.hist(data, bins=60, color="tab:blue", edgecolor="black")
# plt.show()