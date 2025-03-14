def selection_sort(lst):
    # base case already sorted
    if len(lst) <= 1:
        return lst

    for i in range(len(lst)-1):
        smallest = i
        for j in range(i+1, len(lst)):
            if lst[smallest] > lst[j]:
                smallest = j

        lst[smallest], lst[i] = lst[i], lst[smallest]

    return lst
