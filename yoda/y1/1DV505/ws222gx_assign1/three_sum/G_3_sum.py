from algorithms.bf import brute_force
from utils.linear_regression import linear_reg_run
from utils.testing import benchmark_function, fluctuations
from utils.plotting import make_plot


range_values = (50, 700, 50)
avg_times_bf, size_lst = benchmark_function(brute_force, range_values, 5)

fluctuations(brute_force, "Brute force", range_values, 3)

avg_times = [avg_times_bf]

make_plot("List size", "Time in seconds", size_lst, avg_times,
          ["Brute force"], "Average time brute force")


linear_reg_run(size_lst, avg_times_bf, "Brute force")
