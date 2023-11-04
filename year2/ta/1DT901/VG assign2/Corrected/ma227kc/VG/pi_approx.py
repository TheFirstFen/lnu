from random import uniform
# Info from user
N = int(input("Choose the number of points: "))
# number of points inside the circle
num = 0

# Computing
for i in range(N):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    if x**2 + y**2 <= 1:
        num += 1
# Ratio between a circle with R radius and a square with the side 2R is Pi/4
results = (num / N) * 4

print(results)
