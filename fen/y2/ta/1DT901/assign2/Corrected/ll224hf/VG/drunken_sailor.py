# import random
import random


# Make a function for where the sailor is going
def where_next(x, y):
    # first decide on the axis the sailor is moving.
    direction = random.choice([x, y])
    # then decide which direction on the axis, positive or negative.
    step = random.choice([-1, 1])

    # final add the step in given direction
    if direction == x:
        x += step
    else:
        y += step
    return x, y


# Request the inputs. size, steps and amount of sailors.
size = int(input("Enter the size: "))
num_steps = int(input("Enter the number of steps: "))
num_sailor = int(input("Enter the number of sailors: "))

# Nobody has drowned yet, i think.
drowned = 0

# Make a for range. Make all the sailors walk the plank!
for i in range(num_sailor):

    # Set current coordinates and amount of steps already taken.
    # This also resets it for each sailor.
    x = 0
    y = 0
    steps_taken = 0

    # A while loop that continusly runs the loop until all steps taken
    # or the sailor falls off.
    while abs(x) <= size and abs(y) <= size and steps_taken < num_steps:
        # Call for function on where the sailor is going
        x, y = where_next(x, y)
        steps_taken += 1

        # Check if the sailor is still above sea level. if not -> drowned
        if abs(x) > size or abs(y) > size:
            drowned += 1

# Make sure that you dont divide by 0 :)
if drowned != 0:
    percent = round((drowned / num_sailor) * 100, 2)
else:
    percent = 0

# Print results!
print(f"Out of {num_sailor} drunk sailors, {drowned} ({percent}%) fell into" +
      " the water.")
