# Import random module
import random


# Find out if sailor is in water
def is_in_water(k, steps):
    # Start position
    x = 0
    y = 0

# Loop for amount of steps taken
    for i in range(steps):
        direction = random.choice(["right", "left", "up", "down"])
        if direction == "right":
            x += 1
        elif direction == "left":
            x -= 1
        elif direction == "up":
            y += 1
        elif direction == "down": # onödig räcker med en else
            y -= 1
        if x > k or y > k or x < -k or y < -k: 
            return True

    return False


# Start of program

# Read input
k = int(input("Enter the size: "))

steps = int(input("Enter the number of steps: "))

sailors = int(input("Enter the number of sailors: "))

# Counter for people in water
count = 0

for i in range(sailors):
    if is_in_water(k, steps):
        count += 1

print(count)

# Calculation of percentage of sailors in water
p = round(100*count/sailors, 2)

# Result
print(f"Out of {sailors} drunk sailors, {count} ({p}%) fell into the water.")