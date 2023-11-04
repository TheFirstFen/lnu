import random
# store use input for platform size, steps, and number of sailors
size = int(input("Enter the size: "))
steps = int(input("Enter the number of steps: "))
sailors = int(input("Enter the number of sailors: "))

# creat a virtal platform
platform = [0, 0]
# creat a variable to store the number of drunk sailors
sailors_drowned = 0

# loop through the number of sailors
for i in range(sailors):
    # reset the platform for the next sailor
    platform = [0, 0]
    # loop through the number of steps
    for i in range(steps):
        # generate a random number of moves
        moves = random.randint(1, 4)
        # check if the sailor falls into the water
        if abs(platform[0]) == size or abs(platform[1]) == size:
            sailors_drowned += 1
            break
        # move the sailor up
        if moves == 1:
            platform[0] += 1
        # move the sailor down
        if moves == 2:
            platform[0] -= 1
        # move the sailor left
        if moves == 3:
            platform[1] += 1
        # move the sailor right
        if moves == 4:
            platform[1] -= 1

# print the results
print(f"Out of {sailors} drunk sailors, {sailors_drowned}\
 ({round(sailors_drowned * 100 / sailors, 2)}%) fell into the water.")
