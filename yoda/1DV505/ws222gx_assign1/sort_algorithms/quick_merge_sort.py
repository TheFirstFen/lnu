from log_sort.merge_sort import merge_sort
from log_sort.quick_sort_slow import quick_sort_slow

from utils.plotting import make_plot
from utils.test_sort import test_algorithm

start, stop, step = 0, 100_000, 2000
trials = 5

n2_sort_times, sizes = test_algorithm([quick_sort_slow, merge_sort],
                                      trials=trials, begin=start, stop=stop, 
                                      step=step)

# print(n2_sort_times[0])
# print(n2_sort_times[1])

labels = ["Quick sort", "Merge sort"]
make_plot("Size", "Time (s)", sizes, n2_sort_times,  labels)
