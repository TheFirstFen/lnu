from sort_algorithms.quick_sort_slow import quick_sort_slow
from sort_algorithms.quick_sort import quick_sort
from utils.plotting import make_plot
from utils.test_sort import test_algorithm

"""COMMENT: Test shows when quick sort fast is faster the slow quick sort"""
range_values = (6_000_000, 13_000_000, 1_000_000)

trials = 5
algorithms = [quick_sort, quick_sort_slow]

quick_sort_times, sizes = test_algorithm(algorithms,
                                         trials, range_values)

# labels for each algorithm
labels = ["Quick Sort", "Slow Quick Sort"]

make_plot("Number sorted", "Time in seconds", "Average time", quick_sort_times,
          labels=labels, size=sizes)


# reversed ordered list
"""
COMMENT: exceeding a almost sorted list of size 2000 will yield recursion error
for slow quick sort because of how the pivot element acts around almost sorted
list the test below also shows that fast quick sort is faster at 2000, the test
under that will give out an error for 2001 which shows the flaw of quick sort
slow. The error that shows is: RecursionError: maximum recursion depth exceeded

"""
range_values = (0, 2000, 250)
quick_sort_times, sizes = test_algorithm(algorithms, trials, range_values,
                                         True)
make_plot("Number sorted", "Time in seconds",
          "Reversed ordered list average times", quick_sort_times,
          labels=labels, size=sizes)


print("Flaw detected")
range_values = (0, 2001, 250)
quick_sort_times, sizes = test_algorithm(algorithms, trials, range_values,
                                         True)
