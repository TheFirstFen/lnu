"""
These algorithms were copied from a1 as using the sys command proved
unreliable thus i duplicated the sorting algorithms to this lecture
"""
import heap.heap_sort as hp
import sorting_algorithms.quick_sort as qs
import sorting_algorithms.merge_sort as ms
from utils.benchmark import test_algorithm
from utils.plotting import make_plot

# basic running of the algorithms and plotting for them
algorithms = [qs.quick_sort, ms.merge_sort, hp.heap_sort]
labels = ["Quick sort", "Merge sort", "Heap sort"]
results, sizes = test_algorithm(algorithms, 5, (0, 30_000, 1000), False)
make_plot(results, sizes, labels)
