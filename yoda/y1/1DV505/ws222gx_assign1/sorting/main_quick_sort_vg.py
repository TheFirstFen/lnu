"""
1. Test shows that both algorithms work
2. This test will show that quick sort fast does work with a reversed ordered
list.
3. Test is expected to fail and give an error because it will show the flaw in
having the pivot element as the first element rather than the median

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

make_plot("Numbers sorted", "Time in seconds",
          "Randomly ordered list", quick_sort_times,
          labels=labels, size=sizes)


range_values = (0, 2000, 250)
quick_sort_times, sizes = test_algorithm([algorithms[0]], trials, range_values,
                                         True)
make_plot("Numbers sorted", "Time in seconds", "Reversed ordered list for fast"
          " quick sort",  quick_sort_times, labels=labels, size=sizes)


print("Flaw detected: <- intentional")
quick_sort_times, sizes = test_algorithm([algorithms[1]], trials, range_values,
                                         True)
