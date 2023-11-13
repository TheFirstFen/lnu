import matplotlib.pyplot as plt
import matplotlib.colors as col
import random
import math
import csv


class Robot:
    v = 0.3
    delta_t = 0.1

    def __init__(self, csv_file_path, total_time_in_seconds) -> None:
        self.ground_map = self.read_csv_file_content_to_lst(csv_file_path)
        self.number_array = self.ground_map_to_num_array(self.ground_map)
        self.adjusted_number_array = self.reversed_list(self.number_array)
        self.x_0, self.y_0 = self.start_coordinates(self.adjusted_number_array)
        # adjusts the starting positions to appear in the middle of
        # the starting square
        self.x_0 += 1/2
        self.y_0 += 1/2
        self.y_len, self.x_len = self.shape_of_2d_list(self.ground_map)
        self.steps_to_take = int(total_time_in_seconds / self.delta_t)
        self.x_lst = [self.x_0]
        self.y_lst = [self.y_0]
        self.map_area = self.x_len * self.y_len
        self.area_to_mowe = self.map_area - self.obstacle_area(
            self.ground_map)

    def obstacle_area(self, lst):
        """
        Calculates and returns the total area of obstacles in the map
        """
        area = 0
        for i in lst:
            for j in i:
                if j == "O":
                    area += 1
        return area

    def ground_map_to_num_array(self, ground_map):
        """
        Reads a ground map consisting of letters such that
        S is the starting point,
        O is an obstacle,
        L is an area of lawn to be mowed.

        Then converts it to a two-dimensional array/list (or matrix).
        """
        number_array = []
        for i in ground_map:
            ii = []
            for j in i:
                num = 0
                if j == "O":
                    num = 2
                if j == "S":
                    num = 1
                ii.append(num)
            number_array.append(ii)
        return number_array

    def read_csv_file_content_to_lst(self, csv_file_path):
        """
        """
        with open(csv_file_path, "r") as file:
            content = csv.reader(file)
            ground_map = list(content)
        return ground_map

    def ground_map_visualization(self, map_colors):
        cmap = col.ListedColormap(colors=map_colors)
        fig1, ax1 = plt.subplots()
        ax1.imshow(self.number_array, cmap=cmap, aspect=1,
                   vmin=0, vmax=2, extent=[0, self.x_len, 0, self.y_len])
        plt.grid(True, which="both", color="k", linewidth=1.5)
        ax1.set_xticks([i for i in range(self.x_len + 1)],
                       labels=[i for i in range(self.x_len + 1)])
        ax1.set_yticks([i for i in range(self.y_len + 1)],
                       labels=[i for i in range(self.y_len + 1)])
        ax1.set_title("Map area: {} m^2, Lawn area: {} m^2".format(
            self.map_area, self.area_to_mowe))
        # plt.colorbar(ticks=[0, 1, 2])

    def reversed_list(self, lst):
        rev_lst = []
        for i in range(len(lst) - 1, -1, -1):
            rev_lst.append(lst[i])
        return rev_lst

    def start_coordinates(self, ground_map):
        for i in range(len(ground_map)):
            for j in range(len(ground_map[i])):
                if (ground_map[i][j] == 1):
                    return j, i

    def shape_of_2d_list(self, arr):
        y_len = len(arr)
        x_len = len(arr[0])
        return y_len, x_len

    def is_outside(self, x, y):
        """
        Checks if the provided coordinates x and y are outside the ground map
        or inside an obstacle and if it is then returns True
        """
        # Checks if the x coordinate is outside the map
        if (x > self.x_len or x < 0):
            return True
        # Checks if the y coordinate is outside the map
        elif (y > self.y_len or y < 0):
            return True
        else:
            # Checks if the mathematical floor of the x and y coordinates are
            # within any obstacles
            if (self.adjusted_number_array[int(y)][int(x)] == 2):
                return True
        return False

    def one_step(self, x, y, vx, vy):
        x_i = x + vx * self.delta_t
        y_i = y + vy * self.delta_t
        if self.is_outside(x_i, y_i):
            angle = 2 * math.pi * random.random()
            vx_i = self.v * math.cos(angle)
            vy_i = self.v * math.sin(angle)
            return self.one_step(x, y, vx_i, vy_i)
        else:
            return x_i, y_i, vx, vy

    def plot_trace(self):
        fig1, ax1 = plt.subplots()
        ax1.plot(self.x_lst, self.y_lst)
        # plt.grid(True, which="both", color="k", linewidth=1.5)
        ax1.set_xticks([i for i in range(self.x_len + 1)],
                       labels=[i for i in range(self.x_len + 1)])
        ax1.set_yticks([i for i in range(self.y_len + 1)],
                       labels=[i for i in range(self.y_len + 1)])
        plt.grid()

    def start_robot(self):
        angle = 2 * math.pi * random.random()
        vx = self.v * math.cos(angle)
        vy = self.v * math.sin(angle)
        x = self.x_0
        y = self.y_0
        for i in range(self.steps_to_take):
            x, y, vx, vy = self.one_step(x, y, vx, vy)
            self.x_lst.append(x)
            self.y_lst.append(y)

        # The colors green, yellow and black
        colors_1 = ["#009900", "#FFFF00", "#000000"]
        self.ground_map_visualization(colors_1)
        self.plot_trace()
        # plt.show()


def start(csv_file_path, time_hours):
    total_time_hour = time_hours
    total_time_seconds = 3600 * total_time_hour
    robot = Robot(csv_file_path, total_time_seconds)
    # print(robot.area_to_mowe)
    robot.start_robot()


def main():
    """
    map_list = ["empty25x25.csv", "simple.csv", "small.csv",
                "tricky25x25.csv", "my_map.csv"]
    times = [2, 2, 2, 2, 2]
    for i in range(len(map_list)):
        start(map_list[i], 4 * times[i])
    """
    # """
    map_list_2 = ["small.csv", "my_map.csv"]
    time_2 = [2, 2]
    for i in range(len(map_list_2)):
        start(map_list_2[i], time_2[i])
    # """
    plt.show()


if __name__ == "__main__":
    main()
