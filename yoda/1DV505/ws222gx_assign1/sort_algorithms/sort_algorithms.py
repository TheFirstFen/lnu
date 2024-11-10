import random
import time 




lst = []

for i in range(20):
    v = random.randint(1, 200)
    lst.append(v)

print(lst)



print(bubble_sort(lst))
print(insertion_sort(lst))
print(selection_sort(lst))
print(quick_sort(lst))
print(merge_sort(lst))


