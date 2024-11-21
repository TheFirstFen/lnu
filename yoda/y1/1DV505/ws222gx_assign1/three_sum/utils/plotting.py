import matplotlib.pyplot as plt


def make_plot(x_label: str, y_label: str, size: list, time_result: list,
              labels: list, title: str, regression=False, fluc=False):

    color_config = ["r", "b", "g"]
    symbol_config = ["o", "x", "+"]

    for i in range(len(time_result)):
        color = "-" + symbol_config[i] + color_config[i] 
        if fluc or (regression and i == 0):     # if i is 0 than logx vs logy
            color = color[1:]

        plt.plot(size, time_result[i], color, label=labels[i])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()
