import random

count = {}
for j in range(1, 11):
    count[j] = 0
for i in range(100):
    rnd = random.randint(1, 10)
    if rnd not in count:
        count[rnd] = 0
    count[rnd] += 1


for k, v in count.items():
    print(f"{k}\t{v}")
