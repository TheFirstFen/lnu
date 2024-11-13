import time
import matplotlib.pyplot as plt
from algorithms.bf import brute_force
from algorithms.two_pointer import two_pointer
from algorithms.caching import caching
from utils.linear_regression import find_m_k
import math


def log_time(size_lst, exponent):
    time_values = [size**exponent for size in size_lst]
    log_t = [math.log(i) if i > 0 else 0 for i in time_values]
    log_n = [math.log(i) if i > 0 else 0 for i in size_lst]
    return log_n, log_t


def benchmark_function(test_func, target=20, min_size=0, max_size=100,
                       step=10, trials=5):

    size_lst = list(range(min_size, max_size + 1, step))
    avg_times = []

    for size in size_lst:
        times = []
        lst = list(range(1, size + 1))

        for trial in range(trials):
            start_time = time.time()
            test_func(lst, target)
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)

        avg_time = sum(times) / trials
        avg_times.append(avg_time)
        target += 10

    return avg_times, size_lst


labels = ["Brute force", "Two pointer", "Caching"]

avg_times_bf, size_lst = benchmark_function(brute_force)
# avg_times_tP, size_lst = benchmark_function(two_pointer)
# avg_times_ch, size_lst = benchmark_function(caching)

print("Brute force:", avg_times_bf[-1])
# print("Two pointer:", avg_times_tP[-1])
# print("Caching:", avg_times_ch[-1])

log_n, log_t = log_time(size_lst, 3)  # 3 because it is a O(n³)
k, m = find_m_k(log_t, log_n)
line_y = [k*x + m for x in log_n]

print(k)

# both caching and 2 pointer approach is O(n²) thus
log_n_ch_tp, log_t_ch_tp = log_time(size_lst, 2)


# finds the max values to make the plot even
# max_val = max(max(log_n_bf), max(log_t_bf), max(log_n_ch_tp), max(log_t_ch_tp))

# plt.plot(size_lst, avg_times_bf, "-+r", label=labels[0])
plt.plot(log_n, log_t, "+b", label=f"log(n) vs log(t)")
plt.plot(log_t, line_y, "r")

plt.xlabel("log(n) size")
plt.ylabel("log(t) time")
plt.legend()
plt.show()




































































# VILL INTE SE SKITEN så länge
# plt.plot(size_lst, avg_times_tP, "-+b", label=labels[1])
# plt.plot(size_lst, avg_times_ch, "-+y", label=labels[2])

# plt.plot(log_n_bf, log_t_bf, "r", label="O(n²): log(n) vs log(t)")
# plt.plot(log_n_ch_tp, log_t_ch_tp, "b", label="O(n³): log(n) vs log(t)")

# plt.xlim(0, max_val)
# plt.ylim(0, max_val)