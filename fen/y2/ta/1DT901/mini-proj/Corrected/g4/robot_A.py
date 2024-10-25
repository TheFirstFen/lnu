import os
import math
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random as rnd
import numpy as np
import statistics as sts


DELTA = 0.1
FILE_NAME = "/egen.csv"
PLOT_NAME = FILE_NAME[1:-4]  # to use in plot and trace plot
SCALE = 5  # the amount of pixels
DAYS = 3  # how many days is evry run
GROWING_RATE = 4  # procent uppväxet per dag
CUTTING_TIME_PER_DAY = 90
AMOUNT_OF_RUNS = 2  # antalet runs hela koden kommer köras
COUNTER = []  # variable that preserv the count of cutted pixel
V = 0.3


def csv_file_reader():
    """Read the csv file and create a 2D array."""
    data_map = []
    path = os.getcwd()
    full_path = path + FILE_NAME

    with open(full_path, "r") as file:
        for line in file:
            line = line.strip().replace(",", " ").split()
            data_map.append(line)

    return data_map


def converted_csv_map():
    """Invert the x, y axes to handle them as a coordinate system."""
    data_map = csv_file_reader()
    final_map = [list(row[::-1]) for row in zip(*data_map)]
    return final_map


def str_to_int(map):
    """Convert characters in the map to integers."""
    map.reverse()
    y = len(map)
    x = len(map[0])
    for i in range(y):
        for j in range(x):
            if map[i][j] == "O":
                map[i][j] = 0
            elif map[i][j] == "L":
                map[i][j] = 1
            elif map[i][j] == "S":
                map[i][j] = 2
    uniq_element = []
    for elem in map:
        if elem not in uniq_element:
            uniq_element.append(elem)
    return map, x, y, uniq_element


def main(map_csv, inverted_map, str_2_int):

    def map_plot(str_2_int):
        """Plot the map."""
        int_map, x, y, uniq_element = str_2_int
        if len(uniq_element) == 2:
            color = ListedColormap(['green', 'yellow'], 'indexed')
        else:
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

    def general_map(map):
        """Find the coordinates of a specific element in the map."""
        counter_row = -1
        for row in map:
            counter_row += 1
            counter_tile = -1
            for tile in row:
                counter_tile += 1
                if tile == 'S':
                    return counter_row, counter_tile

    def is_outside(x, y):
        """"Check if coordinates are outside the
          map boundaries or on an obstacle"""
        if x < 0.0 or x >= len(inverted_map):
            return True
        if y < 0.0 or y >= len(inverted_map[0]):
            return True
        if inverted_map[int(x)][int(y)] == "O":
            return True
        return False

    def random_bounce():
        """Generate random bouncing angles for movement"""
        bi = math.pi
        rnd_angle = rnd.uniform(0, 2 * bi)
        vx_ny = V * math.cos(rnd_angle)
        vy_ny = V * math.sin(rnd_angle)
        return vx_ny, vy_ny

    def new_position():
        """Simulate movement and return a list of positions"""
        x, y = general_map(inverted_map)
        step_lst = [(x, y)]
        vx, vy = random_bounce()
        mille_sec = ((CUTTING_TIME_PER_DAY * 60)/0.1)

        for _ in range(int(mille_sec)):
            x, y = step_lst[-1]
            while True:
                ny_x = x + (vx * DELTA)
                ny_y = y + (vy * DELTA)
                if not is_outside(ny_x, ny_y):
                    step_lst.append((ny_x, ny_y))
                    break
                else:
                    vx, vy = random_bounce()

        return step_lst

    def pixel_map(map_csv):
        """Create a pixel map based on the CSV map"""
        original_height = len(map_csv)
        original_width = len(map_csv[0])

        pixel_height = original_height * SCALE
        pixel_width = original_width * SCALE

        pixel_map = [
            [0 for _ in range(pixel_width)]
            for _ in range(pixel_height)
        ]

        for i in range(original_height):
            for j in range(original_width):
                original_value = map_csv[i][j]

                pixel_value = 0

                if original_value == 0:
                    pixel_value = 0
                elif original_value == 2 or original_value == 1:
                    pixel_value = 1

                for x in range(i * SCALE, (i + 1) * SCALE):
                    for y in range(j * SCALE, (j + 1) * SCALE):
                        pixel_map[x][y] = pixel_value
        return pixel_map

    def creat_trace():
        """Create a trace of visited coordinates during movement"""
        step_lst = new_position()
        x, y = zip(*step_lst)
        unique_tuples = set()
        visited_cord = []

        for step in step_lst:
            x, y = step
            x = math.floor(x * 5)
            y = math.floor(y * 5)
            step = (x, y)
            if step not in unique_tuples:
                unique_tuples.add(step)
                visited_cord.append(step)
        return visited_cord

    def trace_coverage():
        """Generate a pixel map with the trace coverage and display it"""
        int_map, x, y, uniq_element = str_2_int
        trace_position = creat_trace()
        pixel = pixel_map(map_csv)

        for step in trace_position:
            i, j = step
            pixel[j][i] = 2

        xx = len(pixel[0])
        yy = len(pixel)
        total_pixels = xx * yy
        counter_cut = 0
        counter_obstacle = 0

        for row in pixel:
            for pixel_value in row:
                if pixel_value == 2:
                    counter_cut += 1
                elif pixel_value == 0:
                    counter_obstacle += 1

        if len(uniq_element) == 2:
            color = ListedColormap(['white', 'red'], 'indexed')
        else:
            color = ListedColormap(['black', 'white', 'red'], 'indexed')
        coverage_percentage = round(
            (counter_cut / (total_pixels - counter_obstacle)) * 100
        )
        plt.figure(figsize=(7, 7))  # Adjust the width and height as needed
        plt.pcolormesh(pixel, edgecolors='k', linewidth=2, cmap=color)
        ax = plt.gca()
        ax.set_yticks(np.arange(0, yy + 1, SCALE))
        ax.set_xticks(np.arange(0, xx + 1, SCALE))
        plt.title(f"Cordinate size {yy}x{xx}")
        # Add text to display the coverage percentage under the graph
        text_1 = f"{counter_cut} out of "
        text_2 = f"{total_pixels-counter_obstacle} ==> {coverage_percentage}%"
        plt.xlabel(f"{text_1}{text_2}")
        plt.show()

        return pixel
    pixel = trace_coverage()

    def regrow_pixels(pixel, flips_per_day):
        """Simulate the regrowth of pixels on the map"""
        regrow_tuples_lst = []
        x = len(pixel[0])
        y = len(pixel)

        cutted_grass = 0
        for i in pixel:
            for j in i:
                if j == 2:
                    cutted_grass += 1

        regrowing_pixels = (flips_per_day / 100) * cutted_grass

        # ensure that the map is not empty
        if cutted_grass <= regrowing_pixels:
            print("The regrowing rate larger than cutting rate ")
            exit()
            # need to stop the program

        while regrowing_pixels > 0:
            x_pixel = rnd.randint(0, x - 1)
            y_pixel = rnd.randint(0, y - 1)

            if pixel[y_pixel][x_pixel] == 2:
                pix_cord = (y_pixel, x_pixel)

                if pix_cord not in regrow_tuples_lst:
                    regrow_tuples_lst.append(pix_cord)
                    regrowing_pixels -= 1
        return regrow_tuples_lst

    def progress_map(pixel):
        """Simulate the progress of cutting and regrowing pixels on the map"""
        int_map, x, y, uniq_element = str_2_int

        for i in range(DAYS):
            grow_pixel = regrow_pixels(pixel, GROWING_RATE)
            n_trace = creat_trace()

            for grow in grow_pixel:
                grow_y, grow_x = grow
                if pixel[grow_y][grow_x] == 2:
                    pixel[grow_y][grow_x] = 1

            for step in n_trace:
                ny_x, ny_y = step
                if pixel[ny_y][ny_x] == 1:
                    pixel[ny_y][ny_x] = 2

            cutted_grass = 0
            for i in pixel:
                for j in i:
                    if j == 2:
                        cutted_grass += 1
            COUNTER.append(cutted_grass)

        x_x = len(pixel[0])
        y_y = len(pixel)
        total_pixels = x_x * y_y
        total_cut = 0
        counter_obstacle = 0

        for row in pixel:
            for pixel_value in row:
                if pixel_value == 2:
                    total_cut += 1
                elif pixel_value == 0:
                    counter_obstacle += 1

        if len(uniq_element) == 2:
            color = ListedColormap(['black', 'red'], 'indexed')
        else:
            color = ListedColormap(['black', 'white', 'red'], 'indexed')
        coverage_percentage = round(
            (total_cut / (total_pixels - counter_obstacle)) * 100)

        plt.figure(figsize=(7, 7))  # Adjust the width and height as needed
        plt.pcolormesh(pixel, edgecolors='k', linewidth=2, cmap=color)
        ax = plt.gca()
        ax.set_yticks(np.arange(0, y_y + 1, SCALE))
        ax.set_xticks(np.arange(0, x_x + 1, SCALE))
        plt.title(f"Cordinate size {y_y}x{x_x}")
        text_1 = f"Day {DAYS}: {total_cut} out of "
        text_2 = f"{total_pixels-counter_obstacle} pixels cut =>"
        text_3 = f"{coverage_percentage}% coverage"
        plt.xlabel(f"{text_1}{text_2}{text_3}")
        plt.show()

        return COUNTER, x_x, y_y

    def plot_diagram():
        """Plot the diagram of the cut pixels over the simulation period"""
        counter, x, y = progress_map(pixel)
        procent_cut = [(i / (x * y)) * 100 for i in counter]

        xxx = list(range(1, DAYS + 1))
        yyy = procent_cut[:DAYS]

        plt.plot(xxx, yyy, marker='o', linestyle='-')
        plt.xlabel("Number of Days")
        plt.ylabel("Percentage of Cut")
        plt.title(f"Percentage of Cut After {DAYS} days")

        # Add labels with exact percentage values at each point
        for day, percent in zip(xxx, yyy):
            plt.text(day, percent, f'{percent:.2f}%', ha='right', va='bottom')

        plt.grid(True)
        plt.show()
        return counter[-1]
    cuted_pixels = plot_diagram()
    return cuted_pixels


# Call the main function
std = []
for _ in range(AMOUNT_OF_RUNS):
    map_csv = csv_file_reader()
    inverted_map = converted_csv_map()
    str_2_int = str_to_int(map_csv)
    total_cut = main(map_csv, inverted_map, str_2_int)
    std.append(total_cut)

mean = sts.mean(std)
std_deviation = sts.stdev(std)
percentage_deviation = (std_deviation / mean) * 100

print(f"Total cut after {DAYS} days: {total_cut}")
print(f"Standard devition of the map '{PLOT_NAME}' after", end="")
print(f" {AMOUNT_OF_RUNS} simulations with {CUTTING_TIME_PER_DAY/60}", end="")
print(f" hours coverage is ±{round(percentage_deviation, 2 )}%")
print(f"Mean of the cutted pixels of the map '{PLOT_NAME}' after", end="")
print(f" {AMOUNT_OF_RUNS} simulations with {CUTTING_TIME_PER_DAY/60}", end="")
print(f" hours coverage is {round(mean, 2)}")
