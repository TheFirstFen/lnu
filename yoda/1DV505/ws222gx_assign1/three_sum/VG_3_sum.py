from algorithms.two_pointer import two_pointer
from algorithms.caching import caching
from utils.testing import benchmark_function
from utils.linear_regression import linear_reg_run
from utils.plotting import make_plot

range_values = (10_000, 70_000, 10_000)
avg_times_tP, size_lst = benchmark_function(two_pointer, range_values)
avg_times_ch, size_lst = benchmark_function(caching, range_values)
time_lst = [avg_times_tP, avg_times_ch]

make_plot("list size", "time in seconds", size_lst, time_lst,
          ["Two pointer", "Caching"], "Two pointer vs caching")


linear_reg_run(size_lst, avg_times_tP, "Two pointer")
linear_reg_run(size_lst, avg_times_ch, "Caching")
