import random
import math
from test_main_branch.visuals import visualize_movement_map as vimp
from test_main_branch.visuals import pixel_map
from test_main_branch.visuals import pixel_map_coverage as pcm


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
    # Adding every "boundary" to a list, which includes the edges to the lawn
    # plus every obstacle in the ground_map.
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


def change_cordinate(cordinates, lst):
    # Switches the value of a coordinate to cut, unless it is an obstacle
    for cordinate in cordinates:
        if not lst[int(cordinate[0])][int(cordinate[1])] == 2:
            lst[int(cordinate[0])][int(cordinate[1])] = 3


def calculate_new_position(new_pos, new_angle, direction):
    # Takes one step in the current direction
    new_pos[0] += math.cos(new_angle) * 0.3*direction[0]
    new_pos[1] += math.sin(new_angle) * 0.3*direction[1]
    return new_pos


def hit_wall(cordinate, boundaries, angle, lst, direction):
    distance = None
    times_tried = 0
    pos_list = []
    found_direction = False
    # Creates a list of every square of grass which isn't cut.
    # This list also gets sorted by the distance from the square to the
    # current position.
    for lists in range(len(lst)):
        for elements in range(len(lst[0])):
            if lst[lists][elements] == 0:
                cordinate2 = [int(cordinate[0]), int(cordinate[1])]
                x_squared = (cordinate2[0] - lists) ** 2
                y_squared = (cordinate2[1] - elements) ** 2
                new_distance = x_squared + y_squared
                if distance is None:
                    distance = float(new_distance)
                if (new_distance <= distance):
                    distance = float(new_distance)
                    pos_list.insert(0, [lists, elements])
                else:
                    pos_list.append([lists, elements])
    # Starting with the closest, checks if there is an obstacle
    # between the current position and the wanted grass square.
    while not found_direction:
        if times_tried == len(pos_list):
            new_angle = random.uniform(0, 2*math.pi)
            return new_angle, direction
        current_list = pos_list[times_tried]
        # Computes the angle between the wanted grass square and the current
        # position
        if int(cordinate[0]) == current_list[0]:
            new_angle = math.pi/2
        else:
            new_angle = math.atan((int(cordinate[1]) - current_list[1]) /
                                  (int(cordinate[0]) - current_list[0]))
        new_pos = list(cordinate)
        # Decides wether the x/y value should be positive or negative.
        # This is needed since math.atan only returns values between
        # -pi/2 and pi/2
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


def find_start(data):
    # Searches the list for a start value
    # When found, it returns the value's cordinate
    # If not found, it returns coordinate [0, 0]
    for col in range(len(data)):
        for row in range(len(data[0])):
            if (data[col][row] == 1):
                start_cordinate = [col, row]
                return start_cordinate
    return [0, 0]


def change_position(speed, current_pos, angle, direction, boundaries, lst):
    # Computes a line from the current position to one step before a wall
    # using the angle provided to the function.
    # Also computes the time needed for the mower to drive the distance.
    # Returns time and new position
    length = 0
    line = [current_pos[0] + math.cos(angle)*direction[0] * length,
            current_pos[1] + math.sin(angle)*direction[1] * length]
    pos_list = []
    boundary = 0
    boundary = False
    time = 0
    while not boundary:
        length += speed
        line = [current_pos[0] + math.cos(angle)*direction[0] * length,
                current_pos[1] + math.sin(angle)*direction[1] * length]
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
        line[1] = 1
    if line[0] > (len(lst) - 1):
        line[0] = (len(lst) - 1)
    if line[1] > (len(lst[0]) - 1):
        line[1] = (len(lst[0]) - 1)
    new_pos = line
    movement_history_pos = [int(line[0]), int(line[1])]
    # Every point of the line gets sent to change_coordinate
    # which changes the value to cut.
    change_cordinate(pos_list, lst)
    return new_pos, time, movement_history_pos


def get_back(cordinate, boundaries, time_gone, movement_history, multiplier):
    # Function finding a good way to get back to the start square
    # This is possible by trying to get to the earliest coordinates where the
    # mower turned. It tests whether this is possible without hitting a wall
    # and repeats until it finds the starting cordinate.
    # Also calculates the time needed to drive back.
    global trace_list
    break_other = False
    times_tried = 0
    found_goal = False
    direction = [1, 1]
    while not found_goal:
        # Finds the coordinate the mower is trying to get to, starting with
        # the earliest turn of the mower, going to the last if needed.
        new_pos = list(cordinate)
        start_cordinate = movement_history[times_tried]
        found_direction = False
        if new_pos[0] == start_cordinate[0]:
            new_angle = math.pi/2
        else:
            new_angle = math.atan(((new_pos[1]) - start_cordinate[1]) /
                                  ((new_pos[0]) - start_cordinate[0]))
        if (new_pos[0] < start_cordinate[0]):
            direction[0] = 1
        else:
            direction[0] = -1
        if (new_pos[1] < start_cordinate[1]):
            direction[1] = 1
        else:
            direction[1] = -1

        while not found_direction:
            # Tests whether the position is accesible without running into a
            # wall
            new_pos = calculate_new_position(new_pos, new_angle, direction)
            if [int(new_pos[0]), int(new_pos[1])] in boundaries:
                times_tried += 1
                break
            if [int(new_pos[0]), int(new_pos[1])] == start_cordinate:
                trace_list.append(start_cordinate)
                break_other = True
                distance = (cordinate[0] - start_cordinate[0])**2
                + (cordinate[1] - start_cordinate[1])**2
                time_gone += ((math.sqrt(distance))/multiplier)/0.3
                # Checks whether this is the starting square
                # If so, then it returns the time it took to drive there
                # Aswell as the turning points.
                # If not, it runs the function again with the new position.
                if (times_tried == 0):
                    break
                else:
                    get_back(start_cordinate, boundaries, time_gone,
                             movement_history, multiplier)
                    break
        if break_other:
            break


def main(path, multiplier, minutes, max_percentage, condition, show):
    global trace_list
    # Here starts the main program

    # Start values
    lst = read_data(path, multiplier)
    start_cordinate = find_start(lst)
    boundaries = get_boundaries(lst)

    const_map = [list(row) for row in lst]
    current_pos = list(start_cordinate)
    speed = 0.3

    direction = [1, 1]
    angle = math.pi/2
    actual_time = 0
    movement_history = [[start_cordinate[0], start_cordinate[1]]]
    max_time = minutes * 60
    start_un_cut = 0

    # Calculates the amount of grass squares not cut in the beginning.
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if lst[row][col] == 1:
                lst[row][col] = 0

            if lst[row][col] == 0:
                start_un_cut += 1
    un_cut = start_un_cut
    percentage = 0
    # While loop running until either the max time has gone or every square has
    # been cut.
    available_conditions = {1: actual_time < max_time,
                            0: percentage < max_percentage}
    while available_conditions[condition]:
        un_cut = 0
        # Computes the new position.
        current_pos, time_gone, pos_lst = change_position(speed, current_pos,
                                                          angle, direction,
                                                          boundaries, lst)
        # Adds the time needed to go to the new position.
        actual_time += time_gone/multiplier
        # Turns.
        angle, direction = hit_wall(current_pos, boundaries, angle, lst,
                                    direction)
        # Adds the position to a list, containing every turning point.
        movement_history.append(pos_lst)
        # Calculates the grass squares not cut.
        for lists in range(len(lst)):
            if 0 in lst[lists]:
                un_cut += lst[lists].count(0)
        # Ends the loop if all the grass squares has been cut

        percentage = 100 - ((un_cut/start_un_cut) * 100)

        if condition == 1:
            available_conditions[1] = actual_time < max_time
        else:
            available_conditions[0] = percentage < max_percentage
    if show:
        # Calculates the way back
        trace_pos = [int(current_pos[0]), int(current_pos[1])]
        trace_list = [trace_pos]
        get_back(trace_pos, boundaries, 0, movement_history, multiplier)
        vimp(movement_history, multiplier, True, trace_list)
        pixel_map(const_map, multiplier)
        pcm(lst, actual_time, percentage, (start_un_cut - un_cut),
            start_un_cut)
    return percentage, actual_time
