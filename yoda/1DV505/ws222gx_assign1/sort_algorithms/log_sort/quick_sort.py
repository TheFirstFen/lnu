
def sort_pivot(lst):
    if lst[0] > lst[1]:
        lst[0], lst[1] = lst[1], lst[0]
    if lst[1] > lst[2]:
        lst[1], lst[2] = lst[2], lst[1]
    if lst[0] > lst[1]:
        lst[0], lst[1] = lst[1], lst[0]
    return lst


def pivot_median(lst):
    return sort_pivot([lst[0], lst[(len(lst) // 2)], lst[-1]])[1]


def partion_lst(lst):
    pivot_element = pivot_median(lst)
    left_lst = []
    right_lst = []

    for i in range(len(lst)):
        if pivot_element > lst[i]:
            left_lst.append(lst[i])
        elif pivot_element < lst[i]:
            right_lst.append(lst[i])

    return pivot_element, left_lst, right_lst


def quick_sort(lst):
    if len(lst) <= 1: # already sorted
        return lst
    pivot_element, left_lst, right_lst = partion_lst(lst)
    left_sorted = quick_sort(left_lst)
    right_sorted = quick_sort(right_lst)
    return left_sorted + [pivot_element] + right_sorted

