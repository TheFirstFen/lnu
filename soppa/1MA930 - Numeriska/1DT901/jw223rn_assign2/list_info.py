from random import randint

x = []

for i in range(1, 101):
    x.append(randint(1, 10000))

ma = max(x)
mi = min(x)
avg = sum(x) / len(x)
r_avg = round(avg, 2)
x.remove(ma)
sma = max(x)

print(f"Largest value in list: {ma}")
print(f"Smallest value in list: {mi}")
print(f"Average value in list: {r_avg}")
print(f"Second largest value in list: {sma}")
