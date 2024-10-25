import random


def random_num_list(n):
    lst = []
    for i in range(0, n):
        i = random.randint(0, 100)
        lst.append(i)
    return lst


def only_odd(lst):
    for i in range(0, len(lst)):
        if i % 2 == 0:
            lst.pop()
    return lst


def square_lst(x):
    sq = []
    for i in x:
        sq.append(i*i)
    return sq


def sublist(lst, start, stop):
    lst_new = []
    for i in range(start, stop):
        lst_new.append(lst[i])
    return lst_new


n = int(input("Enter how many elements you want: "))


lst = random_num_list(n)
print(f"{lst}")
print(only_odd(lst))
print(square_lst(lst))
print(sublist(lst, 1, 4))
