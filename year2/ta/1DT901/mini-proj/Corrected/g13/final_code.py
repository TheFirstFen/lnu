import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import random
import os


# checks if lawnmower is outside
def is_outside(x, y,):
    if x >= len(cords_map) or x <= 0:
        return True
    elif y >= len(cords_map[0]) or y <= 0:
        return True
    if cords_map[int(x)][int(y)] == 1:
        return True
    else:
        return False


# takes one step
def one_step(x, y, new_ang, speed):
    x = x + speed * math.cos(new_ang) * dt  # xv
    y = y + speed * math.sin(new_ang) * dt  # yv
    return x, y


# path to map
path = os.getcwd() + "/ground_maps/my_map.csv"
cords = []

# add map to new list
with open(path, 'r') as map:
    for row in map:
        row = row.replace(',', ' ')
        row = row.replace('[', '')
        row = row.replace(']', '')
        row = row.strip()
        row = row.split()
        cords.append(row)


# change letters to 0, 1, 2
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
fig, ax = plt.subplots()
col_map = ListedColormap(["green", 'black', 'yellow'], 'indexed')
ax.pcolormesh(cords, edgecolors='k', linewidth=2, cmap=col_map)
ax.set_aspect("equal", adjustable='box')
ax = plt.gca()  # Get current axis object
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()

# map transpose 
cords_map = [[cords[j][i] for j in range(len(cords))] for i in range(len(cords[0]))]

# starting angle
new_ang = random.uniform(0, 2*math.pi)

# start at start-coordinates
for row in range(len(cords_map)):
    for col in range(len(cords_map)):
        if cords_map[row][col] == 2:
            x = row
            y = col

# coordinates visited list
xc = []
yc = []

# variables for running time
speed = 0.3
a = 0
h = 4    # hours
dt = 0.1   # time per step


# movement
while a < (h * 3600) / dt:
    x, y = one_step(x, y, new_ang, speed)
    if is_outside(x, y) is True:
        while is_outside(x, y) is True:
            new_ang = random.uniform(0, 2*math.pi)
            x, y = one_step(x, y, new_ang, speed)
            if is_outside(x, y) is True:
                # take a step back
                x, y = one_step(x, y, new_ang, -speed)
            else:
                xc.append(x)
                yc.append(y)
    else:
        xc.append(x)
        yc.append(y)
    a += 1


# visualize trace map
plt.plot(xc, yc, 'b-')
plt.show()


# change start-space value to uncut lawn
for ro in cords:
    for letters in range(len(ro)):
        if ro[letters] == 2:
            ro[letters] = 0


# variables
multiplier = 5
coverage = []
rows = []


# creates new bigger nestled list for coverage map
for i in range(len(cords)*multiplier):
    coverage.append(list())
for j in range(len(coverage)):
    for k in range(len(cords[0] * multiplier)):
        coverage[j].append(cords[int(j/multiplier)][int(k/multiplier)])


# count possible squares to be cut (for percentage)
possible = 0
for i in range(len(coverage)):
    for j in range(len(coverage[0])):
        if coverage[i][j] == 0:
            possible += 1


# coverage map
# turn to get coordinates in the right places
for i in coverage[0]:
    coverage[0][::-1]
coverage = [[coverage[j][i] for j in range(len(coverage))] for i in range(len(coverage[0]))]

# change uncut places to cut
for i in range(len(xc)):
    if coverage[int(xc[i] * multiplier)][int(yc[i] * multiplier)] == 0:
        coverage[int(xc[i] * multiplier)][int(yc[i] * multiplier)] = 2

# turn it back
coverage = [[coverage[j][i] for j in range(len(coverage))] for i in range(len(coverage[0]))]
for i in coverage[0]:
    coverage[0][::-1]


# count cut squares
cut = 0
for i in range(len(coverage)):
    for j in range(len(coverage[0])):
        if coverage[i][j] == 2:
            cut += 1


# calculate percentage
percentage = round((cut/possible)*100, 2)

# visualize coverage map
fig, ax = plt.subplots()
rows = len(coverage)
cols = len(coverage[0])
col_map = ListedColormap(["white", 'black', 'red'], 'indexed')
ax.pcolormesh(coverage, edgecolors='k', linewidth=1, cmap=col_map)
ax.set_aspect('equal', adjustable='box')
# percent as label
plt.xlabel(f'Visited {cut} out of {possible} ==> {percentage}%')
ax = plt.gca()  # Get current axis object
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()
