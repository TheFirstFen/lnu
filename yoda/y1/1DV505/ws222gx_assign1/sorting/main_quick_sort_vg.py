"""
COMMENT: Expected result: first test should go through the second will
show a plot only for quick sort fast.
Second should give an error because the "left lists" in the algorithm
will be empty there for we will get
recursion error which is expected on the last test for quick sort slow
"""

from sort_algorithms.quick_sort_slow import quick_sort_slow
from sort_algorithms.quick_sort import quick_sort
from utils.plotting import make_plot
from utils.test_sort import test_algorithm

trials = 5
algorithms = [quick_sort, quick_sort_slow]
labels = ["Quick Sort", "Slow Quick Sort"]

# fast vs slow unordered list (small list)
range_values = (0, 2000, 100)
quick_sort_times, sizes = test_algorithm(algorithms, trials, range_values,
                                         False)

make_plot("Number sorted", "Time in seconds",
          "Randomly ordered list", quick_sort_times,
          labels=labels, size=sizes)


# Flaw in slow quick sort
print("Flaw detected")
range_values = (0, 2000, 250)
quick_sort_times, sizes = test_algorithm(algorithms, trials, range_values,
                                         True)
