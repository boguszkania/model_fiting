import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def johnson_sb(x, gam, dlt, lam, ksi):
    z = (x - ksi) / lam
    left_part = dlt/(lam*np.sqrt(2.0 * np.pi) * np.sqrt((z*z) + 1.0))
    right_part = np.exp(-0.5 * np.square(gam + dlt * np.log(z + np.sqrt((z*z) + 1))))
    return left_part * right_part


def johnson_sb_scaled(x, gam, dlt, lam, ksi, scale):
    z = (x - ksi) / lam
    left_part = dlt/(lam*np.sqrt(2.0 * np.pi) * np.sqrt((z*z) + 1.0))
    right_part = np.exp(-0.5 * np.square(gam + dlt * np.log(z + np.sqrt((z*z) + 1))))
    return scale * left_part * right_part

# =====================================================================================================================


data_path = "C:\\Users\\ljxx5v\\Desktop\\tmp_zFAS_obj0_snow.csv"
output_path = "C:\\Users\\ljxx5v\\Desktop\\early_prog\\"
data = []

in_file = open(data_path, "r")
data_lines = in_file.readlines()
del data_lines[0]

for l in data_lines:
    curr_value = float(l.split(",")[2])
    if curr_value > 0:
        data.append(curr_value)

print("data loaded")

sample_sizes = [500 + 1000*k for k in range(50)]

print(sample_sizes)
exit(0)

for this_resampling_size in sample_sizes:
    bins_count = 200
    resample_count = 10000
    resample_size = this_resampling_size

    output_name = "zFAS_obj0_snow_fails_and_lsFit_bootstrap_bins-count=" + str(bins_count) + "_resample-size=" + str(
        resample_size) + ".csv"
    out_file = open(output_path + output_name, 'w')
 #   out_file.write(
 #       "fraction_of_IoU_over_0.5 johnson_sb_scaled_gam, johnson_sb_scaled_dlt, johnson_sb_scaled_lam, johnson_sb_scaled_ksi, johnson_sb_scaled_scale \n")

    out_file.write(
        "fraction_of_IoU_over_0.5\n")

    for iter_ctr in range(resample_count):
        res_data = np.random.choice(data, size=resample_size)

        bins_edges = np.histogram(res_data, bins=bins_count)[1]
        bins_values = np.histogram(res_data, bins=bins_count)[0]
        bins_values_norm = [k / sum(bins_values) for k in bins_values]
        bins_centers = []

        # for ctr in range(len(bins_edges) - 1):
        #     bins_centers.append(0.5 * (bins_edges[ctr] + bins_edges[ctr + 1]))
        #
        # curr_params, curr_unct = curve_fit(johnson_sb_scaled, bins_centers, bins_values,
        #                                    sigma=[0.1 + (0.9 * k / max(bins_values)) for k in bins_values])
        # # curr_unct = np.sqrt(np.diag(curr_unct))
        # curr_IoU_over_0p5 = len([el for el in res_data if el > 0.5]) / resample_size
        # out_file.write(str(curr_IoU_over_0p5) + "," + str(curr_params[0]) + "," + str(curr_params[1]) + "," + str(
        #     curr_params[2]) + "," + str(curr_params[3]) + "," + str(curr_params[4]) + "\n")

        curr_IoU_over_0p5 = len([el for el in res_data if el > 0.5]) / resample_size
        out_file.write(str(curr_IoU_over_0p5) + "\n")
        if iter_ctr % 100 == 0:
            print("samples count: " + str(iter_ctr))

    out_file.close()



# curr_fitted_curve = [johnson_sb_scaled(cx, *curr_params) for cx in bins_centers]
#
# # plt.hist(data, zorder=0, bins=bins_count)
# plt.figure(1, figsize=(12, 5))
# plt.scatter(bins_centers, bins_values, zorder=1, color='red', s=7)
# plt.plot(bins_centers, curr_fitted_curve)
# plt.show()


