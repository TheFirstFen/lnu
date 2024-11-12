import matplotlib.pyplot as plt

def make_plot(x_label, y_label, *time_result, labels, size):
    color_config = ["r", "b", "g", "y", "c", "m"]

    # plot each run for each algorithm
    for i in range(len(time_result)):
        color = "+-" + color_config[i]
        plt.plot(size, time_result[i], color, label=labels[i])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc="best")
    plt.show()
