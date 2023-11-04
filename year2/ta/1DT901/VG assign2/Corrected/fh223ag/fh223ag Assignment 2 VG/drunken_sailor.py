# Import random to user for random steps and other variables
import random as rd
steps = 0
sailors_made_it = 0
sailor_failed = 0
current_x = 0
current_y = 0

# Ask user for size, steps and sailors
size_of_plane = int(input("Enter the size: "))
max_steps = int(input("Enter number of steps: "))
sailors = int(input("Enter number of sailors: "))

# Set grid boundaries
x_max = size_of_plane
x_min = 0 - size_of_plane
y_max = size_of_plane
y_min = 0 - size_of_plane


# Function to see if sailor is on grid or out of bounds
def on_grid():
    global current_x
    global current_y
    global sailor_failed
    global steps
    global current_x
    global current_y
    while (sailors_made_it + sailor_failed) < sailors:
        if current_x < x_max and current_y < y_max:
            if current_x > x_min and current_y > y_min:
                return True
            else:
                sailor_failed += 1
                steps = 0
                current_x = 0
                current_y = 0
                return False
        else:
            sailor_failed += 1
            steps = 0
            current_x = 0
            current_y = 0
            return False


# Function called take step to move sailors
def take_step():
    global sailors_made_it
    global steps
    global current_x
    global current_y
    global move_y
    if steps > max_steps:
        sailors_made_it += 1
        steps = 0
        current_x = 0
        current_y = 0
    else:
        move_x = rd.randrange(-1, 2, 1)
        if move_x == 0:
            move_y = rd.randrange(-1, 2, 2)
        elif move_x != 0:
            move_y = 0
        current_x += move_x
        current_y += move_y
        steps += 1


# Simulations
while (sailors_made_it + sailor_failed) < sailors:
    while on_grid():
        take_step()

# print results
percentage_failed = (sailor_failed / sailors) * 100
print(f"Out of {sailors} drunk sailors, ", end=(""))
print(f"{sailor_failed} ({percentage_failed}%) fell into the water.")
