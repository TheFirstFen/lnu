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
def coverage(cut_map):
    # new_coordinate_system = cut_map.copy()
    total = len(cut_map) * len(cut_map[0])

    cut = 0

    for row in cut_map:
        for i in row:
            if i == 3:
                cut += 1
            elif i == 2:
                total -= 1

    return cut, total


# Function to change the cut lawn
def coordinatechange(x, y, map, cut, total):
    if map[int(x)][int(y)] == 0:
        map[int(x)][int(y)] = 3
        cut += 1
    elif map[int(x)][int(y)] == 1:
        map[int(x)][int(y)] = 3
        cut += 1
    cover = ((cut/total) * 100)
    return cut, cover


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
                return x, y


# Generates random direction for x and y
def direction():
    speed = 0.3

    angle = math.pi * 2 * random.uniform(0, 1)

    dx = math.cos(angle) * speed
    dy = math.sin(angle) * speed

    return dx, dy


# Mower moves
def move(x, y, timer, time_taken, move_map, multiplier, N, cover, choice,
         percent, cut, total):
    cover = ((cut/total) * 100)
    a_second = (1 / multiplier) / N

    dx, dy = direction()

    count = 0
    least_tries = random.randint(N ** 2, N ** 4)

    if choice == 1:
        while time_taken < timer:
            new_x = x + (dx / N)
            new_y = y + (dy / N)

            if new_x < 0 or new_x >= len(move_map):
                return x, y, time_taken, cover, cut
            if new_y < 0 or new_y >= len(move_map[0]):
                return x, y, time_taken, cover, cut
            if move_map[int(new_x)][int(new_y)] == 2:
                return x, y, time_taken, cover, cut

            x = new_x
            y = new_y
            history(x, y)
            cut, cover = coordinatechange(x, y, move_map, cut, total)
            time_taken += a_second
            count += 1
            if count == least_tries:
                return x, y, time_taken, cover, cut
    elif choice == 2:
        while cover < percent:
            new_x = x + (dx / N)
            new_y = y + (dy / N)

            if new_x < 0 or new_x >= len(move_map):
                return x, y, time_taken, cover, cut
            if new_y < 0 or new_y >= len(move_map[0]):
                return x, y, time_taken, cover, cut
            if move_map[int(new_x)][int(new_y)] == 2:
                return x, y, time_taken, cover, cut

            x = new_x
            y = new_y
            history(x, y)
            cut, cover = coordinatechange(x, y, move_map, cut, total)
            time_taken += a_second
            count += 1
            if count == least_tries:
                return x, y, time_taken, cover, cut

    return x, y, time_taken, cover, cut


# Main simulation, mower starts here
def main_sim(startx, starty, timer, map, multiplier, N, choice, percent):
    cut, total = coverage(map)
    cover = ((cut/total) * 100)
    seconds = float(0)
    if choice == 1:
        x, y = startx, starty
        while seconds < timer:
            turn_history.append([x, y])
            x, y, seconds, cover, cut = move(x, y, timer, seconds, map,
                                             multiplier, N, None, choice,
                                             percent, cut, total)
        return seconds, map
    elif choice == 2:
        x, y = startx, starty
        while cover < percent:
            turn_history.append([x, y])
            x, y, seconds, cover, cut = move(x, y, timer, seconds, map,
                                             multiplier, N, cover, choice,
                                             percent, cut, total)
        return seconds, map


"""
Main
"""
os.system("cls")

percent = 0
timer = 0
choice = False
while choice is False:
    choice = int(input("Should the lawn mower be run based on time (1) or" +
                       "coverage(2)? "))
    if choice != 1 and choice != 2:
        choice = False
    elif choice == 1:
        timer = float(input("For how long should the mower cut? (In hours) "))
        timer = timer * 60 * 60
    elif choice == 2:
        percent = float(input("What percent coverage should lawnmower get" +
                              " before stopping? "))

name = input("Name of .csv file: ")
scaler = int(input("How much should map be scaled by? "))
repeats = int(input("How many simulations should be ran? "))
N = 10

count = 0
total_time = 0
best_cut_total = 0
worst_cut_total = 10**1000
best_time = 10**1000
worst_time = 0

coverage_history = []
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

    time_taken, current_map = main_sim(startx, starty, timer, cord_map, scaler,
                                       N, choice, percent)
    total_time += time_taken
    cut, total = coverage(cord_map)

    # total = color_print(coverage_map, time_taken, path, cut)

    # plt.show()

    if choice == 1:
        if cut > best_cut_total:
            best_cut_total = cut
            best_cut = current_map.copy()
            best_move = move_history.copy()
            best_time = time_taken
        if cut < worst_cut_total:
            worst_cut_total = cut
            worst_cut = current_map.copy()
            worst_move = move_history.copy()
            worst_time = time_taken
    elif choice == 2:
        if time_taken < best_time:
            best_cut_total = cut
            best_cut = current_map.copy()
            best_move = move_history.copy()
            best_time = time_taken
        if time_taken > worst_time:
            worst_cut_total = cut
            worst_cut = current_map.copy()
            worst_move = move_history.copy()
            worst_time = time_taken

    coverage_perc = (cut/total) * 100
    coverage_history.append(coverage_perc)

    count += 1
    print(f"Run {count} done!")

average_time = total_time / count
average = sum(coverage_history) / len(coverage_history)

variance = sum([((x - average) ** 2) for x in coverage_history])
standard_deviation = math.sqrt(variance / len(coverage_history))

print(f"Average: {round(average)}% cut, Standard deviation: " +
      f"{round(standard_deviation, 4)}% with an average time of" +
      f" {round(average_time)} seconds.")


print("Showing best cut!")
name = "Best cut"
cut, total = coverage(best_cut)
color_print(best_cut, best_time, path, cut, total, name)
line_map(best_move)
plt.show()

print("Showing worst cut!")
name = "Worst cut"
cut, total = coverage(worst_cut)
color_print(worst_cut, worst_time, path, cut, total, name)
line_map(worst_move)
plt.show()
