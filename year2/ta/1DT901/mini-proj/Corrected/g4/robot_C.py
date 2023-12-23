import os
import math
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random as rnd
import numpy as np

DELTA = 0.1  # delta time
FILE_NAME = "/data/small.csv"  # the ground map
PLOT_NAME = FILE_NAME[1:-4]  # to use in plot
TIME = 120  # to use in trace
SCALE = 5  # the amout of pixels
V = 0.3  # robot speed


# def to read the csv-files and creat a 2D array to use in other functions
def csv_file_reader():
    data_map = []
    path = os.getcwd()
    full_path = path + FILE_NAME

    with open(full_path, "r") as file:
        for line in file:
            line = line.strip().replace(",", " ").split()
            data_map.append(line)

    return data_map


# def to invert the x,y axels to handle them as cord-system
def converted_csv_map():
    data_map = csv_file_reader()
    final_map = [list(row[::-1]) for row in zip(*data_map)]
    return final_map


# def to convert from digits to to use in other functions
def str_to_int(map):
    map.reverse()
    y = len(map)  # reads the vertical planes
    x = len(map[0])  # reads the horizontal planes
    for i in range(y):
        for j in range(x):
            if map[i][j] == "O":  # ersätt opsticle med 0
                map[i][j] = 0
            elif map[i][j] == "L":  # ersätt gräss med 1
                map[i][j] = 1
            elif map[i][j] == "S":  # ersätt start_place med 2
                map[i][j] = 2
    uniq_element = []
    for elem in map:
        if elem not in uniq_element:
            uniq_element.append(elem)
    return map, x, y, uniq_element


# the main def
def main(map_csv, inverted_map, str_2_int):
    x_max = len(map_csv[0])
    y_max = len(map_csv)

    # def to plot the map
    def map_plot(str_2_int):
        int_map, x, y, uniq_element = str_2_int
        if len(uniq_element) == 2:
            color = ListedColormap(['green', 'yellow'], 'indexed')
        else:
            # visualisera 0 med black, gräss med grönn och start med gul
            color = ListedColormap(['black', 'green', 'yellow'], 'indexed')

        plt.figure()
        plt.pcolormesh(int_map, edgecolors='k', linewidth=2, cmap=color)
        ax = plt.gca()
        ax.set_yticks(np.arange(0, y+1, 1))
        ax.set_xticks(np.arange(0, x+1, 1))
        plt.title(f"Cordinate size {y}x{x}")
        plt.show()
        return uniq_element

    map_plot(str_2_int)

    # def to find the start cordinants
    def general_map(map):
        counter_row = -1
        for row in map:
            counter_row += 1
            counter_tile = -1
            for tile in row:
                counter_tile += 1
                if tile == 'S':
                    return counter_row, counter_tile

    # def to read the map to locate the grid and obstacles
    def is_outside(x, y):
        if x < 0.0 or x >= len(inverted_map):  # Check x boundaries
            return True
        if y < 0.0 or y >= len(inverted_map[0]):  # Check y boundaries
            return True
        if inverted_map[int(x)][int(y)] == "O":  # check for opsticle
            return True
        return False

    # def to generate random angles to explore new velocities
    def random_bounce():
        bi = math.pi
        rnd_angle = rnd.uniform(0, 2 * bi)  # generate a random angle
        vx_ny = V * math.cos(rnd_angle)  # new velocity for x
        vy_ny = V * math.sin(rnd_angle)  # new velocity for y
        return vx_ny, vy_ny

    # Clac the new position and return a list of steps
    def new_position():
        x, y = general_map(inverted_map)
        step_lst = [(x, y)]
        vx, vy = random_bounce()
        mille_sec = (TIME * 60)/0.1  # time for the equation

        for _ in range(int(mille_sec)):
            x, y = step_lst[-1]
            while True:
                ny_x = x + (vx * DELTA)  # new position for x
                ny_y = y + (vy * DELTA)  # new position for y
                if not is_outside(ny_x, ny_y):
                    step_lst.append((ny_x, ny_y))
                    break
                else:
                    vx, vy = random_bounce()

        return step_lst

    # def to create a coverage map out of the ground map
    def pixel_map(map_csv):
        original_height = len(map_csv)
        original_width = len(map_csv[0])

        # Calculate the dimensions of the pixel map
        pixel_height = original_height * SCALE
        pixel_width = original_width * SCALE

        # Create an empty pixel map with all pixels initially set to 0
        pixel_map = [
            [0 for _ in range(pixel_width)]
            for _ in range(pixel_height)
        ]

        # Fill in the pixel map based on the original map
        for i in range(original_height):
            for j in range(original_width):
                original_value = map_csv[i][j]

                pixel_value = 0  # Default value (e.g., '0')

                # You can set the value based on the original map here
                if original_value == 0:
                    pixel_value = 0  # For obstacles, for example
                elif original_value == 2 or original_value == 1:
                    pixel_value = 1  # For grass, for example

                # Fill in the corresponding pixels in the pixel map
                for x in range(i * SCALE, (i + 1) * SCALE):
                    for y in range(j * SCALE, (j + 1) * SCALE):
                        pixel_map[x][y] = pixel_value
        return pixel_map

    # def to plot the trace using list from new_postion
    def creat_trace():
        step_lst = new_position()
        x, y = zip(*step_lst)
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(f'Map name: {PLOT_NAME}, Time: {TIME} min')
        plt.xlim(0, x_max)
        plt.ylim(0, y_max)
        plt.show()
        unique_tuples = set()
        visited_cord = []

        for step in step_lst:
            x, y = step
            x = math.floor(x * SCALE)
            y = math.floor(y * SCALE)
            step = (x, y)
            # Check if the modified coordinates are
            # not in the set of unique tuples
            if step not in unique_tuples:
                unique_tuples.add(step)
                visited_cord.append(step)
        return visited_cord

    # def to crate a trace covrage
    def trace_coverage():
        int_map, x, y, uniq_element = str_2_int
        trace_position = creat_trace()
        pixel = pixel_map(map_csv)
        for step in trace_position:
            i, j = step
            pixel[j][i] = 2

        counter_cut = 0
        counter_obstacle = 0
        xx = len(pixel[0])
        yy = len(pixel)
        total_pixels = xx * yy

        for row in pixel:
            for pixel_value in row:
                if pixel_value == 2:  # means been cut
                    counter_cut += 1
                elif pixel_value == 0:  # means it's an opsticle
                    counter_obstacle += 1

        if len(uniq_element) == 2:
            color = ListedColormap(['white', 'red'], 'indexed')
        else:
            color = ListedColormap(['black', 'white', 'red'], 'indexed')
        # Calculate the coverage percentage
        coverage_percentage = round(
            (counter_cut / (total_pixels - counter_obstacle)) * 100
        )
        # Create the plot
        plt.figure(figsize=(7, 7))  # Adjust the width and height as needed
        plt.pcolormesh(pixel, edgecolors='k', linewidth=2, cmap=color)
        ax = plt.gca()
        ax.set_yticks(np.arange(0, yy + 1, SCALE))
        ax.set_xticks(np.arange(0, xx + 1, SCALE))
        plt.title(f"Cordinate size {yy}x{xx}")
        # Add text to display the coverage percentage under the graph
        text_1 = f"{counter_cut} out of {total_pixels-counter_obstacle} ==>"
        text_2 = f"{coverage_percentage}%"
        plt.xlabel(f"{text_1}{text_2}")
        plt.show()
    trace_coverage()


map_csv = csv_file_reader()
inverted_map = converted_csv_map()
str_2_int = str_to_int(map_csv)
main(map_csv, inverted_map, str_2_int)
