def partion_lst(lst):
    pivot_element = lst[0]
    left_lst = []
    right_lst = []

    for i in range(1, len(lst)):
        if pivot_element > lst[i]:
            right_lst += [lst[i]]
        else:
            left_lst += [lst[i]]
    return pivot_element, left_lst, right_lst


def quick_sort_slow(lst):
    if len(lst) <= 1: # already sorted
        return lst
    pivot_element, left_lst, right_lst = partion_lst(lst)
    left_sorted = quick_sort(left_lst)
    right_sorted = quick_sort(right_lst)
    return right_sorted + [pivot_element] + left_sorted


