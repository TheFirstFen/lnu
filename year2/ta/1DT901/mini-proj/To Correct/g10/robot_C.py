import matplotlib.pyplot as plt
import random
import math
import robot_functions as rf


class Robot:
    v = 0.3
    delta_t = 0.1
    step_counter = 0

    def __init__(self, csv_file_path, pixels_per_sqaure,
                 total_time_in_hours) -> None:
        self.n = pixels_per_sqaure
        self.ground_map = rf.read_csv_file_content_to_lst(csv_file_path)
        self.number_array = rf.ground_map_to_num_array(self.ground_map)
        self.adjusted_number_array = rf.reverse_rows_list(self.number_array)
        self.ext_arr = rf.pixel_grid(self.ground_map)

        self.extended_number_array = rf.extend_array(self.ext_arr, self.n)
        self.y_len, self.x_len = rf.shape_of_2d_list(
            self.number_array)
        self.x_0, self.y_0 = rf.start_coordinates(self.number_array)
        self.x_0 = self.x_0 * self.n + 2
        self.y_0 = self.y_0 * self.n + 2
        self.extended_number_array[self.y_0][self.x_0] = 1
        self.steps_to_take = int(total_time_in_hours / self.delta_t)
        self.x_lst = [self.x_0]
        self.y_lst = [self.y_0]
        self.map_area = self.x_len * self.y_len
        self.area_to_mowe = self.map_area - rf.obstacle_area(
            self.extended_number_array
        )

    def n_sized_partitions(self, ground_map):
        number_array = []
        for i in ground_map:
            ii = []
            for j in i:
                num = 0
                if j == "O":
                    num = 2
                ii.append(num)
            number_array.append(ii)
        return number_array

    def ground_map_visit(self, x, y):
        if (self.extended_number_array[int(y)][int(x)] == 0):
            self.extended_number_array[int(y)][int(x)] = 1

    def is_outside(self, x, y):
        """
        Checks if the provided coordinates x and y are outside the ground map
        or inside an obstacle and if it is then returns True
        """
        # Checks if the x coordinate is outside the map
        if (x > self.n * self.x_len or x < 0):
            return True
        # Checks if the y coordinate is outside the map
        elif (y > self.n * self.y_len or y < 0):
            return True
        else:
            # Checks if the mathematical floor of the x and y coordinates are
            # within any obstacles
            if (self.extended_number_array[int(y)][int(x)] == 2):
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
            self.ground_map_visit(x_i, y_i)
            return x_i, y_i, vx, vy

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
        # colors_1 = ["#009900", "#FFFF00", "#000000"]
        # self.ground_map_visualization(colors_1)
        colors_2 = ["#FFFFFF", "#FF0000", "#000000"]
        visit_count, total_count = rf.compute_coverage(
            self.extended_number_array)
        rf.pixel_visualization(colors_2, self.extended_number_array,
                               visit_count, total_count)
        # plt.show()


def start(csv_file_path, n, time_hours):
    total_time_hour = time_hours
    total_time_seconds = 3600 * total_time_hour
    robot = Robot(csv_file_path, n, total_time_seconds)
    robot.start_robot()


def main():
    n = 5
    # """
    map_list = ["empty25x25.csv", "simple.csv", "small.csv",
                "tricky25x25.csv", "my_map.csv"]
    times = [2, 2, 2, 2, 2]
    for i in range(len(map_list)):
        start(map_list[i], n, 0.5 * times[i])
    # """
    """
    map_list_2 = ["small.csv", "my_map.csv"]
    time_2 = [2, 2]
    for i in range(len(map_list_2)):
        start(map_list_2[i], n, time_2[i])
    """
    plt.show()


if __name__ == "__main__":
    main()
