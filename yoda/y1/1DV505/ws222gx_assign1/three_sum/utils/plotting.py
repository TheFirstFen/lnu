import matplotlib.pyplot as plt


def make_plot(x_label: str, y_label: str, size: list, time_result: list,
              labels: list, title: str, regression=False):

    color_config = ["r", "b", "g"]
    symbol_config = ["o", "x", "+"]

    for i in range(len(time_result)):
        color = symbol_config[i] + color_config[i] 
        if regression and i > 0:
            color = "-" + color

        plt.plot(size, time_result[i], color, label=labels[i])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()
