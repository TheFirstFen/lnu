from random import randint

n = int(input("Provide a positive integer: "))
start = int(input("Between which slots in list do you want to see? Start: "))
stop = int(input("Stop: "))


def random_num_list(n):
    return [randint(1, 100) for i in range(n)]


def only_odd(lst):
    nlst = []
    for i in lst:
        if i % 2 != 0:
            nlst.append(i)
    return nlst


def square(lst):
    nlst = []
    for i in lst:
        sqi = i ** 2
        nlst.append(sqi)
    return nlst


def sublist(lst, start, stop):
    nlst = []
    nlst = lst[start - 1:stop]
    return nlst


lst = random_num_list(n)
odlst = only_odd(lst)
sqlst = square(lst)
sblst = sublist(lst, start, stop)

print(f"Here is the list: {lst}")
print(f"Odds in it are: {odlst}")
print(f"Each number squared: {sqlst}")
print(f"The values between slot {start} and {stop} are: {sblst}")
