import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

UF = [138.9081, 289.4722, 496.712, 613.6678, 759.3135, 1151.4298, 1884.0646, 2666.2219, 3240.5701, 299.9637, 587.0532, 908.2133, 1210.4905, 1581.5702, 2088.6219, 2928.7795, 3826.9374, 4551.8938, 477.0312, 987.4022, 1448.0341, 1911.2313, 2351.8321, 2913.3186, 3963.033, 4955.5304, 5472.8949, 601.1442, 1252.5543, 1749.2413, 2397.9209, 2952.229, 3717.7634, 4971.4248, 6209.9347, 7003.932, 797.5033, 1521.8169, 2355.0839, 3138.815, 3979.347, 4833.0438, 6197.3846, 7289.7807, 8118.3614, 945.5566, 1872.7626, 2848.4117, 3820.5867, 4823.969, 5959.7781, 7497.5593, 8786.1379, 9485.4298, 1119.0343, 2162.8478, 3294.955, 4328.108, 5529.6256, 7028.656, 8538.4224, 9871.9793, 10704.2586, 1220.7946, 2491.0277, 3619.4225, 4805.5973, 5898.6319, 7151.2541, 9480.7006, 11120.1281, 12047.6322, 1376.8089, 2716.1459, 4185.8002, 5451.919, 7017.6475, 8796.1647, 10771.7907, 12435.7852, 13607.1288]

WQUF = [1.6866, 0.7157, 1.5401, 1.6191, 2.0231, 9.1617, 92.6887, 311.1436, 645.8135, 0.3493, 0.4464, 0.6967, 1.032, 1.5427, 11.5221, 90.9915, 325.9956, 686.6072, 0.2411, 0.4686, 0.7548, 0.9814, 1.5484, 9.0967, 104.7103, 322.7142, 663.8989, 0.2342, 0.4326, 0.8647, 1.0028, 1.4066, 6.6864, 92.6178, 311.2668, 657.8237, 0.3154, 0.495, 0.7197, 1.0242, 1.4755, 7.5921, 95.1274, 295.311, 639.5703, 0.2717, 0.4684, 0.7217, 0.9777, 1.4282, 8.9439, 94.2215, 327.6406, 664.688, 0.2784, 0.5417, 0.7196, 1.3166, 1.4063, 10.2523, 90.9684, 302.7965, 672.6987, 0.2709, 0.4668, 0.7408, 1.0388, 1.5325, 8.9481, 87.926, 304.0819, 647.6537, 0.3173, 0.8825, 0.8168, 1.1116, 1.4744, 6.5056, 93.6685, 334.8278, 620.0973]

x = [10_000, 20_000, 30_000, 40_000, 50_000, 60_000, 70_000, 80_000, 90_000]
def linmod(x, m, b):
    x = np.array(x)
    return m * x + b

element = 9
num_plots = len(UF) // element

uf_slopes = []
uf_intercepts = []
wquf_slopes = []
wquf_intercepts = []

for i in range(num_plots):
    start_id = i * element
    end_id = start_id + element

    params_uf, _ = curve_fit(linmod, x[:element], UF[start_id:end_id])
    uf_slopes.append(params_uf[0])
    uf_intercepts.append(params_uf[1])

    params_wquf, _ = curve_fit(linmod, x[:element], WQUF[start_id:end_id])
    wquf_slopes.append(params_wquf[0])
    wquf_intercepts.append(params_wquf[1])
    
    plt.scatter(x[:element], UF[start_id:end_id], label='UF')
    plt.plot(x[:element], linmod(x[:element], *params_uf), '--', label=f'UF Fit (m={params_uf[0]:.2f}, b={params_uf[1]:.2f})')

    plt.scatter(x[:element], WQUF[start_id:end_id], label='WQUF')
    plt.plot(x[:element], linmod(x[:element], *params_wquf), '--', label=f'WQUF Fit (m={params_wquf[0]:.2f}, b={params_wquf[1]:.2f})')

    plt.xlabel('Amount of unions')
    plt.ylabel('Time (milliseconds)')
    plt.title(f'Amount of elements in Array {100000 + i * 100000}')
    plt.legend()
    plt.show()

print("| Plot | UF Slope (m)| UF Intercept (b)   | WQUF Slope (m) | WQUF Intercept (b)    |")
print("|------|-------------|---------------------|---------------|-----------------------|")
for i in range(num_plots):
    print(f"| {i + 1}    | {uf_slopes[i]:.2f}        | {uf_intercepts[i]:.2f}             | {wquf_slopes[i]:.2f}          | {wquf_intercepts[i]:.2f}               |")