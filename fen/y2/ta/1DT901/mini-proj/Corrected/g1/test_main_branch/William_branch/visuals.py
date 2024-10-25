import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap as Lcm


# splits cords into x cordinates and y cordinates
def split_coords(cords):
    x_values = [c[0] for c in cords]
    y_values = [c[1] for c in cords]
    return x_values, y_values


def reduced_data(data, divider, big_reduced=True):
    reduced_movement_path = []

    # Reduces the robot movement coordinates before pixel adaptation
    for cell in range(len(data)):
        x_coordinate = data[cell][0] / divider
        y_coordinate = data[cell][1] / divider
        reduced_movement_path.append([x_coordinate, y_coordinate])
    print(reduced_movement_path)
    return reduced_movement_path


# creates the visualzation for the boundary and robo
def visualize_movement_map(robo_coords, divider, has_back=False,
                           reverse_movement=[]):

    reduced_movement_path = reduced_data(robo_coords, divider, False)
    #print(reduced_movement_path)
    x_coords_robo, y_coords_robo = split_coords(reduced_movement_path)
    plt.plot(x_coords_robo, y_coords_robo)
    if has_back:
        reduced_reverse = reduced_data(reverse_movement, divider, False)

        x_coords_back, y_coords_back = split_coords(reduced_reverse)

        plt.plot(x_coords_robo, y_coords_robo, 'b',
                 x_coords_back, y_coords_back, 'r--')
    else:
        plt.plot(x_coords_robo, y_coords_robo, 'b')
    plt.show()


# reverts the columns into rows and rows into columns
def transpose_data(data):
    num_rows = len(data)
    num_columns = len(data[0])

    transposed_data = []
    for column in range(num_columns):
        transposed_row = []
        for row in range(num_rows):
            transposed_row.append(data[row][column])
        transposed_data.append(transposed_row)

    return transposed_data


def pixel_map(data, divider):
    fig, ax = plt.subplots()
    has_obstacles = False
    for col in data:
        if 2 in col:
            has_obstacles = True
            break

    if has_obstacles:
        colors = {0: 'green', 1: 'yellow', 2: 'black'}
        cmap = Lcm([colors[0], colors[1], colors[2]], 'indexed')
    else:
        colors = {0: 'green', 1: 'yellow'}
        cmap = Lcm([colors[0], colors[1]], 'indexed')

    # Your custom transpose function
    data = transpose_data(data)

    # Reduce the size of the data using the divider
    reduced_data = []
    for row in range(0, len(data), divider):
        reduced_row = []
        for col in range(0, len(data[row]), divider):
            reduced_row.append(data[row][col])
        reduced_data.append(reduced_row)

    # Get the dimensions of the reduced data
    rows = len(reduced_data)
    cols = len(reduced_data[0])

    ax.pcolormesh(reduced_data, edgecolors="k", linewidth=2, cmap=cmap)
    ax.set_aspect('equal', adjustable='box')
    plt.title(f"Colored grid of size {rows}x{cols}")
    plt.show()


# splits the time into hours, minutes and seconds
def get_time(past_time):
    hours, minutes, seconds = 0, 0, 0

    hours = past_time // 3600
    minutes = (past_time % 3600) // 60
    seconds = round(past_time % 60, 2)

    return hours, minutes, seconds


def pixel_map_coverage(data, past_time, coverage, uncut, allcut):

    time_slots = get_time(past_time)

    # Change the colors depending on the coverage
    if uncut == allcut:
        colors = {2: 'black', 3: 'red'}
        cmap = Lcm([colors[2], colors[3]], 'indexed')
    elif uncut != 0:
        colors = {0: 'white', 2: 'black', 3: 'red'}
        cmap = Lcm([colors[0], colors[2], colors[3]], 'indexed')
    else:
        colors = {0: 'white', 2: 'black'}
        cmap = Lcm([colors[0], colors[2]])
    data = transpose_data(data)
    # Create grid data based on the length and width of your data
    rows = len(data)
    cols = len(data[0])

    # Create a list of where all the different colors will go
    plot_map = [[list(colors.keys()).index(data[row][col])
                 for col in range(cols)] for row in range(rows)]

    fig, ax = plt.subplots()
    ax.pcolormesh(plot_map, edgecolors='k', linewidth=1, cmap=cmap)
    ax.set_aspect('equal', adjustable='box')
    ax = plt.gca()

    ax.set_yticks(range(0, (rows + 1), 1))
    ax.set_xticks(range(0, (cols + 1), 1))
    ax.tick_params(axis='both', labelsize=3)
    plt.title(f"Grid size {rows}x{cols}")
    plt.xlabel(f"Visited {uncut} out of {allcut}" +
               f" ==> {coverage}% " +
               f"after {time_slots[0]} hour(s) {time_slots[1]} minute(s)"
               f" {time_slots[2]} second(s)")

    plt.show()
