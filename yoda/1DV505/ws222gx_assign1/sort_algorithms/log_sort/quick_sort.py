import random


def sort_pivot(lst):    # bubble sort casue it is only 3 elements
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def pivot_median(lst):
    left = lst[0]
    right = lst[-1]
    middle = lst[(len(lst) // 2)]


    return sort_pivot([left, middle, right])[1]

def partion_lst(lst):
    pivot_element = pivot_median(lst)
    left_lst = []
    right_lst = []

    for i in range(len(lst)):
        if pivot_element > lst[i]:
            left_lst += [lst[i]]
        elif pivot_element < lst[i]:
            right_lst += [lst[i]]
    return pivot_element, left_lst, right_lst


def quick_sort(lst):
    if len(lst) <= 1: # already sorted
        return lst
    pivot_element, left_lst, right_lst = partion_lst(lst)
    left_sorted = quick_sort(left_lst)
    right_sorted = quick_sort(right_lst)
    return left_sorted + [pivot_element] + right_sorted


lst = []

for i in range(10):
    lst.append(random.randint(1, 100))

print(lst)
print(quick_sort(lst))
