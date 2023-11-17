import os
import matplotlib.pyplot as plt
import random
import math
# Constants
N = 4  # Each cell divided into 5 new cell
v = 0.3  # LawnMover speed
delta_t = 0.1
new_map = None


def read_map(path):
    lst = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            # split by comma, strip whitespace
            row = line.strip('[]\n').split(',')
            lst.append(row)
    return lst[::-1]


def one_step(x, y, vx, vy):
    while True:
        # Calculate position according to xi+1 = xi + vx∆t (1) yi+1 = yi + vy∆t
        xu = x + vx * delta_t
        yu = y + vy * delta_t

        if not is_outside(xu, yu):
            return xu, yu, vx, vy

        # Generate a new random velocity
        alpha = random.uniform(0, 2 * math.pi)
        vx = v * math.cos(alpha)
        vy = v * math.sin(alpha)


def is_outside(x, y):
    global obstacle_pos
    outside = False
    rows = len(ground_map)
    cols = len(ground_map[0])
    obstacles = (int(x), int(y)) in obstacle_pos
    if x < 0 or x > cols or y < 0 or y > rows or obstacles:
        outside = True
    return outside


def find_position(lst):
    start_pos = None
    obstacle_pos = []
    lawn_pos = []
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            cell = lst[y][x]
            if cell == 'S':
                start_pos = (x, y)
            elif cell == 'O':
                obstacle_pos.append((x, y))
            elif cell == 'L':
                lawn_pos.append((x, y))
    return start_pos, obstacle_pos, lawn_pos


# convert the original map to NxN
def converted_map(lst):
    global new_map  # Set new_map as a global variable
    # Grid data
    # calculates the number of rows in the grid
    rows = len(lst)
    # calculates the number of columns
    cols = len(lst[0])

    # Calculate the new grid
    # Each cell into 5 new cells
    new_rows = rows * N
    new_cols = cols * N

    # New grid
    new_grid = []

    for y in range(new_rows):
        new_row = []
        for x in range(new_cols):
            # Calculate new position
            old_x = x // N
            old_y = y // N

            new_cell = lst[old_y][old_x]
            # Append new cell value to the current row
            new_row.append(new_cell)
        # Append new_row to the current row
        new_grid.append(new_row)

    new_map = new_grid  # Assign the result to new_map


def plot_grid(lst):
    # Create grid data
    rows = len(lst)
    cols = len(lst[0])

    for y in range(rows):
        for x in range(cols):
            cell = lst[y][x]
            if cell == 'S':
                color = 'yellow'
            elif cell == 'O':
                color = 'black'
            elif cell == 'L':
                color = 'green'
            elif cell == 'V':
                color = 'red'
            else:
                color = 'white'

            plt.fill_between([x, x+1], y, y+1, color=color, edgecolor='k')

    # Fine-tune plot layout
    ax = plt.gca()
    ax.set_yticks(range(0, rows + 1, 1))
    ax.set_xticks(range(0, cols + 1, 1))
    plt.title(f"Colored grid of size {rows}x{cols}")
    plt.show()


# 2 hour sim
def simulate_trace():
    # Starting point and verosity
    start_x, start_y = start_pos
    start_vx = 0.3
    start_vy = 0.3

    # Calculate the number of steps for a 30-minute simulation
    sim_minutes = 120
    steps = int(sim_minutes * 60 / delta_t)

    # Trace starting point
    trace = [(start_x, start_y)]

    x, y, vx, vy = start_x, start_y, start_vx, start_vy

    for step in range(steps):
        # Calculate trace for each step, append to the lst
        x, y, vx, vy = one_step(x, y, vx, vy)
        trace.append((x, y))

    return trace


def coverage(lst):
    # Copy of the original map
    rows = len(new_map)
    cols = len(new_map[0])
    origin_map = []

    for y in range(rows):
        origin_row = []
        for x in range(cols):
            origin_row.append(new_map[y][x])
        origin_map.append(origin_row)

    for x, y in lst:
        x_scaled, y_scaled = int(x * N), int(y * N)  # Scale the coord by N
        origin_map[y_scaled][x_scaled] = 'V'

    return origin_map


def plot_trace(lst):
    # storing x, y
    x = []
    y = []

    for i in lst:
        x.append(i[0] * N)  # Scale the x position by N
        y.append(i[1] * N)  # Scale the y position by N

    # Plot the trace on the converted map
    plot_grid(new_map)

    # Plot the trace of 2-hour simulation
    plt.plot(x, y)
    plt.title('Lawnmower path after 2 Hours')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    # Show the plot
    plt.show()


# calculate percentage of visited/total cells
def percentage(lst):
    total = 0
    visited = 0
    row = len(lst)
    cols = len(lst[0])
    total = row * cols
    obstacle = 0
    for row in lst:
        visited += row.count('V')
        obstacle += row.count('O')
    total = total - obstacle
    coverage_percentage = (visited / total) * 100
    return coverage_percentage, visited, total


def plot_final(lst):
    # Create grid data
    rows = len(lst)
    cols = len(lst[0])

    for y in range(rows):
        for x in range(cols):
            cell = lst[y][x]
            if cell == 'V':
                color = 'red'
            elif cell == 'O':
                color = 'black'
            else:
                color = 'white'

            plt.fill_between([x, x+1], y, y+1, color=color, edgecolor='k')

    # Get coverage percentage, visited, total
    percent, visited, total = percentage(coverage_map)

    # Title
    plt.title(f"{visited} out of {total} ==> {percent:.2f}%")

    # Fine-tune plot layout
    ax = plt.gca()
    ax.set_yticks(range(0, rows + 1, 1))
    ax.set_xticks(range(0, cols + 1, 1))
    plt.show()


path = os.getcwd() + '\\mini-project\\ground_maps\\small.csv'
ground_map = read_map(path)

# Position
start_pos, obstacle_pos, lawn_pos = find_position(ground_map)

# Plot map
plot_map = plot_grid(ground_map)

# Convert ground map
converted_map(ground_map)

# Simulate
trace = simulate_trace()
print(len(trace))

coverage_map = coverage(trace)

# Plot the trace on the converted map
plot_trace(trace)  # Plot the trace on the converted map

# Plot coverage
plot_final(coverage_map)
