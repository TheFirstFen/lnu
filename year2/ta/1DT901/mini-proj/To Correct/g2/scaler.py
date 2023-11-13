import csv


# reads file in maps folder based on input
def reader(name, scaler):
    # name = "small"
    # name = input("Name of .csv file: ")
    repo = f"maps/{name}.csv"
    # scaler = 4
    # scaler = int(input("How much should map be scaled by? "))

    with open(repo, "r") as read:
        row_list = []
        for row in csv.reader(read):
            col_list = []
            for i in row:
                count = 0
                while count < scaler:
                    if i == "L":
                        col_list.append(0)
                    elif i == "S":
                        col_list.append(1)
                    elif i == "O":
                        col_list.append(2)
                    count += 1
            count = 0
            while count < scaler:
                row_list.append(col_list.copy())
                count += 1
    # writer(row_list)
    return row_list, repo, scaler


# saves scaled list to file current.csv
def writer(gen_map):
    path = "maps/current.csv"

    with open(path, "w") as write:
        len(gen_map)
        for row in gen_map:
            csv_line = ",".join(map(str, row)) + "\n"
            write.write(csv_line)
