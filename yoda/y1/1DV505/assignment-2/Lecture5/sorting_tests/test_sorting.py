import pytest


def test_sort_base_case(func):
    assert func([]) == []
    assert func([1]) == [1]


def test_sort_ordered(func):
    lst = [1, 2, 3, 4, 5]
    assert func(lst) == lst


def test_sort_reversed_ordered(func):
    lst = [5, 4, 3, 2, 1]
    assert func(lst) == lst[::-1]


def test_sort_random_ordered(func):
    lst = [1, 4, 2, 11, 7]
    sorted_lst = [1, 2, 4, 7, 11]
    assert func(lst) == sorted_lst


def test_sort_duplicates(func):
    lst = [2, 2, 1, 3, 1, 1]
    sorted_lst = [1, 1, 1, 2, 2, 3]
    assert func(lst) == sorted_lst


def test_same_elements(func):
    lst = [1, 1, 1, 1]
    assert func(lst) == lst


def test_above_base_case(func):
    lst = [2, 1]
    assert func(lst) == [1, 2]


def test_float_values(func):
    lst = [1.4, 1.3, 2.6, 1.8]
    sorted_lst = [1.3, 1.4, 1.8, 2.6]
    assert func(lst) == sorted_lst


def test_negative_values(func):
    lst = [1, -4, 2, 11, -7]
    sorted_lst = [-7, -4, 1, 2, 11]
    assert func(lst) == sorted_lst
