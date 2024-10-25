import random


def movement():
    move = [1, 2, 3, 4]
    # randomly chooses one option
    r = random.choice(move)

    # each option correlates to a move
    if r == move[0]:    # x + 1
        position[0] += 1

    elif r == move[1]:  # x - 1
        position[0] -= 1

    elif r == move[2]:  # y + 1
        position[1] += 1

    else:               # y - 1
        position[1] -= 1

    return position


def percentage(fallen_sailor, sailors):
    # fallen devided by total then times 100 to get percentage
    percentage = (fallen_sailor/sailors)*100
    percentage = round(percentage, 2)

    return percentage


# get grid size
size = int(input("Enter size: "))
boundary = []
boundary.append(-size)
boundary.append(size)

# input sailors and steps
steps = int(input("Enter the number of steps: "))
sailors = int(input("Enter the humber of sailors: "))

fallen_sailor = 0

# for every sailor
for i in range(0, sailors):
    # resets position for new sailor
    position = [0, 0]

    # for every step
    for j in range(0, steps):
        is_fallen = False

        # moves sailor
        movement()

        # checks if sailor has fallen
        for k in position:
            if k < -size or k > size:
                # counts fallen silors
                fallen_sailor += 1
                is_fallen = True
                break

        # stops iteration when sailor has fallen
        if is_fallen:
            break

# percentage of fallen sailros
percent = percentage(fallen_sailor, sailors)

# print resaults
print(f"Out of {sailors} drunk sailors, {fallen_sailor} ({percent}%) fell" +
      " into the water.")
