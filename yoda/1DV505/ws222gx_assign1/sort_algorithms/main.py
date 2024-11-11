from n2_sort.bubble_sort import bubble_sort
from n2_sort.selection_sort import selection_sort
from n2_sort.insertion_sort import insertion_sort

from log_sort.merge_sort import merge_sort
from log_sort.quick_sort_slow import quick_sort_slow
from log_sort.quick_sort import quick_sort

from utils.plotting import make_plot
from utils.test_sort import test_algorithm

start, stop, step = 0, 1000, 50
trials = 2


quick_sort_times, sizes = test_algorithm(quick_sort, quick_sort_slow, 
                                         trials=trials, begin=start, stop=stop, step=step)


print("Quick Sort Time:", quick_sort_times[0][-1])
print("Slow Quick Sort Time:", quick_sort_times[1][-1])

# labels for each algorithm
labels = ["Quick Sort", "Slow Quick Sort"]

make_plot("Number sorted", "Time in seconds", 
          quick_sort_times[0], quick_sort_times[1], 
          labels=labels, size=sizes)
