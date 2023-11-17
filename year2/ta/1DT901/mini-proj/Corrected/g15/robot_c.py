import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import random as rd
path = os.getcwd() + "/Simple.csv"  # Csv filepath


with open(path, "r") as file:  # open csv and make a list 0,1,2
    csv_list = []  # coordinats list
    ft = ""  # String to save line for line in csv file and modify
    index_sec = 0  # second index
    index_fir = 0  # first index
    for line in file:  # read line for line
        ft += line  # Add line to string ft
        csv_list.append([ch for ch in line if ch.isalpha()])  # add letters
    while index_fir < len(csv_list):  # go through all rows
        while index_sec <= len(csv_list[0]):  # go through all collumns
            if index_sec >= len(csv_list[0]):  # go to next row
                index_fir += 1
                index_sec = 0
                break
            elif csv_list[index_fir][index_sec] == "L":  # L = 0
                csv_list[index_fir][index_sec] = 0
            elif csv_list[index_fir][index_sec] == "O":  # O = 1
                csv_list[index_fir][index_sec] = 1
            else:
                csv_list[index_fir][index_sec] = 2  # S = 2
            index_sec += 1
    csv_list.reverse()  # Reverse list so origo is at the right place

# number of rows and columns
rows = len(csv_list)
columns = len(csv_list[0])


# x and y values
point_x = rd.uniform(-1, 1)  # random x point on unit circle
point_y = rd.uniform(-1, 1)  # random y point on unit circle
rand_a = math.tan(point_y / point_x)
start_x = 3.0
start_y = 0.0
v_coeffient = 0.3  # Change velosity
vx = v_coeffient * math.cos(rand_a)
vy = v_coeffient * math.sin(rand_a)
run_time = 15  # run time in minutes
t = 10  # steps per second
steps_to_take = run_time * (t * 60)
steps_taken = 0
x_max = columns
y_max = rows
y_min = 0
x_min = 0
v = round(math.sqrt((vx**2) + (vy**2)), 1)
path = []  # coordinates used for trace

# Plot grid in colors
plt.figure()
# 0 = green(L) 1 = black (O) 2 = yellow(S)
plt.subplot(1, 2, 1)  # Plot side by side
col_map = ListedColormap(["Green", "black", "yellow"], "indexed")
plt.pcolormesh(csv_list, edgecolors="k", linewidth=2, cmap=col_map)
ax = plt.gca()
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, columns+1, 1))
plt.title(f"colored grid of size {rows}x{columns}")


def new_velocity():  # Function since its used often
    point_x = rd.uniform(-1, 1)  # random x point on unit circle
    point_y = rd.uniform(-1, 1)  # random y point on unit circle
    rand_a = math.tan(point_y / point_x)
    vx = v_coeffient * math.cos(rand_a)  # New vx
    vy = v_coeffient * math.sin(rand_a)  # New vy
    return vx, vy


def is_outside(x, y):
    if x > x_max or x < x_min:  # outside on x axis
        return True
    elif y > y_max or y < y_min:  # outside on y axis
        return True
    elif csv_list[int(y)][int(x)] == 1:  # if true obstacle in the way
        return True
    return False  # inside and no obstacle


def take_step(x, y, vx, vy):
    global steps_taken
    global path
    global start_x
    global start_y
    next_x = start_x + (vx * (1 / t))  # next x coordinate
    next_y = start_y + (vy * (1 / t))  # next y coordinate
    while is_outside(next_x, next_y):  # as long as we are outside, new pos
        vx, vy = new_velocity()  # new vx and vy
        next_x = start_x + (vx * (1 / t))  # next x coordinate
        next_y = start_y + (vy * (1 / t))  # next y coordinate
    path.append([next_x, next_y])  # add the coodrinate to trace list
    start_x = next_x  # take step
    start_y = next_y  # take step
    steps_taken += 1  # add 1 step taken
    return vx, vy, start_x, start_y


# Main program
while steps_taken < steps_to_take:  # aslong as we have steps to take, move
    vx, vy, start_x, start_y = take_step(start_x, start_y, vx, vy)


xcords = []  # list of where we have been in x-axis
ycords = []  # list of where we have been in y-axis
for k in range(len(path)):
    xcords.append([path[k][0]])  # Add all x-coords
for k in range(len(path)):
    ycords.append([path[k][1]])  # Add all y-cords


plt.subplot(1, 2, 2)  # plot side by side
plt.title("Robot Trace")
plt.plot(xcords, ycords)  # plot trace
#plt.show()  # show plot

lst = [0] * 5
lst_ones = [2] * 5
lst_o = [lst_ones for i in range(5)]
lst_w = [lst for i in range(5)]
coverage_lst = []

for row in csv_list:
    for chr in row:
        if chr == 1:
            coverage_lst.append(lst_o)
        else:
            coverage_lst.append(lst_w)

index = 0
for i in path:
    x = 0
    y = 0
    if path[index][1] < 1:
        y = 0
        x = path[index][1]
    else:
        if path[index][1] < 0.2:
            y = 0
        elif path[index][1] > 0.2 and path[index][1] < 0.4:
            y = 1
        elif path[index][1] > 0.4 and path[index][1] < 0.6:
            y = 2
        elif path[index][1] > 0.6 and path[index][1] < 0.8:
            y = 3
        elif path[index][1] > 0.8:
            y = 4
        if path[index][0] < 0.2:
            x = 0
        elif path[index][0] > 0.2 and path[index][0] < 0.4:
            x = 1
        elif path[index][0] > 0.4 and path[index][0] < 0.6:
            x = 2
        elif path[index][0] > 0.6 and path[index][0] < 0.8:
            x = 3
        elif path[index][0] > 0.8:
            x = 4
        coverage_lst[int(path[index][0] + (path[index][1] ** 2))][y][x] = 1
    print(path[index][0], path[index][1], int(path[index][0] + (path[index][1] ** 2)))
    index += 1


print(coverage_lst)
