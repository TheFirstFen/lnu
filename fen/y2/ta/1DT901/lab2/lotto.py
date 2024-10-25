import random as rd

lotto = []
while len(lotto) < 7:
    n = rd.randint(1, 35)
    if n not in lotto:
        lotto.append(n)

# Sort and print
lotto.sort()
print("\nThe Lotto numbers this week:")
for i in lotto:
    print(i, end=" ")
print()
