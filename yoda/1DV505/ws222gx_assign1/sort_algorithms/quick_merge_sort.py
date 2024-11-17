from log_sort.merge_sort import merge_sort
from log_sort.quick_sort_slow import quick_sort_slow

from utils.plotting import make_plot
from utils.test_sort import test_algorithm

range_values = (0, 1000, 100)
trials = 5

n2_sort_times, sizes = test_algorithm([quick_sort_slow, merge_sort],
                                      trials, range_values)


labels = ["Quick sort", "Merge sort"]
make_plot("Size", "Time (s)", "Average time", n2_sort_times,  labels,
          size=sizes)
