from scaler import reader as map_gen
import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import random


# Function to record history of moves, starting with starting square
def history(x, y):
    move_history.append([x, y])


# calculate coverage and set square that was cut to cut (3)
def coverage(cut_map, moves):
    new_coordinate_system = cut_map.copy()
    total = len(new_coordinate_system) * len(new_coordinate_system[0])

    cut = 0
    # For loop as intended
    for x, y in moves:
        new_coordinate_system[int(x)][int(y)] = 3

    for row in new_coordinate_system:
        for i in row:
            if i == 3:
                cut += 1
            elif i == 2:
                total -= 1

    return new_coordinate_system, cut, total


# output plot that shows lines and cut squares
def color_print(plot_map, time, path, cut, total, name):
    color_map = plot_map.copy()

    col_map = ListedColormap(['white', 'yellow', 'black', 'red'], 'indexed')

    plt.pcolormesh(color_map, edgecolors='k', linewidth=0.1, cmap=col_map)

    plt.figtext(0.5, 0.01, f'After {round(time)} seconds, ' +
                f'{round(((cut/total) * 100), 2)}% of the lawn got cut' +
                f' ({cut}/{total})', ha='center', va='center')

    plt.title(f"Colored grid of simulated lawn {path}, {name}")

    # line_map()

    plt.axis('equal')


# plot that shows lines
def line_map(moves):
    x = []
    y = []
    for i in moves:
        y.append(i[0])
        x.append(i[1])

    plt.plot(x, y, linewidth=0.8, alpha=1)


# Find start location
def find_start(main_map):
    finder_map = main_map.copy()
    x_lenght = len(finder_map)
    y_lenght = len(finder_map[0])

    for x in range(x_lenght):
        for y in range(y_lenght):
            if finder_map[x][y] == 1:
                history(x, y)
                # print(x, y)
                return x, y


# Generates random direction for x and y
def direction():
    speed = 0.3

    angle = math.pi * 2 * random.uniform(0, 1)

    dx = math.cos(angle) * speed
    dy = math.sin(angle) * speed

    return dx, dy


# Mower moves
def move(x, y, timer, time_taken, move_map, multiplier, N):
    a_second = (1 / multiplier) / N

    dx, dy = direction()

    # print("Time to move!", "\tDirection in X:\t", dx, "\tDirection in Y:\t"
    #      , dy)
    while time_taken < timer:
        new_x = x + (dx / N)
        new_y = y + (dy / N)

        if new_x < 0 or new_x >= len(move_map):
            break
        if new_y < 0 or new_y >= len(move_map[0]):
            break
        if move_map[int(new_x)][int(new_y)] == 2:
            break

        x = new_x
        y = new_y
        history(x, y)
        time_taken += a_second
        # print(time_taken)
    turn_history.append([x, y])

    # print("Turns taken:", time_taken)
    return x, y, time_taken


# Main simulation, mower starts here
def main_sim(startx, starty, timer, map, multiplier, N):
    # print("The time is:", timer)
    seconds = 0
    x, y = startx, starty
    while seconds < timer:
        x, y, seconds = move(x, y, timer, seconds, map, multiplier, N)
        # print("Time taken:", seconds, "Timer:", timer)
    return seconds


"""
Main
"""
os.system("cls")

# timer = 2
timer = float(input("For how long should the mower cut? (In hours) "))
name = input("Name of .csv file: ")
scaler = int(input("How much should map be scaled by? "))
repeats = int(input("How many simulations should be ran? "))
N = 10

timer = timer * 60 * 60
count = 0

best_cut_total = 0
worst_cut_total = 10**1000

coverage_history = []
cut_history = []
best_cut = []
best_move = []
worst_cut = []
worst_move = []

while count < repeats:
    move_history = []
    turn_history = []

    row_list, path, scaler = map_gen(name, scaler)
    cord_map = row_list.copy()
    cord_map.reverse()

    startx, starty = find_start(cord_map)
    # print("Starting X:", starty, "\t", "Starting Y:", startx)

    time_taken = main_sim(startx, starty, timer, cord_map, scaler, N)

    coverage_map, cut, total = coverage(cord_map, move_history)

    # total = color_print(coverage_map, time_taken, path, cut)

    # print(f"Amount of turns: {len(turn_history)}")

    # plt.show()

    if cut > best_cut_total:
        best_cut_total = cut
        best_cut = coverage_map.copy()
        best_move = move_history.copy()
    elif cut < worst_cut_total:
        worst_cut_total = cut
        worst_cut = coverage_map.copy()
        worst_move = move_history.copy()

    coverage_perc = (cut/total) * 100
    cut_history.append(cut)
    coverage_history.append(coverage_perc)

    count += 1

average = sum(coverage_history) / len(coverage_history)

variance = sum([((x - average) ** 2) for x in coverage_history])
standard_deviation = math.sqrt(variance / len(coverage_history))

print(f"Average: {round(average)}% cut, Standard deviation: " +
      f"{round(standard_deviation, 4)}%")


print("Showing best cut!")
name = "Best cut"
coverage_map, cut, total = coverage(best_cut, best_move)
color_print(best_cut, time_taken, path, cut, total, name)
line_map(best_move)
plt.show()

print("Showing worst cut!")
name = "Worst cut"
coverage_map, cut, total = coverage(worst_cut, worst_move)
color_print(worst_cut, time_taken, path, cut, total, name)
line_map(worst_move)
plt.show()
