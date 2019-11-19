import numpy as np
from scipy.optimize import curve_fit

def johnson_sb(gam, dlt, lam, ksi, x):
    z = (x - ksi) / lam
    left_part = dlt/(lam*np.sqrt(2.0 * np.pi) * np.sqrt((z*z) + 1.0))
    right_part = np.exp(-0.5 * np.square(gam + dlt * np.log(z + np.sqrt((z*z) + 1))))
    return left_part * right_part


def fit_model(data_2d, function):
    xs = np.array([line[0] for line in data_2d])
    ys = np.array([line[1] for line in data_2d])

    popt, pcov = curve_fit(function, xs, ys)
    unct = np.sqrt(np.diag(pcov))
    return popt, unct

# =====================================================================================================================
data_path = "C:\\Users\\ljxx5v\\Desktop\\tmp_zFAS_obj0.csv"
data = []

in_file = open(data_path, "r")
data_lines = in_file.readlines()
del data_lines[0]

for l in data_lines:
    curr_value = float(l.split(",")[2])
    if curr_value > 0:
        data.append(curr_value)

print("data loaded")
print(fit_model(johnson_sb))


