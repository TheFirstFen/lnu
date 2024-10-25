import random


# checks to see if the sailor is in the boundary
def sailor_in_boundary(x, y, boundary):
    return -boundary <= x <= boundary and -boundary <= y <= boundary


# simulates each sailor if it has fallen it returns True
def simulate_each_sailor(steps_max, boundary):
    x, y = 0, 0
    for step in range(steps_max):
        random_gen = random.randint(0, 3)

        if random_gen == 0:
            x += 1
        elif random_gen == 1:
            x -= 1
        elif random_gen == 2:
            y += 1
        else:
            y -= 1

        if not sailor_in_boundary(x, y, boundary):
            return True


boundary = int(input("Enter the size: "))
steps_max = int(input("Enter the number of steps: "))
sailors = int(input("Enter the number of sailors: "))
fallen_sailors = 0

# loops through each sailor
for sailor in range(sailors):
    if simulate_each_sailor(steps_max, boundary):
        fallen_sailors += 1

# calculates the percantage for the fallen sailors
calc = round((fallen_sailors/sailors)*100, 2)

print(f"Out of {sailors} drunk sailors, {fallen_sailors} ({calc}%) fell into "
      "the water")
