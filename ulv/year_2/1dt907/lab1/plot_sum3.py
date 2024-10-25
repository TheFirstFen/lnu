import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

sum3 = [16.9668, 114.1317, 381.033, 880.8674, 1745.6464, 3018.0189, 1270.1628, 1978.613, 2668.9876, 3747.8984, 4.0912, 33.1559, 113.375, 247.7487, 471.2105, 819.1755, 1349.169, 1887.6059, 2662.266, 3636.2751, 4.2966, 33.0056, 108.6279, 246.5941, 489.9892, 853.4465, 1281.8797, 1870.3615, 2730.397, 3673.7304, 4.7349, 35.6495, 112.0916, 252.2281, 492.9955, 806.9612, 1272.4762, 1934.4337, 2652.5325, 3651.7732, 4.0885, 32.7407, 109.2355, 264.0834, 471.8088, 821.9324, 1271.6019, 1949.2431, 2632.3199, 3681.4237, 5.5225, 35.0493, 113.3697, 250.1829, 472.8654, 811.7497, 1323.3977, 1866.7491, 2766.9657, 3637.1608, 4.7924, 37.7414, 117.601, 258.8323, 542.9613, 830.4462, 1270.819, 1869.0107, 2733.0023, 3708.7759, 4.116, 33.1561, 108.2687, 248.2034, 472.9898, 820.834, 1264.8769, 1957.7358, 2657.0091, 3712.4308, 4.7393, 33.0947, 106.8482, 250.6147, 484.4523, 810.5276, 1394.8407, 1986.115, 2732.882, 3695.8157, 4.109, 33.7136, 110.5657, 253.5378, 498.0691, 863.2911, 1300.2774, 1875.3452, 2737.0727, 3633.2545]

sum32point = [2.7822, 2.1983, 9.3253, 6.139, 9.2924, 13.4173, 20.9374, 25.987, 32.0801, 38.5199, 0.4897, 1.3699, 2.9544, 5.3652, 8.0156, 12.1531, 16.1786, 22.0585, 30.2228, 32.8461, 0.3335, 1.4736, 2.9652, 5.3135, 8.3691, 12.1427, 17.9647, 20.4602, 26.2937, 35.3045, 0.3747, 1.3806, 3.0815, 5.3701, 9.2897, 12.0669, 15.7859, 23.4305, 25.8433, 33.5583, 0.6798, 1.2771, 3.3921, 8.7391, 8.2052, 11.6352, 16.6965, 20.8673, 27.4657, 33.2613, 0.3408, 1.4441, 2.8684, 5.3299, 8.2875, 11.3643, 16.2663, 22.2655, 30.9956, 34.3733, 0.4194, 1.4896, 3.0194, 5.5421, 8.2877, 11.7905, 16.9402, 21.9664, 28.1797, 35.1535, 0.3611, 1.4902, 3.1237, 5.2856, 8.3408, 11.6111, 15.658, 22.6824, 30.393, 33.3643, 0.6287, 1.5314, 2.9854, 5.3185, 8.8881, 11.7122, 18.0149, 22.2572, 29.876, 33.7197, 0.3333, 1.4704, 3.103, 5.1787, 8.0068, 14.0274, 17.0888, 23.2302, 28.4099, 33.8654]

element = 10

def fitted_curve(x, a, b):
    return a * x**b

def computed_curve(x, a, b):
    return (np.array(x) * 2**(a / b))**b

def plot_and_fit(x_data, y_data, label, fit_function, params, element, linestyle):
    plt.scatter(x_data[:element], y_data, label=f'{label} Original', marker='o')
    plt.plot(x_data[:element], fit_function(x_data[:element], *params), linestyle, label=f'{label} Fit (a={params[0]:.2f}, b={params[1]:.2f})')

num_plots = len(sum3) // element

print("| Plot | sum3 a fitted | sum3 b fitted | sum3 a computed | sum3 b computed |  sum3 two pointer a fitted | sum3 two pointer b fitted | sum3 two pointer a computed | sum3 two pointer b computed |")
print("|------|---------------|---------------|-----------------|-----------------|----------------------------|---------------------------|-----------------------------|---------------------------- |")


for i in range(num_plots):
    start_id = i * element
    end_id = start_id + element

    # Fitting the curve to sum3 data
    params_sum3, _ = curve_fit(fitted_curve, x[:element], sum3[start_id:end_id])
    params_sum3_computed, _ = curve_fit(computed_curve, x[:element], sum3[start_id:end_id])

    # Fitting the curve to sum3 two-pointer data
    params_sum3_2p, _ = curve_fit(fitted_curve, x[:element], sum32point[start_id:end_id])
    params_sum3_2p_computed, _ = curve_fit(computed_curve, x[:element], sum32point[start_id:end_id])

    print(f"| {i + 1:<4} | {params_sum3[0]:.2f}          | {params_sum3[1]:.2f}          | {params_sum3_computed[0]:.2f}          | {params_sum3_computed[1]:.2f}             | " +
          f"{params_sum3_2p[0]:.2f}                       | {params_sum3_2p[1]:.2f}                     | {params_sum3_2p_computed[0]:.2f}                      | {params_sum3_2p_computed[1]:.2f}                 qq      |")



    # Plotting the original data and the fitted curves
    plot_and_fit(x, sum3[start_id:end_id], 'sum3', fitted_curve, params_sum3, element, '--')
    plot_and_fit(x, sum3[start_id:end_id], 'sum3', computed_curve, params_sum3_computed, element, '-')

    plot_and_fit(x, sum32point[start_id:end_id], 'sum3 two pointer', fitted_curve, params_sum3_2p, element, '--')
    plot_and_fit(x, sum32point[start_id:end_id], 'sum3 two pointer', computed_curve, params_sum3_2p_computed, element, '-')

    plt.xlabel('amount of elements')
    plt.ylabel('Time (milliseconds)')
    plt.legend()
    plt.show()
