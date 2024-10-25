import random


# Take input from user
def user_input():

    step_count = int(input("Enter the number of steps: "))
    grid = int(input("Enter the size: "))
    sailor_amount = int(input("Enter the number of sailors: "))
    return drunken_sailor(step_count, grid, sailor_amount)


# Check if the sailor out of grid range.
def drunken_sailor(step_count, grid, sailor_amount):
    dry_sailor = 0
    wet_sailor = 0

    max_y, min_y = grid, -grid
    max_x, min_x = grid, -grid

    for sailor in range(sailor_amount):
        current_place = {"X": 0, "Y": 0}

        for step in range(step_count):
            step_generator = random.randint(0, 3)
            if step_generator == 0:
                current_place["Y"] += 1
            elif step_generator == 1:
                current_place["Y"] -= 1
            elif step_generator == 2:
                current_place["X"] += 1
            else:
                current_place["X"] -= 1

        if (current_place["X"] > max_x) or (current_place["X"] < min_x):
            wet_sailor += 1
        if (current_place["Y"] > max_y) or (current_place["Y"] < min_y):
            wet_sailor += 1
        else:
            dry_sailor += 1
    return output(wet_sailor, sailor_amount)


# Calculate the procentage and print it
def output(wet_sailor, sailor_amount):
    percentage_wet = (wet_sailor / sailor_amount) * 100
    print(f"Out of {sailor_amount} drunk sailors, {wet_sailor}\
({percentage_wet:.2f}%) fell into the water.")


user_input()
