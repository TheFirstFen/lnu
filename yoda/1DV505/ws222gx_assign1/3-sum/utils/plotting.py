import matplotlib.pyplot as plt


def make_plot(x_label: str, y_label: str, size: list, time_result: list,
              labels: list, title: str, regression=False):

    color_config = ["r", "b", "g", "y", "c", "m"]

    # plot each run for each algorithm
    for i in range(len(time_result)):
        color = "-+" + color_config[i]
        if regression and i == 0:
            color = color[1:]

        plt.plot(size, time_result[i], color, label=labels[i])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(loc="best")
    plt.show()
