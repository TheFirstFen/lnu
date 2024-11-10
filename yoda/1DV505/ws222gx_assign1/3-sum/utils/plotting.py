import matplotlib.pyplot as plt


def make_plot(x_label, y_label, time_result, size):
    color_config = ["r", "b", "g", "y", "b"]

    for i in range(len(time_result)):
        color = f"-+{color_config[i]}"
        plt.plot(time_result[i], size, color)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

