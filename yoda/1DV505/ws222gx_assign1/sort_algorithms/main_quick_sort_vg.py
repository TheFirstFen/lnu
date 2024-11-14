from log_sort.quick_sort_slow import quick_sort_slow
from log_sort.quick_sort import quick_sort

from utils.plotting import make_plot
from utils.test_sort import test_algorithm

start, stop, step = 1_000_000, 7_000_000, 1_000_000
trials = 3


quick_sort_times, sizes = test_algorithm(quick_sort, quick_sort_slow,
                                         trials=trials, begin=start, stop=stop,
                                         step=step)


print("Quick Sort Time:", quick_sort_times[0][-1])
print("Slow Quick Sort Time:", quick_sort_times[1][-1])

# labels for each algorithm
labels = ["Quick Sort", "Slow Quick Sort"]

make_plot("Number sorted", "Time in seconds",
          quick_sort_times,
          labels=labels, size=sizes)
