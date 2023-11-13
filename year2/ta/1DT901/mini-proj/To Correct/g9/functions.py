import math
from matplotlib import pyplot as plt
from matplotlib import colors
import random
import numpy as np


# Global variables
delta_t = 0.5
time_count = 0


def create_map(path):
    modlist = []
    lst = []
    with open(path, "r") as r:
        for line in r:
            lst.append(line.strip())
        for item in lst:
            new_lst = []
            for letter in item:
                if letter != ",":
                    if letter == "L":
                        new_lst.append(1)
                    elif letter == "O":
                        new_lst.append(0)
                    elif letter == "S":
                        new_lst.append(2)
            modlist.append(new_lst)
    return modlist


def visualize(data):
    cmap = colors.ListedColormap(['black', 'green', 'yellow'])
    plt.figure(figsize=(7, 5))
    plt.pcolor(data[::-1], cmap=cmap, edgecolors='k', linewidths=1)
    plt.title("Preview of map")
    plt.show()


"""
Source:
https://numpy.org/doc/stable/user/absolute_beginners.html#welcome-to-numpy
"""


def visualize_coverage(data, percentage):
    cmap = colors.ListedColormap(['black', 'white', 'yellow', 'red'])
    data = np.array(data)

    color_mapped_data = np.zeros(data.shape, dtype=int)
    color_mapped_data[data == 0] = 0
    color_mapped_data[data == 1] = 1
    color_mapped_data[data == 2] = 2
    color_mapped_data[data == 3] = 3

    plt.figure(figsize=(7, 5))
    plt.pcolor(color_mapped_data[::-1],
               cmap=cmap, edgecolors='k', linewidths=1,
               vmin=0, vmax=3)
    plt.title(f"Coverage map: {percentage}% visited")
    plt.show()


def coordinates(x, y, map):
    coordinates = map[::-1]
    return coordinates[x][y]


def pixel_map(map, N):
    big_lst = []
    for item in map:
        small_lst = []
        for value in item:
            for i in range(N):
                small_lst.append(value)
        for i in range(N):
            big_lst.append(small_lst)
    return big_lst


def find_start(map):
    map = map[::-1]
    for i, sub_list in enumerate(map):
        if 2 in sub_list:
            x, y = sub_list.index(2), i
            return x, y


def movement(time, N, map):
    global time_count
    x, y = find_start(map)
    x_list = []
    y_list = []
    vx = 0
    vy = 0.3
    while time_count < time:
        xnew, ynew = newcoordinates(x, y, vx, vy)
        while is_outside(xnew, ynew, map):
            vinkel = random.uniform(0, 2 * math.pi)
            vx = 0.3 * N * math.cos(vinkel)
            vy = 0.3 * N * math.sin(vinkel)
            xnew, ynew = newcoordinates(x, y, vx, vy)
        x_list.append(xnew)
        y_list.append(ynew)
        x = xnew
        y = ynew
    time_count = 0
    return x_list, y_list


def coverage(pixel, x_list, y_list):
    coverage_map = pixel.copy()
    reverse_map = coverage_map[::-1]
    floor_x = [math.floor(n) for n in x_list]
    floor_y = [math.floor(n) for n in y_list]
    b = list(zip(floor_x, floor_y))
    c = set(b)
    for item in c:
        x = item[0]
        y = item[1]
        new_row = list(reverse_map[y])
        new_row[x] = 3
        reverse_map[y] = new_row
    return reverse_map[::-1]


def get_percentage(map, coverage_map):
    grass_count = 0
    for item in map:
        for element in item:
            if element == 2 or element == 1:
                grass_count += 1
    cut = 0
    for item in coverage_map:
        for entry in item:
            if entry == 3:
                cut += 1

    percentage = round((cut/grass_count) * 100)
    return percentage


def is_outside(x, y, map):
    x = math.floor(x)
    y = math.floor(y)
    if x < 0 or x >= len(map[0]):
        return True
    if y < 0 or y >= len(map):
        return True
    if coordinates(y, x, map) == 0:
        return True
    return False


def tracemap(x_list, y_list, map):
    plt.plot(x_list, y_list, linestyle='-', color='blue', label='Line Example')
    plt.title("Lawnmower Trace")
    plt.xlim(-1, len(map[0])+1)
    plt.ylim(-1, len(map)+1)
    plt.show()


def newcoordinates(x, y, vx, vy):
    global time_count
    newx = x + vx * delta_t
    newy = y + vy * delta_t
    time_count += delta_t
    return newx, newy


def many_runs(map, num, N, time):
    per_list = []
    for i in range(num):
        xlist, ylist = movement(time, N, map)
        cov = coverage(map, xlist, ylist)
        per = get_percentage(map, cov)
        per_list.append(per)
    average = np.mean(per_list)
    standard_deviation = np.std(per_list)
    print(round(average, 1), "±", round(standard_deviation, 1))
    print(per_list)
