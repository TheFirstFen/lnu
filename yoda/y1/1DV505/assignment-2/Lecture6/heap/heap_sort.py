from . import Heap


def heap_sort(lst):
    if len(lst) <= 1:
        return lst
    heap = Heap.Heap()
    for i in lst:
        heap.add(i)

    sorted_lst = []
    while not heap.is_empty():
        sorted_lst.append(heap.pull_high())

    # pulls from biggest to smallest so reverse order it is
    return sorted_lst[::-1]
