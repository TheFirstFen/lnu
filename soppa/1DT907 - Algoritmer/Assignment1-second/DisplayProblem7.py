import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

sizeAmount = np.array([100, 500, 1000, 2500, 5000, 7500, 10000])
time3sum = np.array([0.007715625, 0.108891459, 0.602767166, 9.167325667, 73.820756459, 252.517078708, 583.159775042])
time3sumcache = np.array([0.00195325, 0.017687792, 0.029005958, 0.189759417, 0.783339083, 1.701242208, 3.341058083])

def power_law(x, a, b):
    return a * x ** b

params_3sum, covariance_3sum = curve_fit(power_law, sizeAmount, time3sum)
params_3sumcache, covariance_3sumcache = curve_fit(power_law, sizeAmount, time3sumcache)

fitted_curve_3sum = power_law(sizeAmount, *params_3sum)
fitted_curve_3sumcache = power_law(sizeAmount, *params_3sumcache)

log_sizeAmount = np.log2(sizeAmount)
log_time3sum = np.log2(time3sum)
log_time3sumcache = np.log2(time3sumcache)

def linear_model(x, b, c):
    return b * x + c

params_3sum_linear, covariance_3sum_linear = curve_fit(linear_model, log_sizeAmount, log_time3sum)
params_3sumcache_linear, covariance_3sumcache_linear = curve_fit(linear_model, log_sizeAmount, log_time3sumcache)

b_3sum_linear, c_3sum_linear = params_3sum_linear
b_3sumcache_linear, c_3sumcache_linear = params_3sumcache_linear

print(f"Growth(b) for 3sum (linear model): {b_3sum_linear}")
print(f"Growth(b) for 3sumcache (linear model): {b_3sumcache_linear}")

fitted_curve_3sum_linear = linear_model(log_sizeAmount, b_3sum_linear, c_3sum_linear)
fitted_curve_3sumcache_linear = linear_model(log_sizeAmount, b_3sumcache_linear, c_3sumcache_linear)

plt.scatter(sizeAmount, time3sum, marker='o', color='blue', label='3sumbruteforce Data')
plt.plot(sizeAmount, fitted_curve_3sum, color='orange', label=f'3sumbruteforce Fit: {params_3sum[0]:.8f} * x^{params_3sum[1]:.2f}')
plt.scatter(sizeAmount, time3sumcache, color='green', marker='o', label='3sumcache Data')
plt.plot(sizeAmount, fitted_curve_3sumcache, color='red', label=f'3sumcache Fit: {params_3sumcache[0]:.8f} * x^{params_3sumcache[1]:.2f}')
plt.title('Fitting 3sumbruteforce and 3sumcache to a*x^b')
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.grid(True)
plt.legend()
plt.show()

plt.scatter(log_sizeAmount, log_time3sum, label='3sumbruteforce Data')
plt.plot(log_sizeAmount, fitted_curve_3sum_linear, label=f'3sumbrutoforce Linear Fit: {b_3sum_linear:.2f} * x + {c_3sum_linear:.2f}')
plt.scatter(log_sizeAmount, log_time3sumcache, label='3sumcache Data')
plt.plot(log_sizeAmount, fitted_curve_3sumcache_linear, label=f'3sumcache Linear Fit: {b_3sumcache_linear:.2f} * x + {c_3sumcache_linear:.2f}')
plt.title('Fitting models to log data')
plt.xlabel('log2(Input Size)')
plt.ylabel('log2(Time)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
