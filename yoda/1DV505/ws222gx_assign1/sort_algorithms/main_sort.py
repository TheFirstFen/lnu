from n2_sort.bubble_sort import bubble_sort
from n2_sort.selection_sort import selection_sort
from n2_sort.insertion_sort import insertion_sort
from utils.plotting import make_plot
from utils.test_sort import test_algorithm

start, stop, step = 0, 1000, 100
trials = 10

n2_sort_times, sizes = test_algorithm([selection_sort, insertion_sort,
                                      bubble_sort], trials=trials,
                                      begin=start, stop=stop, step=step)

# print(n2_sort_times[0])
# print(n2_sort_times[1])

labels = ["Selection sort", "Insertion sort", "Bubble sort"]
make_plot("Size", "Time (s)", sizes, n2_sort_times,  labels)
