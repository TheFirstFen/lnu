import random


def man_over_board(size, x, y):
    return -size <= x <= size and -size <= y <= size


# variables
size = int(input("Enter size: "))
steps = int(input("Enter the number of steps: "))
sailors = int(input("Enter rhe number of sailiors: "))


water = 0
for i in range(sailors):
    x, y = 0, 0
    for j in range(steps):
        step = random.randint(0, 3)
        if step == 0:
            y += 1
        elif step == 1:
            x += 1
        elif step == 2:
            y -= 1
        else:
            x -= 1
    if not man_over_board(size, x, y):
        water += 1

p = (water/sailors) * 100

print(f"""Out of {sailors} drunk sailors, {water} ({round(p, 2)}%)
      fell into the water.""")
