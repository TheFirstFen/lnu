import os


def read_maps(path):
    ground_map = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line.strip().split(",")
            ground_map.append(line)
    return ground_map


path = os.getcwd() + "\\simple.csv"

lst = read_maps(path)
for x,y in 