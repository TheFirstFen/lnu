num = int(input("How many primes? "))

cnum = 2
count = 0
prow = 10


def isnot_prime(x):
    for i in range(2, x):
        if x == 2 or x == 3 or x == 5 or x == 7:
            return False
        elif x % i == 0:
            return True


while count <= (num - 1):
    if prow == 0:
        print(end="\n")
        prow = 10
    elif not isnot_prime(cnum):
        print(cnum, end=" ")
        cnum += 1
        prow += -1
        count += 1
    else:
        print(end="")
        cnum += 1
print()
