import random as rd

sums = 13*[0]  # Positions 0 and 1 never used
for i in range(10000):
    rn1 = rd.randint(1, 6)
    rn2 = rd.randint(1, 6)
    sums[rn1+rn2] += 1

print("\nFrequency table (sum,count) for rolling two dices 10000 times")
for i in range(2, 13):
    print(i, "\t", sums[i])
