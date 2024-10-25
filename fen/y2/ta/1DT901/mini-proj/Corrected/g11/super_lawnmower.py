import csv
import matplotlib.pyplot as plt
import os
from matplotlib.colors import ListedColormap
from matplotlib.ticker import PercentFormatter
import numpy as np
import questionary


# call the functions to run the simulation
def run_simulation(machines, map_list):
    # run for one machine
    if machines == 1:
        map_list = movement(map_list)
        coverage(map_list)
        return
    # run for multiple machines
    map_list = movement(map_list)
    cov_map = expand_map(map_list)
    grass_count = np.sum((cov_map == 0) | (cov_map == 2))
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
    map_list = expand_map(map_list)
    return map_list


# determine the starting point
def starting_point(map_list):
    start_row, start_col = np.where(map_list == 2)
    x = start_col[0]
    y = start_row[0] + 0.5
    return x, y


# determine the rotation angle
def velocity(value="right"):
    v = 0.3
    # 0: right, 1: up, 2: left, 3: down
    directions = {'right': 0, 'left': 2, 'up': 1, 'down': 3}
    alpha = np.deg2rad(directions[value] * 90)
    vx = v * np.cos(alpha)
    vy = v * np.sin(alpha)
    return vx, vy


# check if the lawnmower hit an obstacle
def check_collision(tempx, tempy, columns, rows, map_list):
    print(tempx, tempy)
    if tempx > columns - 0.5 or tempx < 0.5\
            or tempy > rows - 0.5 or tempy < 0.5:
        return True
    tempx = int(tempx)
    tempy = int(tempy)
    if (map_list[tempy][tempx] == 1 or map_list[tempy][tempx] == 3):
        return True
    return False


def check_right(x, y, map_list, direction):
    curx, cury = int(x), int(y)
    movements = {
        "up": (1, 0),  # Move right when facing up
        "down": (-1, 0),  # Move left when facing down
        "left": (0, 1),  # Move up when facing left
        "right": (0, -1),  # Move down when facing right
    }

    # Get the movement based on the current direction
    move_x, move_y = movements[direction]
    leftx, lefty = movements["left"]
    print(movements[direction])
    # Calculate the new position
    new_x = curx + move_x
    new_y = cury + move_y
    print(new_x, "newx")
    print(new_y, "newy")
    print(curx, "curx")
    print(cury, "cury")
    print(len(map_list[0]), "maplist")
    if 0 <= new_x < len(map_list[0]) and 0 <= new_y < len(map_list):
        # Check if the position to the "right" is free
        if map_list[new_y][new_x] == 0 or map_list[new_y][new_x] == 4\
                or map_list[lefty][leftx] == 4:
            print(map_list[cury][curx], "the 4")
            print(map_list[new_y][new_x], "new 4")
            map_list[cury][curx] = 4
            return True  # The space to the "right" is free to move into.
    return False


# calculate the movement
def movement(map_list):
    map_list[map_list != 1] = 3
    return map_list


# exoand each square to 5X5
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


# calculate the coverage of the lawnmower and show the corresponding map
def coverage(map_list):
    cov_map = map_list
    # count the number of lawn squares after making it smaller
    grass_count = np.sum((cov_map == 0) | (cov_map == 2))
    cells_covered = np.count_nonzero((cov_map == 3))
    results = 100
    
    # Define your custom colormap with colors for specific indices
    colors = ['w', 'k', 'y', 'r', 'g']
    color_map_cov = ListedColormap(colors, "indexed")
    
    # Create a color array based on your custom colormap
    color_array = color_map_cov(cov_map)
    
    plt.figure()
    plt.pcolormesh(color_array, edgecolors='k')
    plt.figtext(0.5, 0.01, f"Visited {cells_covered} out of {grass_count}\
 ==> {results}%", ha='center', va='bottom', fontsize=16)
    plt.show()


# program excution
machines = []
num_machines = input("how many machines would you like to run? [default: 1] ")
if num_machines.strip() == "":
    num_machines = "1"

selected_map = questionary.select(
    "choose map:",
    choices=["simple", "empty", "small", "tricky", "my_map"]
).ask()

time_input = questionary.select(
    "choose a unit:",
    choices=['hours', 'minutes', 'seconds']
).ask()
timer_input = input("for how long do you want it to run (input number)?\
[default: 1] ")
if timer_input.strip() == "":
    timer_input = "1"
timer = int(timer_input) * (1 if time_input == "seconds"
                            else 60 if time_input == "minutes" else 3600)

path = os.getcwd()
map_list = np.array(load_map(f'{path}/models/{selected_map}.csv'))

x0, y0 = starting_point(map_list)

for i in range(int(num_machines)):
    machines = [run_simulation(int(num_machines),
                map_list) for _ in range(int(num_machines))]

if int(num_machines) > 1:
    average = round(sum(machines) / len(machines), 2)
    std = sum([(x - average) ** 2 for x in machines]) / (len(machines) - 1)
    std = round(std ** 0.5, 2)

    for i in range(int(num_machines)):
        print(f"\nMachine {i+1}:")
        print(f"Coverage Percentage: {machines[i]}")
    print(f"\nthe total average is: {average}")
    print(f"the standard deviation is: {std}\n")
    x_pos = list(range(1, int(num_machines) + 1))
    labels = [f"{n}" for n in x_pos]
    plt.bar(x_pos, machines)
    plt.xticks(x_pos, labels)
    plt.title(f"{int(num_machines)} machines average coverage")
    plt.xlabel("machine number")
    plt.ylabel("coverage percentage")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(100))
    plt.show()
