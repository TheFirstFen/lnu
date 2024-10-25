import random
import math
import os
import time
# from jakob_visuals import visualize_movement_map as vimp
# from jakob_visuals import pixel_map
# from jakob_visuals import pixel_map_coverage as pcm

start_time = time.time()


def print_out_map(current_map):
    # Clears terminal and prints out groundmap
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
    # Adding every "boundary" to a list, which includes the edges of the lawn
    # plus every obstacle in the groundmap
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
    # returns the value of a given coordinate
    status = lst[int(cordinate[0])][int(cordinate[1])]
    return status


def change_cordinate(cordinates, lst):
    # Switches the value of a coordinate to cut, unless it is an obstacle
    for cordinate in cordinates:
        if not lst[int(cordinate[0])][int(cordinate[1])] == 2:
            lst[int(cordinate[0])][int(cordinate[1])] = 3


def hit_wall(cordinate, boundaries, angle, lst, direction):
    # Randomizes an angle an sends it back
    direction = [1, 1]
    angle = random.uniform(0, 2*math.pi)
    return cordinate, angle, direction


def find_start(data) -> list[int]:
    # Searches the list for a start value
    # When found, it returns the value's cordinate
    # If not found, it returns coordinate [0, 0]
    for col in range(len(data)):
        for row in range(len(data[0])):
            if (data[col][row] == 1):
                start_cordinate = [col, row]
                return start_cordinate
    return [0, 0]


def change_position(speed, current_pos, angle, direction, boundaries, lst, multiplier):
    # Computes a line from the current position to one step before a wall 
    # using the angle provided to the function.
    # Also computes the time needed for the mower to drive the distance.
    # Returns time and new position
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
    # Base cases since python's math is inconsistent
    if line[0] < 0:
        line[0] = 0
    if line[1] < 0:
        line[1] = 0
    if line[0] > (len(lst) - 1):
        line[0] = (len(lst) - 1)
    if line[1] > (len(lst[0]) - 1):
        line[1] = (len(lst[0]) - 1)
    new_pos = line
    change_cordinate(pos_list, lst)
    return new_pos, time, pos_list


# Here starts the main program

# Start values
path = 'ground_maps/small.csv'
multiplier = 4
lst = read_data(path, multiplier)
start_cordinate = find_start(lst)
boundaries = get_boundaries(lst)

const_map = [list(row) for row in lst]
current_pos = list(start_cordinate)
speed = 0.3

direction = [1, 1]
angle = math.pi/2
actual_time = 0
all_cut = False
last_pos = list(start_cordinate)
movement_history = [[start_cordinate[0], start_cordinate[1]]]
max_time = 120 * 60
start_un_cut = 0

# Calculates the amount of grass squares not cut in the beginning
for lists in range(len(lst)):
    for elements in range(len(lst[lists])):
        if (lst[lists][elements] == 0 or lst[lists][elements] == 1):
            start_un_cut += 1
un_cut = start_un_cut

# While loop running until either the max time has gone or every square has
# been cut
while (not all_cut) and actual_time < max_time:
    un_cut = 0
    cut = 0
    # Computes the new position
    current_pos, time_gone, pos_lst = change_position(speed, current_pos, angle, direction, boundaries, lst, multiplier)
    # Adds the time needed to go to the new position
    actual_time += time_gone/multiplier
    # Turns.
    current_pos, angle, direction = hit_wall(current_pos, boundaries,
                                             angle, lst, direction)
    # Adds the position to a list, containing every turning point
    last_pos = list(current_pos)
    movement_history += pos_lst
    # Calculates the grass squares not cut
    for lists in range(len(lst)):
        for elements in range(len(lst[lists])):
            if lst[lists][elements] == 0 or lst[lists][elements] == 1:
                un_cut += 1
    # Ends loop if all the grass squares is cut
    if (un_cut == 0):
        all_cut = True

print("Real world time:", time.time()-start_time)
print("Time:", actual_time)
print("Cut, uncut:", start_un_cut - un_cut, un_cut)
print("Percentage cut:", round((1-(un_cut/start_un_cut))*100, 1))
# print_out_map(lst)
# vimp(movement_history)
# pixel_map(const_map)
# pcm(const_map, lst, actual_time)
