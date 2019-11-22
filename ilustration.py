import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fog_data_x = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 38743, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]
fog_data_y = [0.021199999999999997, 0.014900000000000024, 0.012199999999999989, 0.010249999999999981, 0.009280000000000066, 0.0086666666666666, 0.008000000000000007,
              0.007665900936943415, 0.00691111111111109, 0.006619999999999959, 0.006418181818181878, 0.005850000000000022, 0.005569230769230771, 0.005742857142857161,
              0.005360000000000031,0.005099999999999993]

snow_data_x = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20814, 22000, 24000, 26000, 28000, 30000, 32000, 34000, 36000, 38000, 40000, 42000]
snow_data_y = [0.04200000000000004, 0.030000000000000027, 0.024666666666666615, 0.02112500000000006, 0.019199999999999995, 0.01708333333333334, 0.015928571428571403, 0.015249999999999986,
               0.014000000000000012, 0.01297203805131164, 0.01295454545454544, 0.012166666666666659, 0.011538461538461497, 0.011285714285714343, 0.01090000000000002, 0.010624999999999996,
               0.010294117647058898, 0.009888888888888947, 0.009842105263157874, 0.009375000000000022, 0.009047619047619082]


snow_past_x = snow_data_x[0:10]
snow_past_y = snow_data_y[0:10]
snow_prognosis_x = snow_data_x[9:21]
snow_prognosis_y = snow_data_y[9:21]

fog_past_x = fog_data_x[0:7]
fog_past_y = fog_data_y[0:7]
fog_prognosis_x = fog_data_x[6:16]
fog_prognosis_y = fog_data_y[6:16]


fig, ax = plt.subplots(1, figsize=(10, 5))
ax.plot(snow_past_x, snow_past_y, color="peru", linewidth=2, label="snow data, obtained")
ax.plot(snow_prognosis_x, snow_prognosis_y, color="peru", dashes=[3, 1], linewidth=2, label="snow data, prognosis")
ax.plot(fog_past_x, fog_past_y, color="dodgerblue", linewidth=2, label="fog data, obtained")
ax.plot(fog_prognosis_x, fog_prognosis_y, color="dodgerblue", dashes=[3,1], linewidth=2, label="fog data, prognosis")

f = ticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos: "${}$".format(f._formatSciNotation('%1.10e' % x))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.xaxis.set_major_formatter(ticker.FuncFormatter(g))
plt.grid(alpha=0.2, which='minor')
plt.grid(alpha=0.5, which='major')
plt.xlim((0, 82000))
ax.legend(loc='upper right', fontsize='12', framealpha=1.0, labelspacing=0.7, handletextpad=1.2, borderaxespad=1, borderpad=1.0)
ax.set_xlabel("number of data frames", fontsize=12)
ax.set_ylabel("confidence interval width", fontsize=12)
ax.tick_params(labelsize=12)
fig.suptitle("Audi zFAS confidence intervals widths for obj_0 IoU performance", fontsize=16)
plt.show()
