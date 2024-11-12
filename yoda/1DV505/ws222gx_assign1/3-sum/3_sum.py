import time
import matplotlib.pyplot as plt
from algorithms.bf import brute_force
from algorithms.two_pointer import two_pointer
from algorithms.caching import caching
from utils.linear_regression import find_m_k
import math


def benchmark_function(test_func, target=50, min_size=0, max_size=100,
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

k, m = find_m_k(size_lst, avg_times_bf)
k = round(k, 3)
m = round(m, 3)
linear_lst = []
for i in range(len(size_lst)):
    regression = k*i + m
    linear_lst.append(regression)
print(k, m)


log_times = []


for i in avg_times_bf:
    log_times.append(math.log(i))
print(log_times)

plt.plot(size_lst, avg_times_bf, "-+r", label=labels[0])
plt.plot(size_lst, linear_lst, "-+b", label=f"k = {k} m = {m}")
# plt.plot(size_lst, avg_times_tP, "-+b", label=labels[1])
# plt.plot(size_lst, avg_times_ch, "-+y", label=labels[2])
# plt.plot(math.log(len(size_lst)), log_times, label="log")

plt.xlabel("List Size")
plt.ylabel("Average Execution Time (s)")
plt.legend()
plt.show()
