import random as rd


def one_step(x, y):
    r = rd.randint(1, 4)
    if r == 1:
        x += 1
    elif r == 2:
        x -= 1
    elif r == 3:
        y += 1
    elif r == 4:
        y -= 1
    return x, y


# Program starts
# Read configuration
# size = int( input("Enter the size: ") )
# steps = int( input("Enter the number of steps: ") )
# runs = int( input("Enter the number of sailors: ") )
size = 10
steps = 50
runs = 150

# Start simulation
lake_count = 0
for i in range(runs):
    count = 0
    x, y = 0, 0
    while abs(x) <= size and abs(y) <= size and count < steps:
        x, y = one_step(x, y)
        count += 1

    if count < steps:  # Check if fell into water
        lake_count += 1

ratio = round(100*lake_count/runs, 2)
print(f"Out of {runs} drunk sailors,", end=" ")
print(f"{lake_count} ({ratio}%) fell into the water.")
