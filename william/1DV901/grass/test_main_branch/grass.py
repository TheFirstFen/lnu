import random
import math
import os
import time
import numpy as np
# from visuals import visualize_movement_map as vimp
# from visuals import pixel_map
# from visuals import pixel_map_coverage as pcm


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

    # kan vara problemet.    
    data = []
    for i in range(len(lines[0].strip().split(","))):
        data.append(list())
    for i in range(len(lines)-1, -1, -1):
        row_data = [item.strip() for item in lines[i].strip().split(",")]
        for char in range(len(row_data)):
            data[char].append(row_data[char])

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
            if (lst[lists][elements] == "O"):
                boundaries.append([lists, elements])
    return boundaries


def get_cordinate(cordinate, lst):
    status = lst[int(cordinate[0])][int(cordinate[1])]
    return status


def change_cordinate(cordinate, lst):
    if not lst[int(cordinate[0])][int(cordinate[1])] == "O":
        lst[int(cordinate[0])][int(cordinate[1])] = "*"
        lst[int(cordinate[0])][int(cordinate[1])] = "C"
    return lst


def calculate_new_position(new_pos, new_angle, direction):
    new_pos[0] += math.cos(new_angle) * 0.3*direction[0]
    new_pos[1] += math.sin(new_angle) * 0.3*direction[1]
    return new_pos


def hit_wall(cordinate, boundaries, angle, last_pos, direction):
    if [int(cordinate[0]), int(cordinate[1])] in boundaries:
        cordinate = last_pos
        direction = [1, 1]
        angle = random.uniform(0, 2*math.pi)
    return cordinate, angle, direction


def find_start(data) -> list[int]:
    for col in range(len(data)):
        for row in range(len(data[0])):
            if (data[col][row] == "S"):
                start_cordinate = [col, row]
                return start_cordinate
    return [0, 0]


def change_position(speed: float, direction: list,
                    angle: float, current_position: list,
                    current_pos) -> list:

    current_pos[0] += speed*direction[0]*math.cos(angle)
    current_pos[1] += speed*direction[1]*math.sin(angle)
    return current_position


def main():
    path = 'simple.csv'
    multiplier = 5
    lst = read_data(path, multiplier)
    start_cordinate = find_start(lst)
    # print(start_cordinate)
    boundaries = get_boundaries(lst)

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
    
    for lists in range(len(lst)):
        for elements in range(len(lst[lists])):
            if (lst[lists][elements] == "L" or lst[lists][elements] == "S"):
                start_un_cut += 1
    
    un_cut = start_un_cut
    precentage = 1
    while (precentage) >= 0.2 and actual_time < max_time:
        # time.sleep(1)
        un_cut = 0

        current_pos, angle, direction = hit_wall(current_pos, boundaries,
                                                 angle, last_pos,
                                                 direction)

        last_pos = list(current_pos)
        movement_history.append([(current_pos[0]), (current_pos[1])])
        change_cordinate(current_pos, lst)

        current_pos = change_position(speed, direction, angle)
        actual_time += 1/multiplier

        for lists in range(len(lst)):
            for elements in range(len(lst[lists])):
                if (lst[lists][elements] == "L"):
                    un_cut += 1
        # print_out_map(lst)
        # os.system("cls")
        # print(un_cut)

        if (current_pos == start_cordinate):
            is_back = True
        else:
            is_back = False

        if (un_cut == 0):
            all_cut = True
    
    precentage = un_cut / start_un_cut
    print(actual_time)
    # print_out_map(lst)
    # vimp(boundaries, start_cordinate, movement_history)
    # pixel_map(const_map)
    # pcm(const_map, lst, actual_time)
    return un_cut, precentage


count = 10
total = 0
lst = []
for i in range(count):
    sim_info = main()
    total += sim_info[1]
    lst.append(sim_info[1])
    
avg = total / count
std = np.std(lst)

print("Average missed grass squares: ", avg)
print("Std: ", std)
