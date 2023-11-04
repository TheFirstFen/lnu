import random

# Input: Read boundary (k), maximum number of steps, and number of sailors
k = int(input("Enter the boundary (k): "))
max_steps = int(input("Enter the maximum number of steps: "))
num_sailors = int(input("Enter the number of drunken sailors to simulate: "))

fallen_sailors = 0

for _ in range(num_sailors):
    x, y = 0, 0  # Start at the origin
    for _ in range(max_steps):
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        if abs(x) > k or abs(y) > k:
            fallen_sailors += 1
            break

print(f"Out of {num_sailors} sailors, {fallen_sailors} fell into the water.")
