import csv
import matplotlib.pyplot as plt
import os
from matplotlib.colors import ListedColormap
from matplotlib.ticker import PercentFormatter
import random
import numpy as np
import questionary


# call the functions to run the simulation
def run_simulation(machines, map_list, x0, y0, timer):
    if machines == 1:
        x, y = movement(map_list, x0, y0, timer)
        show_map(map_list, x, y)
        coverage(x, y, map_list)
        return
    x, y = movement(map_list, x0, y0, timer)
    cov_map = expand_map(map_list)
    grass_count = np.sum((cov_map == 0) | (cov_map == 2))
    covx = expand_xy(x)
    covy = expand_xy(y)
    color_map(covx, covy, cov_map)
    cells_covered = np.count_nonzero((cov_map == 3))
    return round(100 * cells_covered / grass_count, 2)


# load the map
def load_map(file_path):
    map_list = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        pre_map_list = list(reader)
        for i in pre_map_list:
            temp_list = []
            for j in i:
                temp_list.append(0 if j == "L" else 1 if j == "O" else 2)
            map_list.append(temp_list)
    map_list.reverse()
    return map_list


# determine the starting point
def starting_point(map_list):
    [y], [x] = np.where(map_list == 2)
    print(x)
    return x, y


# determine the rotation angle
def random_velocity(v=0.01):
    alpha = random.uniform(0, 2 * np.pi)
    vx = v * np.cos(alpha)
    vy = v * np.sin(alpha)
    return vx, vy


# check if the lawnmower hit an obstacle
def check_collision(tempx, tempy, columns, rows):
    if tempx >= columns or tempx < 0 or tempy >= rows or tempy < 0:
        return True
    if map_list[int(tempy)][int(tempx)] == 1:
        return True


# calculate the movement
def movement(map_list, x0, y0, timer):
    x = [x0]
    y = [y0]
    newx = x0
    newy = y0
    vx, vy = random_velocity()
    time = 0
    temp_timer = 0
    rows, columns = map_list.shape
    while time <= timer:
        tempx = newx + vx
        tempy = newy + vy
        a = check_collision(tempx, tempy, columns, rows)
        if a:
            vx, vy = random_velocity()
            continue
        newx = tempx
        newy = tempy
        x.append(newx)
        y.append(newy)
        temp_timer += 1
        if temp_timer == 30:
            temp_timer = 0
            time += 1
    return x, y


# expand each square to 5X5
def expand_map(map_list):
    new_map = []
    for i in map_list:
        temp_map = []
        for j in i:
            temp_map.extend([j] * 5)
        for _ in range(5):
            new_map.append(temp_map.copy())
    new_map = np.array(new_map)
    return new_map


# expand x,y accordingly
def expand_xy(value):
    expanded = [x * 5 for x in value]
    return expanded


# color cells that were moved on
def color_map(covx, covy, cov_map):
    for i in range(len(covx)):
        cov_map[int(covy[i])][int(covx[i])] = 3
    return cov_map


# calculate the coverage of the lawnmower and show the corresponding map
def coverage(x, y, map_list):
    cov_map = expand_map(map_list)
    # count the number of lawn squares after making it smaller
    grass_count = np.sum((cov_map == 0) | (cov_map == 2))
    covx = expand_xy(x)
    covy = expand_xy(y)
    color_map(covx, covy, cov_map)
    cells_covered = np.count_nonzero((cov_map == 3))
    results = round(100 * cells_covered / grass_count)
    plt.figure()
    colors = ['w', 'k', 'w', 'r']
    color_map_cov = ListedColormap(colors)
    plt.pcolormesh(cov_map, cmap=color_map_cov, edgecolors='k')
    plt.figtext(0.5, 0.01, f"Visited {cells_covered} out of\
 {grass_count} ==> {results}%", ha='center', va='bottom',
                fontsize=16)
    plt.show()


# show the map in matplotlib
def show_map(map_list, x, y):
    rows, cols = map_list.shape
    lawn_cells = np.count_nonzero(map_list == 0) + 1
    plt.figure()
    # Assign color to value: 0 = green, 1 = black, 2 = yellow
    color_map = ListedColormap(['green', 'black', 'yellow'], 'indexed')

    # Plot grid
    plt.pcolormesh(map_list, edgecolors='k', linewidth=1, cmap=color_map)
    # Fine tune plot layout
    ax = plt.gca()  # Get current axis object
    ax.set_yticks(range(0, rows+1, 1))
    ax.set_xticks(range(0, cols+1, 1))
    plt.title(f"Colored grid of size {rows}x{cols} ({rows*cols}m^2)\
                \nlawn size = {lawn_cells}m^2 and the coverage is:\
 {round((100 * lawn_cells) / (rows*cols), 2)}%")
    plt.show()
    color_map2 = ListedColormap(['w', 'w', 'w'], 'indexed')
    plt.pcolormesh(map_list, cmap=color_map2)
    ax = plt.gca()  # Get current axis object
    ax.set_yticks(range(0, rows+1, 1))
    ax.set_xticks(range(0, cols+1, 1))
    plt.plot(x, y, color="blue", linewidth=1)
    plt.show()


# program excution
# store the machines data
machines = []
# user input for the number of machines
num_machines = input("how many machines would you like to run? [default: 1] ")
# if no input set the number to 1
if num_machines.strip() == "":
    num_machines = "1"

# user input to select the map
selected_map = questionary.select(
    "choose map:",
    choices=["simple", "empty", "small", "tricky", "my_map"]
).ask()

# user input to select the time unit
time_input = questionary.select(
    "choose a unit:",
    choices=['hours', 'minutes', 'seconds']
).ask()
# user input to choose the time
timer_input = input("for how long do you want it to run (input number)?\
[default: 1] ")
# if no input set the number to 1
if timer_input.strip() == "":
    timer_input = "1"
# set the timer to the picked time
timer = int(timer_input) * (1 if time_input == "seconds"
                            else 60 if time_input == "minutes" else 3600)
# get current path
path = os.getcwd()
# load the selected map and transfer it to numbers array
map_list = np.array(load_map(f'{path}/models/{selected_map}.csv'))

# set the starting points
x0, y0 = starting_point(map_list)

# run the simulation for each mamchine
for i in range(int(num_machines)):
    machines = [run_simulation(int(num_machines),
                map_list, x0, y0, timer) for _ in range(int(num_machines))]

# excuted only if number of machines is more than 1
if int(num_machines) > 1:
    average = round(sum(machines) / len(machines), 2)
    std = sum([(x - average) ** 2 for x in machines]) / (len(machines) - 1)
    std = round(std ** 0.5, 2)

# output on terminal
    for i in range(int(num_machines)):
        print(f"\nMachine {i+1}:")
        print(f"Coverage Percentage: {machines[i]}")
    print(f"\nthe total average is: {average}")
    print(f"the standard deviation is: {std}\n")

# output on diagram
    x_pos = list(range(1, int(num_machines) + 1))
    labels = [f"{n}" for n in x_pos]
    plt.bar(x_pos, machines)
    plt.xticks(x_pos, labels)
    plt.title(f"{int(num_machines)} machines average coverage")
    plt.subplots_adjust(bottom=0.2)
    plt.figtext(0.05, 0.1, f"the total average is: {average}", ha='left')
    plt.figtext(0.05, 0.05, f"the standard deviation is: {std}", ha='left')
    plt.xlabel("machine number")
    plt.ylabel("coverage percentage")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(100))
    plt.show()
