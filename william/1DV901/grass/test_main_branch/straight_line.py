import math


def straightline(current_pos, angle, direction, boundaries):
    length = 0
    line = [current_pos[0] + math.cos(angle)*direction[0]*length, current_pos[1] + math.sin(angle)*direction[1] * length]
    pos_list = []
    boundary = 0
    time = 0
    while boundary == 0:
        length += 0.3
        pos_list.append(int(line[0]), int(line[1]))
        if ([int(line[0]), int(line[1])] in boundaries):
            boundary = 1
        time += 1
    line[0] -= math.cos(angle)*direction[0]*0.3
    line[1] -= math.sin(angle)*direction[1]*0.3
    new_pos = line
    
    
