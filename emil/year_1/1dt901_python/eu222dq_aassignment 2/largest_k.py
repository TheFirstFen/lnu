sum_of_number = int(input("enter a number here: "))
k = 0
n = 0
while (k + n) <= sum_of_number:
    k += n
    n += 2
n -= 2
print(f"{n}")
