from log_sort.quick_sort_slow import quick_sort_slow
from log_sort.quick_sort import quick_sort

from utils.plotting import make_plot
from utils.test_sort import test_algorithm

range_values = (0, 1000, 100)
trials = 3


quick_sort_times, sizes = test_algorithm(quick_sort, quick_sort_slow,
                                         trials, range_values)

# labels for each algorithm
labels = ["Quick Sort", "Slow Quick Sort"]

make_plot("Number sorted", "Time in seconds", "Average time", quick_sort_times,
          labels=labels, size=sizes)
