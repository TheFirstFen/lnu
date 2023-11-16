# triangle.py
#
# Author: Samuel Berg
# 06-Oct-2022

def positive_int(float_lst):
    int_lst = []
    for i in float_lst:
        if i > 0:
            int_lst.append(round(i))
    return int_lst


def largest_K(N):
    tot = 0
    count = 1
    while (tot + count) <= N:
        tot += count
        count += 2
    count -= 2
    return count


# Demonstration code
lst = [1.3, 2.67, -2.25, 4.88]
N = 40

print(lst)
print(positive_int(lst))

print(f'N = {N}')
print(largest_K(N))

# Completed
