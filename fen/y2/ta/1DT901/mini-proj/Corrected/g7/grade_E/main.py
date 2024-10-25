import os
import matplotlib.pyplot as plt
import random
import math
# Constants
N = 5  # Each cell divided into 5 new cell
v = 0.3  # LawnMover speed
delta_t = 1


def read_map(path):
    lst = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            # split by comma, strip whitespace
            row = line.strip('[]\n').split(',')
            lst.append(row)
    return lst[::-1]


def one_step(x, y, vx, vy):
    # Calculate position acording to xi+1 = xi + vx∆t (1) yi+1 = yi + vy∆t
    xu = x + vx * delta_t
    yu = y + vy * delta_t

    # If outside or obstacle
    while is_outside(xu, yu):
        # Generate a new random velocity
        alpha = random.uniform(0, 2 * math.pi)
        vx = v * math.cos(alpha)
        vy = v * math.sin(alpha)
        # New positions
        xu = x + vx * delta_t
        yu = y + vy * delta_t
    return xu, yu, vx, vy


def is_outside(x, y):
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
    return new_grid


def lawn_trace(x0, y0, vx, vy):
    trace = []
    x, y = x0, y0
    while not is_outside(x, y):
        # Calculate the new position using one_step function
        x, y, vx, vy = one_step(x, y, vx, vy)

        # Append the current (x, y) position in the trace
        trace.append((x, y))

    return trace


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


# 30 min sim
def simulate_trace_30():
    # Starting point and verosity
    start_x, start_y = start_pos
    start_vx = 0.3
    start_vy = 0.3

    # Calculate the number of steps for a 30-minute simulation
    sim_minutes = 30
    steps = int(sim_minutes * 60 / delta_t)

    # Trace starting point
    trace = [(start_x, start_y)]

    x, y, vx, vy = start_x, start_y, start_vx, start_vy

    for step in range(steps):
        # Calculate trace for each step, append to the lst
        x, y, vx, vy = one_step(x, y, vx, vy)
        trace.append((x, y))

    return trace


# 15 min sim
def simulate_trace_15():
    # Starting point and verosity
    start_x, start_y = 0, 0
    start_vx = 0.3
    start_vy = 0.3

    # Calculate the number of steps for a 30-minute simulation
    sim_minutes = 15
    steps = int(sim_minutes * 60 / delta_t)

    # Trace starting point
    trace = [(start_x, start_y)]

    x, y, vx, vy = start_x, start_y, start_vx, start_vy

    for step in range(steps):
        # Calculate trace for each step, append to the lst
        x, y, vx, vy = one_step(x, y, vx, vy)
        trace.append((x, y))

    return trace


def plot_trace(lst):
    # storing x, y
    x = []
    y = []

    for i in lst:
        x.append(i[0])
        y.append(i[1])

    # Plot the trace of 30 min simulate
    plt.plot(x, y)
    plt.title('Lawnmover path after 15 Minutes')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    # Show the plot
    plt.show()


def plot_trace30(lst):
    # storing x, y
    x = []
    y = []

    for i in lst:
        x.append(i[0])
        y.append(i[1])

    # Plot the trace of 30 min simulate
    plt.plot(x, y)
    plt.title('Lawnmover path after 30 Minutes')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    # Show the plot
    plt.show()


path = os.getcwd() + '\\mini-project\\ground_maps\\simple.csv'
ground_map = read_map(path)

# plot map
plot_map = plot_grid(ground_map)

# Position
start_pos, obstacle_pos, lawn_pos = find_position(ground_map)

# Simulate 15/30
trace_15 = simulate_trace_15()
trace_30 = simulate_trace_30()

# Plot the trace
plot_trace(trace_15)
plot_trace30(trace_30)
