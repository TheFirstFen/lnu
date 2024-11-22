import matplotlib.pyplot as plt


def make_plot(x_label: str, y_label: str, title: str, time_result: dict,
              labels: list, regression=False, size=[]):
    color_config = ["r", "b", "g", "y", "c", "m"]
    symbols = ["x", "o", "s"]

    # plot each run for each algorithm
    for i in range(len(time_result)):

        color = symbols[i] + color_config[i]
        if not regression:
            plt.plot(size, time_result[i], color, label=labels[i])
        else:
            plt.plot(time_result[i][0], time_result[i][0], color,
                     label=time_result[i][2])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()
