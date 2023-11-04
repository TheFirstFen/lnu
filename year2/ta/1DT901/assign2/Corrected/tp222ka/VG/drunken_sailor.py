import random


# Function for generating random number between 1 and 4
def rnd_num():
    rnd = random.randint(1, 4)
    return rnd


# Function for direction base on random number
# to determine (left, right, up, or down)
def direction():
    x, y = 0, 0  # Start at (0,0)
    rnd = rnd_num()
    if rnd == 1:
        x += 1  # Left
    elif rnd == 2:
        x -= 1  # Right
    elif rnd == 3:
        y += 1  # Up
    elif rnd == 4:
        y -= 1  # Down
    return x, y


# Simulate a single drunk sailor taking multiple steps
def walk_step(step):
    x, y = 0, 0
    for _ in range(step):
        move_x, move_y = direction()  # Get a random direction
        x += move_x  # Update the position in the x-axis
        y += move_y  # Update the position in the y-axis
    return x, y


# check if the sailor is inside the given size boundery
def check_inside(x, y, size):
    return abs(x) <= size and abs(y) <= size


# Run the simulate sailors for a specified number
def simulate(size, step, sailor):
    drunk_sailor = 0
    for _ in range(sailor):
        final_position = walk_step(step)  # simulate sailor step
        # Check if sailor is inside the boundary
        inside = check_inside(final_position[0], final_position[1], size)
        if not inside:
            drunk_sailor += 1  # If not inside, count them as a drunk sailor
    percent = (drunk_sailor / sailor) * 100  # Calculate the percentage
    print(f"Out of {sailor} drunk sailors, {drunk_sailor} ", end="")
    print(f"({percent:.2f}%) fell into the water")


# Get user input for simulation parameters
size = int(input("Enter the size: "))
step = int(input("Enter the number of steps: "))
sailor = int(input("Enter the number of sailors: "))

# Run the simulation using user input
simulate(size, step, sailor)
