import random
size = int(input("Enter the size: "))
steps = int(input("Enter the number of steps: "))
sailors = int(input("Enter the number of sailors: "))
fallen_sailors = 0


#  function checking if the sailor has fallen
def boundary(x, y, size):
    if (x < -size or x > size):
        return True
    elif (y < -size or y > size):
        return True


def randomstep(boundary, steps):
    x = 0
    y = 0
    #  for loop randomizing the steps
    for i in range(steps):
        direction = random.randint(0, 3)
        if (direction == 0):
            y -= 1
        elif (direction == 1):
            x -= 1
        elif (direction == 2):
            x += 1
        else:
            y += 1
        if boundary(x, y, size):
            return True


#  adds a fallen sailor when it's detected
for k in range(sailors):
    if (randomstep(boundary, steps)):
        fallen_sailors += 1

#  calculating the percentage of sailors fallen
amount = (fallen_sailors/sailors) * 100
percentage = round(amount, 2)

print(f"Out of {sailors} drunken sailors, {fallen_sailors} ({percentage}%)"
      "fell into the water")
