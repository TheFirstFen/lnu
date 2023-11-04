from random import randint
# info from user
sz = int(input("Enter the size: "))
steps = int(input("Enter the number of steps: "))
sailor = int(input("Enter the number of sailors: "))
# Number of drowning sailors
out = 0
# Computing
for i in range(0, sailor):
    lst = ([0, 0], [0, 0])
    for j in range(0, steps):
        dir = randint(1, 4)
        if dir == 1:
            lst[0][0] -= 1
        if dir == 2:
            lst[0][1] += 1
        if dir == 3:
            lst[1][0] -= 1
        if dir == 4:
            lst[1][1] += 1
    if lst[0][0] < -sz or lst[0][1] > sz or lst[1][0] < -sz or lst[1][1] > sz:
        out += 1
out = out/sailor
# Displaying results
print(f"Out of {sailor} drunk sailors, {out*sailor} ({out*100}%)",
      "fell into the water.")
