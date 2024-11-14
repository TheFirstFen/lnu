def half_lsts(lst):
    half_values = (len(lst) // 2)

    left_lst = lst[0:half_values]
    right_lst = lst[half_values::]

    return left_lst, right_lst


def merge(left, right):
    finished_lst = []
    i = j = 0   # i = left, right = j

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            finished_lst += [left[i]]
            i += 1
        else:
            finished_lst += [right[j]]
            j += 1

    while i < len(left):
        finished_lst += [left[i]]
        i += 1

    while j < len(right):
        finished_lst += [right[j]]
        j += 1

    return finished_lst


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left_lst, right_lst = half_lsts(lst)

    left_sorted = merge_sort(left_lst)
    right_sorted = merge_sort(right_lst)

    return merge(left_sorted, right_sorted)
