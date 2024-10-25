import random


def random_list(n):
    return [random.randint(1, 10) for i in range(n)]


def average(lst):
    return round(sum(lst) / len(lst))


def only_odd(lst):
    return [num for num in lst if num % 2 != 0]


def to_string(lst):
    return "[" + ",".join([str(i) for i in lst]) + "]"


def contains(lst, a, b):
    for index in range(len(lst)-1):
        if lst[index] == a and lst[index+1] == b:
            return True
    return False


def has_duplicates(lst):
    for index in range(len(lst)-1):
        for num in range(index+1, len(lst)):
            if lst[index] == lst[num]:
                return True
    return False


lst = random_list(10)
print(lst)

print(average(lst))
print(only_odd(lst))
print(to_string(lst))
print(contains(lst, 1, 3))
print(has_duplicates(lst))
