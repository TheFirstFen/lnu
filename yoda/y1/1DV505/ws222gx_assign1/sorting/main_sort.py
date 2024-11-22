from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.selection_sort import selection_sort
from sort_algorithms.insertion_sort import insertion_sort
from utils.plotting import make_plot
from utils.test_sort import test_algorithm
from utils.linear_regression import linear_reg_run

range_values = (100, 6500, 100)
trials = 5

n2_sort_times, sizes = test_algorithm([bubble_sort, selection_sort,
                                      insertion_sort], trials, range_values)


labels = ["Selection sort", "Insertion sort", "Bubble sort"]

linear_results = linear_reg_run(sizes, n2_sort_times, labels)
make_plot("List size", "Time result", "Average time", n2_sort_times, labels,
          size=sizes)

make_plot("List size", "Time result", "Time complexity with log-log plots",
          linear_results, labels, True)
