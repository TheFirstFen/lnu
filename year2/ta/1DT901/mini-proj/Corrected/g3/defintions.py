
path = 'simple.csv'


def read_file(path):  # Fungerar
    plot_map = []

    with open(path, "r") as file:
        lst = file.readlines()
        for symbol in lst:
            temp_list = []
            for char in symbol:
                if (char == "O"):
                    temp_list.append(0)
                elif (char == "L"):
                    temp_list.append(1)
                elif (char == "S"):
                    temp_list.append(2)
            plot_map.append(temp_list)

    new_lst = []

    for i in range(len(plot_map)):
        new_lst.append(list())

    for col in range(len(plot_map[0])):
        for row in range(len(plot_map)):
            new_lst[row].append(plot_map[row][col])

    return new_lst[::-1]


def start_point(plot_map):  # Fungerar
    for lists in range(len(plot_map)):
        for i in range(len(plot_map[0])):
            if plot_map[lists][i] == 2:
                y = lists
                x = i
                return x, y


def is_outside(x, y):  # Fungerar
    if x < 0 or x > cols:
        return True
    if y < 0 or y > rows:
        return True
    else:
        symbol = plot_map[x][y]
        if symbol == 0:
            return True
        else:
            return False


def positions(x, y):
    pass


# Main
path = "simple.csv"
plot_map = read_file(path)
plot_map.reverse()
rows = len(plot_map)
cols = len(plot_map[0])
