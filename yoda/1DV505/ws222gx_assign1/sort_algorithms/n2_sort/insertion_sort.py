def insertion_sort(lst):

    if len(lst) <= 1:
        return lst

    for i in range(1, len(lst)):
        second_element = lst[i]
        j = i - 1

        while second_element < lst[j] and j >= 0:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = second_element
    return lst
