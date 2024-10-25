import random
import math
import os
import time


def read_data(file) -> list:
    with open(file, "r") as file:
        lines = file.readlines()

    data = []
    for i in range(len(lines[0].strip().split(","))):
        data.append(list())
    for i in range(len(lines)-1, -1, -1):
        row_data = [item.strip() for item in lines[i].strip().split(",")]
        for char in range(len(row_data)):
            data[char].append(row_data[char])
    return data


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
    print(boundaries)
    return boundaries


def get_cordinate(cordinate, lst):
    status = lst[int(cordinate[0])][int(cordinate[1])]
    return status


def change_cordinate(cordinate, lst):
    if not lst[int(cordinate[0])][int(cordinate[1])] == "O":
        lst[int(cordinate[0])][int(cordinate[1])] = "C"


def farthest_way(cordinate, boundaries, lst):
    for i in range(100):
        new_angle = i*math.pi/50
        direction = [1, 1]
        new_pos = list(cordinate)
        while 1 == 1:
            new_pos[0] += math.cos(new_angle)
            new_pos[1] += math.sin(new_angle)
            if [int(new_pos[0]), int(new_pos[1])] in boundaries:
                new_pos[0] -= math.cos(new_angle)
                new_pos[1] -= math.sin(new_angle)
                for i in range(100):
                    new_pos2 = list(new_pos)
                    new_angle2 = i*math.pi/50
                    direction = [1, 1]
                    while 1 == 1:
                        new_pos2[0] += math.cos(new_angle2)
                        new_pos2[1] += math.sin(new_angle2)
                        if [int(new_pos2[0]), int(new_pos2[1])] in boundaries:
                            break
                        elif lst[int(new_pos2[0])][int(new_pos2[1])] == "L":
                            return new_angle, direction
    new_angle = random.uniform(0, 2*math.pi)
    return new_angle, direction


def hit_wall(cordinate, boundaries, angle, last_pos, lst, direction):
    if [int(cordinate[0]), int(cordinate[1])] in boundaries:
        cordinate = last_pos
        distance = None
        times_tried = 0
        pos_list = []
        found_direction = False
        for lists in range(len(lst)):
            for elements in range(len(lst[0])):
                if lst[lists][elements] == "L":
                    new_distance = ((cordinate[0] - lists)**2) + ((cordinate[1] - elements)**2)
                    if distance is None:
                        distance = float(new_distance)
                    if (new_distance <= distance):
                        distance = float(new_distance)
                        pos_list.insert(0, [lists, elements])
                    else:
                        pos_list.append([lists, elements])
        while not found_direction:
            if times_tried == len(pos_list):
                # new_angle = random.uniform(0, 2*math.pi)
                new_angle, direction = farthest_way(cordinate, boundaries, lst)
                return cordinate, new_angle, direction
            current_list = pos_list[times_tried]
            if int(cordinate[0]) == current_list[0]:
                new_angle = math.pi/2
            else:
                new_angle = math.atan((cordinate[1] - current_list[1]) / (cordinate[0] - current_list[0]))
            new_pos = list(cordinate)
            found_direction = False
            if (new_pos[0] < current_list[0]):
                direction[0] = 1
            else:
                direction[0] = -1
            if (new_pos[1] < current_list[1]):
                direction[1] = 1
            else:
                direction[1] = -1
            while not found_direction:
                new_pos[0] += math.cos(new_angle) * 0.3*direction[0]
                new_pos[1] += math.sin(new_angle) * 0.3*direction[1]
                if [int(new_pos[0]), int(new_pos[1])] in boundaries:
                    times_tried += 1
                    break
                if lst[int(new_pos[0])][int(new_pos[1])] == "L":
                    return cordinate, new_angle, direction
    return cordinate, angle, direction


path = 'simple.csv'
lst = read_data(path)
# lst = [["L", "L", "L", "L"], ["L", "L", "L", "L"], ["L", "L", "O", "O"], ["S", "L", "L", "L"], ["L", "L", "L", "L"]]
for lists in range(len(lst)):
    for elements in range(len(lst[0])):
        if (lst[lists][elements] == "S"):
            start_cordinate = [lists, elements]

boundaries = get_boundaries(lst)
current_pos = list(start_cordinate)
speed = 0.3
direction = [1, 1]
angle = math.pi/2
actual_time = 0
all_cut = False
last_pos = list(start_cordinate)

while not all_cut:
    un_cut = 0
    current_pos, angle, direction = hit_wall(current_pos, boundaries, angle, last_pos, lst, direction)
    last_pos = list(current_pos)
    change_cordinate(current_pos, lst)
    current_pos[0] += speed*direction[0]*math.cos(angle)
    current_pos[1] += speed*direction[1]*math.sin(angle)
    actual_time += 1
    for lists in range(len(lst)):
        for elements in range(len(lst[lists])):
            if (lst[lists][elements] == "L"):
                un_cut += 1
                new_list = [lists, elements]
    print(un_cut)
    print(current_pos)
    # os.system('cls')
    for i in range(len(lst[0])):
        for k in range(len(lst)):
            # print(lst[k][-i-1], end=" ")
            pass
        # print()
    if (un_cut == 0):
        break
print(actual_time)
