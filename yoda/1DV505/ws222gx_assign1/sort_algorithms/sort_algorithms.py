import random
import time 

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        second_element = lst[i]
        j = i - 1 # first element basically
        
        while lst[j] > second_element and j >= 0:
            lst[j+1] = lst[j]
            j -= 1 
        lst[j+1] = second_element
    return lst


def selection_sort(lst):
    for i in range(1, len(lst)-1):
        smallest = i 
        for j in range (i+1, len(lst)):
            if lst[smallest] > lst[j]:
                smallest = j
        
        lst[smallest], lst[i] = lst[i], lst[smallest]

    return lst


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


def quick_sort(lst):
    if len(lst) <= 1: # already sorted
        return lst
    pivot_element, left_lst, right_lst = partion_lst(lst)
    left_sorted = quick_sort(left_lst)
    right_sorted = quick_sort(right_lst)
    return right_sorted + [pivot_element] + left_sorted


def merge_sort(lst):
    pass

lst = []

for i in range(10):
    v = random.randint(1, 100)
    lst.append(v)

print(lst)
print(bubble_sort(lst))
print(insertion_sort(lst))
print(selection_sort(lst))
print(quick_sort(lst))
