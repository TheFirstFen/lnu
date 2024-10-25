import random as rd


def random_list(n):
    return [rd.randint(1, 100) for i in range(n)]


def average(lst):
    return round(sum(lst)/len(lst))


def only_odd(lst):
    return [n for n in lst if n % 2 == 1]


def to_string(lst):  # return str(lst)
    ret = "["
    if len(lst) > 0:
        ret += str(lst[0])
    for i in range(1, len(lst)):
        ret = ret + "," + str(lst[i])
    ret += "]"
    return ret


def contains(lst, a, b):
    for i in range(len(lst)-1):
        if lst[i] == a and lst[i+1] == b:
            return True
    return False


def has_duplicates(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
