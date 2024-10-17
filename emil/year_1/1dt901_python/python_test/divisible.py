def divisible(n):
    lst = []
    for i in range(1, n+1):
        if i % 6 == 0:
            lst.append(i)
        elif i % 7 == 0:
            lst.append(i)
    return lst


n = int(input("Enter a number here: "))

print(f"Divisible numbers in range of 1 to {n}")

div = divisible(n)
s = len(div)
j = 0
k = 10
while k < s + 10:
    print(*div[j: k])
    j += 10
    k += 10
