import matplotlib.pyplot as plt
import matplotlib.colors as col
import csv


def start_coordinates(ground_map):
    x, y = 0, 0
    for i in range(len(ground_map)):
        for j in range(len(ground_map[i])):
            if (ground_map[i][j] == 1):
                x, y = j, i
    return x, y


def read_csv_file_content_to_lst(csv_file_path):
    with open(csv_file_path, "r") as file:
        content = csv.reader(file)
        ground_map = list(content)
        return ground_map


def reverse_rows_list(lst):
    rev_row_lst = []
    for i in range(len(lst) - 1, -1, -1):
        rev_row_lst.append(lst[i])
    return rev_row_lst


def reverse_columns_list(lst):
    rev_col_list = []
    for i in range(0, len(lst)):
        col = []
        for j in range(len(lst[i]) - 1, -1):
            col.append(lst[i][j])
    return rev_col_list()


def shape_of_2d_list(arr):
    y_len = len(arr)
    x_len = len(arr[0])
    return y_len, x_len


def ground_map_to_num_array(ground_map):
    """
    Reads a ground map consisting of letters such that
    S is the starting point,
    O is an obstacle,
    L is an area of lawn to be mowed.

    Then converts it to a two-dimensional array/list (or matrix).
    """
    number_array = []
    for i in ground_map:
        ii = []
        for j in i:
            num = 0
            if j == "O":
                num = 2
            if j == "S":
                num = 1
            ii.append(num)
        number_array.append(ii)
    return number_array


def extend_array(arr, size_increase_factor):
    """
    """
    extended_grid_array = []
    for i in arr:
        for e in range(size_increase_factor):
            ii = []
            for j in i:
                for e1 in range(size_increase_factor):
                    ii.append(j)
            extended_grid_array.append(ii)

    return extended_grid_array


def obstacle_area(lst):
    """
    Calculates and returns the total area of obstacles in the map
    """
    area = 0
    for i in lst:
        for j in i:
            if j == 2:
                area += 1
    return area


def ground_map_visualization(map_colors, number_array,
                             map_area, area_to_mowe):
    y_len, x_len = shape_of_2d_list(number_array)
    cmap = col.ListedColormap(colors=map_colors)
    fig1, ax1 = plt.subplots()
    ax1.imshow(number_array, cmap=cmap, aspect=1,
               vmin=0, vmax=2, extent=[0, x_len, 0, y_len])
    plt.grid(True, which="both", color="k", linewidth=1.5)
    ax1.set_xticks([i for i in range(x_len + 1)],
                   labels=[i for i in range(x_len + 1)])
    ax1.set_yticks([i for i in range(y_len + 1)],
                   labels=[i for i in range(y_len + 1)])
    ax1.set_title("Map area: {} m^2, Lawn area: {} m^2".format(
        map_area, area_to_mowe))
    # plt.colorbar(ticks=[0, 1, 2])


def pixel_visualization(map_colors, number_array, visit_count, total_count):
    y_len, x_len = shape_of_2d_list(number_array)
    cmap = col.ListedColormap(colors=map_colors)
    fig1, ax1 = plt.subplots()
    ax1.imshow(number_array, cmap=cmap, aspect=1,
               vmin=0, vmax=2, extent=[0, x_len, 0, y_len])
    plt.grid(True, which="both", color="k", linewidth=1.5)
    ax1.set_xticks([i for i in range(x_len + 1)],
                   labels=[i for i in range(x_len + 1)])
    ax1.set_yticks([i for i in range(y_len + 1)],
                   labels=[i for i in range(y_len + 1)])
    coverage = 100 * visit_count / total_count
    ax1.set_title("{} out of {} ==> {}%".format(visit_count,
                  total_count, int(round(coverage, 0))))


def pixel_grid(ground_map):
    number_array = []
    for i in ground_map:
        ii = []
        for j in i:
            num = 0
            if j == "O":
                num = 2
            ii.append(num)
        number_array.append(ii)
    return number_array


def compute_coverage(extended_number_array):
    total_count = 0
    visit_count = 0
    for i in extended_number_array:
        for j in i:
            if j == 1:
                visit_count += 1
            if not (j == 2):
                total_count += 1
    return visit_count, total_count
