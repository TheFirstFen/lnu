import random
import math
import os
import time
from test_main_branch.visuals import visualize_movement_map as vimp
from test_main_branch.visuals import pixel_map
from test_main_branch.visuals import pixel_map_coverage as pcm
start_time = time.time()


def print_out_map(current_map):

    os.system('cls')
    for row in range(len(current_map[0])):
        for col in range(len(current_map[1])):
            print(current_map[col][-row-1], end=" ")
            pass
        print()


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

    # basically the cutting width
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


def get_cordinate(cordinate, lst):
    status = lst[int(cordinate[0])][int(cordinate[1])]
    return status


def change_cordinate(cordinates, lst):
    for cordinate in cordinates:
        if not lst[int(cordinate[0])][int(cordinate[1])] == 2:
            lst[int(cordinate[0])][int(cordinate[1])] = 3


def calculate_new_position(new_pos, new_angle, direction):
    new_pos[0] += math.cos(new_angle) * 0.3*direction[0]
    new_pos[1] += math.sin(new_angle) * 0.3*direction[1]
    return new_pos


def hit_wall(cordinate, boundaries, angle, lst, direction):
    distance = None
    times_tried = 0
    pos_list = []
    found_direction = False
    for lists in range(len(lst)):
        for elements in range(len(lst[0])):
            if lst[lists][elements] == 0:

                cordinate2 = [int(cordinate[0]), int(cordinate[1])]
                x_coordinate_squared = (cordinate2[0] - lists)**2
                y_coordinate_squared = (cordinate2[1] - elements)**2
                new_distance = x_coordinate_squared + y_coordinate_squared

                if distance is None:
                    distance = float(new_distance)
                if (new_distance <= distance):
                    distance = float(new_distance)
                    pos_list.insert(0, [lists, elements])
                else:
                    pos_list.append([lists, elements])

    while not found_direction:
        if times_tried == len(pos_list):
            new_angle = random.uniform(0, 2*math.pi)
            return new_angle, direction
        current_list = pos_list[times_tried]
        if int(cordinate[0]) == current_list[0]:
            new_angle = math.pi/2
        else:
            new_angle = math.atan((int(cordinate[1]) - current_list[1]) /
                                  (int(cordinate[0]) - current_list[0]))
        new_pos = list(cordinate)

        if (new_pos[0] < current_list[0]):
            direction[0] = 1
        else:
            direction[0] = -1
        if (new_pos[1] < current_list[1]):
            direction[1] = 1
        else:
            direction[1] = -1

        while not found_direction:
            new_pos = calculate_new_position(new_pos, new_angle, direction)
            if [int(new_pos[0]), int(new_pos[1])] in boundaries:
                times_tried += 1
                break
            if lst[int(new_pos[0])][int(new_pos[1])] == 0:
                return new_angle, direction
    return angle, direction


def find_start(data) -> list[int]:
    for col in range(len(data)):
        for row in range(len(data[0])):
            if (data[col][row] == 1):
                start_cordinate = [col, row]
                return start_cordinate
    return [0, 0]


def change_position(speed, current_pos, angle, direction, boundaries, lst):
    length = 0
    line = [current_pos[0] + math.cos(angle)*direction[0]*length, current_pos[1] + math.sin(angle)*direction[1] * length]
    movement_history = []
    pos_list = []
    boundary = 0
    boundary = False
    time = 0
    while not boundary:
        length += speed
        line = [current_pos[0] + math.cos(angle)*direction[0]*length, current_pos[1] + math.sin(angle)*direction[1] * length]
        movement_history.append(line)
        pos_list.append([math.floor(line[0]), math.floor(line[1])])
        if ([math.floor(line[0]), math.floor(line[1])] in boundaries):
            boundary = True
        time += 1
    pos_list.pop(-1)
    line[0] -= math.cos(angle)*direction[0]*speed
    line[1] -= math.sin(angle)*direction[1]*speed
    new_pos = line
    # new_set = set(pos_list)
    change_cordinate(pos_list, lst)
    return new_pos, time, pos_list


path = 'ground_maps/amazinglawn.csv'
multiplier = 5
lst = read_data(path, multiplier)
start_cordinate = find_start(lst)
# print(start_cordinate)
boundaries = get_boundaries(lst)

const_map = [list(row) for row in lst]
current_pos = list(start_cordinate)
speed = 0.3

direction = [1, 1]
angle = math.pi/2
actual_time = 0
is_back, all_cut = False, False
last_pos = list(start_cordinate)
movement_history = [[start_cordinate[0], start_cordinate[1]]]
max_time = 120 * 60
start_un_cut = 0

for row in range(len(lst)):
    for col in range(len(lst[row])):
        if lst[row][col] == 1:
            lst[row][col] = 0

        if lst[row][col] == 0:
            start_un_cut += 1

un_cut = start_un_cut

while (not all_cut) and actual_time < max_time:
    un_cut = 0
    cut = 0
    current_pos, time_gone, pos_lst = change_position(speed, current_pos,
                                                      angle, direction,
                                                      boundaries, lst,
                                                      multiplier)
    actual_time += time_gone/multiplier
    angle, direction = hit_wall(current_pos, boundaries, angle, lst, direction)
    movement_history += pos_lst

    for lists in range(len(lst)):
        if 0 in lst[lists]:
            un_cut += lst[lists].count(0)

    if (current_pos == start_cordinate):
        is_back = True
    else:
        is_back = False

    if (un_cut == 0):
        all_cut = True

# print(movement_history)
print("Real world time:", time.time()-start_time)
print("Time:", actual_time)
print("Cut, uncut:", start_un_cut - un_cut, un_cut)
print("Percentage cut:", round((1-(un_cut/start_un_cut))*100, 1))
precentage = round((100-(un_cut/start_un_cut)*100), 2)
# print_out_map(lst)
vimp(movement_history, multiplier)
pixel_map(const_map, multiplier)
pcm(lst, actual_time, precentage, start_un_cut - un_cut, start_un_cut)
