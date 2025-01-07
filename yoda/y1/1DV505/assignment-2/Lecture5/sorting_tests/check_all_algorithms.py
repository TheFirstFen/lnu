"""
These algorithms were brought from a1 as using the sys command proved
unreliable i duplicated the sorting algorithms to this lecture
"""
from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.insertion_sort import insertion_sort
from sort_algorithms.selection_sort import selection_sort

from sort_algorithms.quick_sort import quick_sort
from sort_algorithms.quick_sort_slow import quick_sort_slow
from sort_algorithms.merge_sort import merge_sort

import test_sorting as ts
import pytest


sorting_algorithms = [bubble_sort, insertion_sort, selection_sort,
                      quick_sort, quick_sort_slow, merge_sort]


# decorator to be able to run every sorting algorithm with the pytest
@pytest.mark.parametrize("func", sorting_algorithms)
def test_sorting_algorithms(func):
    ts.test_sort_base_case(func)
    ts.test_sort_ordered(func)
    ts.test_sort_random_ordered(func)
    ts.test_sort_duplicates(func)
    ts.test_same_elements(func)
    ts.test_above_base_case(func)
    ts.test_float_values(func)
    ts.test_negative_values(func)
