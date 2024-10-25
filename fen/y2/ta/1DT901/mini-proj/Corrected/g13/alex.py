import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import random
import os


def is_outside(x, y,):
    if x >= len(cords_map) or x <= 0:
        return True
    elif y >= len(cords_map[0]) or y <= 0:
        return True
    if cords_map[int(x)][int(y)] == 1:
        return True
    else:
        return False


def one_step(x, y, new_ang, speed):
    x = x + speed * math.cos(new_ang) * dt  # xv
    y = y + speed * math.sin(new_ang) * dt  # yv
    return x, y


# path to map
path = os.getcwd() + "/my_map.csv"
cords = []

# add map to new list
with open(path, 'r') as map:
    for row in map:
        row = row.replace(',', '')
        row = row.replace('[', '')
        row = row.replace(']', '')
        row = row.strip()
        row = row.split()
        cords.append(row)


for rows in cords:
    for letters in range(len(rows)):
        if rows[letters] == 'L':
            rows[letters] = 0
        elif rows[letters] == 'O':
            rows[letters] = 1
        else:
            rows[letters] = 2


# change order
cords = cords[::-1]



#  visualize ground map
rows = len(cords)
cols = len(cords[0])
col_map = ListedColormap(["green", 'black', 'yellow'], 'indexed')
plt.pcolormesh(cords, edgecolors='k', linewidth=2, cmap=col_map)

ax = plt.gca()  # Get current axis object
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()

cords_map = [[cords[j][i] for j in range(len(cords))] for i in range(len(cords[0]))]

# random new angle
new_ang = random.uniform(0, 2*math.pi)
print(new_ang)

# start coordinates
for row in range(len(cords_map)):
    for col in range(len(cords_map)):
        if cords_map[row][col] == 2:
            x = row
            y = col


xc = []
yc = []
a = 0
speed = 0.3
h = 10     # hours
dt = 0.3    # time per step

for i in range(0, 60):     # 60 is test value
    while a < (h * 3600) / dt:
        # x = x + speed*math.cos(new_ang) * dt  # xv
        # y = y + speed*math.sin(new_ang) * dt  # yv
        x, y = one_step(x, y, new_ang, speed)
        if is_outside(x, y) is True:
            while is_outside(x, y) is True:
                new_ang = random.uniform(0, 2*math.pi)
                x, y = one_step(x, y, new_ang, speed)
                # x = x + speed * math.cos(new_ang) * dt
                # y = y + speed * math.sin(new_ang) * dt
                if is_outside(x, y) is True:
                    # x = x - speed * math.cos(new_ang) * dt
                    # y = y - speed * math.sin(new_ang) * dt
                    x, y = one_step(x, y, new_ang, -speed)  # one step fast ett steg tillbaka
                else:
                    xc.append(x)
                    yc.append(y)

        else:
            xc.append(x)
            yc.append(y)

        a += 1


plt.plot(xc, yc, 'b-')
plt.show()
