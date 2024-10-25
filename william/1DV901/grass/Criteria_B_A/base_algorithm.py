import random
import math
from visuals import visualize_movement_map as vimp
from visuals import pixel_map
from visuals import pixel_map_coverage as pcm


def read_data(file, multiplier) -> list:
    with open(file, "r") as file:
        lines = file.readlines()

    data = []
    for i in range(len(lines[0].strip().split(","))):
        data.append(list())
    for i in range(len(lines)-1, -1, -1):
        row_data = [item.strip() for item in lines[i].strip().split(",")]
        for char in range(len(row_data)):
            value = ""
            if row_data[char] == "L":
                value = 0
            elif row_data[char] == "S":
                value = 1
            else:
                value = 2
            data[char].append(value)

    new_lst = []
    for i in range(len(data) * multiplier):
        new_lst.append(list())
    for j in range(len(new_lst)):
        for k in range(len(data[0]) * multiplier):
            new_lst[j].append(data[int(j/multiplier)][int(k/multiplier)])

    return new_lst


def get_boundaries(lst):
    boundaries = []
    for i in range(len(lst) + 2):
        boundaries.append([i-1, -1])
        boundaries.append([i-1, len(lst[0])])
    for i in range(len(lst[0]) + 2):
        boundaries.append([len(lst), i-1])
        boundaries.append([-1, i-1])
    for lists in range(len(lst)):
        for elements in range(len(lst[0])):
            if (lst[lists][elements] == 2):
                boundaries.append([lists, elements])
    return boundaries


def change_cordinate(cordinate, lst):
    if not lst[int(cordinate[0])][int(cordinate[1])] == 2:
        lst[int(cordinate[0])][int(cordinate[1])] = 3
    return lst


def hit_wall(cordinate, boundaries, angle, last_pos, lst, direction):
    if [int(cordinate[0]), int(cordinate[1])] in boundaries:
        cordinate = last_pos
        direction = [1, 1]
        angle = random.uniform(0, 2*math.pi)
    return cordinate, angle, direction


def find_start(data) -> list[int]:
    for col in range(len(data)):
        for row in range(len(data[0])):
            if (data[col][row] == 1):
                start_cordinate = [col, row]
                return start_cordinate
    return [0, 0]


def change_position(speed, direction,
                    angle, current_pos, delta_t):

    current_pos[0] += speed*direction[0]*math.cos(angle) * delta_t
    current_pos[1] += speed*direction[1]*math.sin(angle) * delta_t
    return current_pos


def main(path, multiplier, minutes, max_percentage, condition, delta_t, show):
    percentage = 0

    lst = read_data(path, multiplier)
    start_cordinate = find_start(lst)
    boundaries = get_boundaries(lst)

    const_map = [list(row) for row in lst]
    current_pos = list(start_cordinate)
    speed = 0.3

    direction = [1, 1]
    angle = math.pi/2
    actual_time = 0
    last_pos = list(start_cordinate)
    movement_history = [[start_cordinate[0], start_cordinate[1]]]
    max_time = minutes * 60

    start_un_cut = 0
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if lst[row][col] == 1:
                lst[row][col] = 0

            if lst[row][col] == 0:
                start_un_cut += 1
    un_cut = start_un_cut
    percentage = 0
    available_conditions = {1: actual_time < max_time,
                            0: percentage < max_percentage}
    while available_conditions[condition]:
        un_cut = 0

        current_pos, angle, direction = hit_wall(current_pos, boundaries,
                                                 angle, last_pos,
                                                 lst, direction)

        last_pos = list(current_pos)
        movement_history.append([(current_pos[0]), (current_pos[1])])
        lst = change_cordinate(current_pos, lst)

        current_pos = change_position(speed, direction, angle, current_pos,
                                      delta_t)
        actual_time += delta_t/multiplier

        for lists in range(len(lst)):
            if 0 in lst[lists]:
                un_cut += lst[lists].count(0)

        if condition == 1:
            available_conditions[1] = actual_time < max_time
        else:
            available_conditions[0] = percentage < max_percentage

        percentage = 100 - ((un_cut / start_un_cut) * 100)

    if show:
        vimp(movement_history, multiplier)
        pixel_map(const_map, multiplier)
        pcm(lst, actual_time, round(percentage, 2),
            (start_un_cut - un_cut), start_un_cut)
    return percentage, actual_time
