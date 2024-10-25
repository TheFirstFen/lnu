import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import random


def read_file(path):

    plot_map = []

    with open(path, "r") as file:
        lst = file.readlines()
        for symbol in lst:
            temp_list = []
            for char in symbol:
                if (char == "O"):
                    temp_list.append(0)
                elif (char == "L"):
                    temp_list.append(1)
                elif (char == "S"):
                    temp_list.append(2)
            plot_map.append(temp_list)
    lst = []
    for i in range(len(plot_map[0])):
        column = []
        for row in plot_map:
            column.append(row[i])
        lst.append(column[::-1])

    return lst


def transpose_visuals_pixel_map(lst):
    new_lst = []
    for i in range(len(lst[0])):
        column = []
        for row in range(len(lst)):
            column.append(lst[row][i])
        new_lst.append(column)
    return new_lst


def cords_split(lst):  # sparar värden där den kört
    x_coords = []
    y_coords = []

    for num in lst:
        x_coords.append(num[0])
        y_coords.append(num[1])
    return x_coords, y_coords


def start_point(plot_map):
    for lists in range(len(plot_map)):
        for i in range(len(plot_map[0])):
            if plot_map[lists][i] == 2:
                x = lists
                y = i
                return x, y


def is_outside(x, y):
    if x < 0 or x > cols:
        return True
    if y < 0 or y > rows:
        return True
    else:
        symbol = plot_map[int(x)][int(y)]
        if symbol == 0:
            return True
        else:
            return False


def one_step(x, y, vx, vy, delta_t):
    delta_t = 0
    x_new = x
    y_new = y
    can_move = True

    while can_move:
        # vx = 0.3 * math.cos(math.pi/2)
        # vy = 0.3 * math.sin(math.pi/2)

        # x_new = x_new + (vx * delta_t)
        # y_new = y_new + (vy * delta_t)
        x_new += vx
        y_new += vy
        delta_t += 1

        if is_outside(x_new, y_new):
            can_move = False

    while is_outside(x_new, y_new):
        delta_t += 1

        x_new -= vx
        y_new -= vy
    return x_new, y_new, delta_t


def bounce(x, y, t):
    alpha = random.uniform(0, 2 * math.pi)
    v = 0.3

    # x = x + v*math.cos(alpha) * t
    # y = y + v*math.sin(alpha) * t
    vx = v*math.cos(alpha)
    vy = v*math.sin(alpha)
    return vx, vy


def cut(cordinate, lst):  # ej använd än
    lst[int(cordinate[0])][int(cordinate[1])] = 3


def coverage_grid(multiplier):
    temp_list = []
    for col in read_file(path):
        for symbol in col:
            for i in range(multiplier):
                temp_list.append(symbol)
    return temp_list
    """temp_list2 = []
    for row in temp_list:
        for i in range(multiplier):
            temp_list2.append(row)
    return temp_list2"""


# Main
path = "ground_maps/simple.csv"
plot_map = read_file(path)
rows = len(plot_map[0])
cols = len(plot_map)
x_cords, y_cords = start_point(plot_map)
vx = 0
vy = 0.3
t = 1
time_gone = 0
multiplier = 5
lst = []

# Start program
times_run = 0
while times_run < 10:
    lst.append([x_cords, y_cords])
    x_cords, y_cords, time_gone = one_step(x_cords, y_cords, vx, vy, time_gone)
    vx, vy = bounce(x_cords, y_cords, time_gone)
    times_run += time_gone

x_coords, y_coords = cords_split(lst)

print(coverage_grid(multiplier))
# Plotting
plt.figure()
color_map = ListedColormap(['black', 'green', "yellow"], 'indexed')
plt.pcolormesh(transpose_visuals_pixel_map(plot_map),
               edgecolors='k', linewidth=2, cmap=color_map)

ax = plt.gca()
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()

plt.plot(x_coords, y_coords)
plt.show()
