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


# path to map
path = os.getcwd() + "/Small.csv"
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
"""for ro in cords:
    print(row)"""


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

# test print
for c in cords_map:
    print(c)
print(cords_map[3][0])

# test print
for row in cords_map:
    print(row)


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

h = 2       # hours
dt = 0.5    # time per step
vx = x + 0.3*math.cos(new_ang) * dt  # xv
vy = y + 0.3*math.sin(new_ang) * dt


def one_step(x, y, vx, vy):
    




plt.plot(xc, yc, 'b-')
plt.show()
