import time
import matplotlib.pyplot as plt
from algorithms.bf import brute_force
from algorithms.two_pointer import two_pointer
from algorithms.caching import caching
from utils.linear_regression import line_reg, log_values


def benchmark_function(test_func):

    target = 20
    min_size, max_size, step = 50, 10_000, 1000
    trials = 5

    size_lst = list(range(min_size, max_size, step))
    avg_times = []

    for size in size_lst:
        print("Current run:", size)
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



labels = ["", "Caching"]

# avg_times_bf, size_lst = benchmark_function(brute_force)
avg_times_tP, size_lst = benchmark_function(two_pointer)
# avg_times_ch, size_lst = benchmark_function(caching)

# print("Brute force:", avg_times_bf[-1])
# print("Two pointer:", avg_times_tP[-1])
# print("Caching:", avg_times_ch[-1])fluctuates


log_x, log_y = log_values(size_lst, avg_times_tP)
k, m, line_y = line_reg(log_x, log_y)
rounded_k = round(k, 3)

print(f"Expceted k value around 3\nComputated k value: {rounded_k}")

plt.plot(log_x, log_y, "+b", label="log(n) vs log(t)")
plt.plot(log_x, line_y, "r", label=f"kx + m\nk value = {rounded_k}")

plt.xlabel("log(n) size")
plt.ylabel("log(t) time")
plt.legend()
plt.show()




# plt.plot(size_lst, avg_times_tP, "-+b", label=labels[0])
# plt.plot(size_lst, avg_times_ch, "-+y", label=labels[1])
plt.plot(size_lst, avg_times_tP, "-+r", label="Caching force")
plt.xlabel("List sizes")
plt.ylabel("Time in seconds(s)")
plt.title("Linear regression log(n) vs log(t)")
plt.legend()
plt.show()

"""
for i in range(3):
    avg_times_bf, size_lst = benchmark_function(brute_force)
    plt.plot(size_lst, avg_times_bf, "+", label=f"Run {i+1}")

plt.legend()
plt.xlabel("List sizes")
plt.ylabel("Time in seconds(s)")
plt.show()
"""


# finds the max values to make the plot even
# max_val = max(max(log_n_bf), max(log_t_bf), max(log_n_ch_tp), max(log_t_ch_tp))

# plt.plot(size_lst, avg_times_bf, "-+r", label=labels[0])




































































