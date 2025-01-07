import matplotlib.pyplot as plt


def make_plot(results: dict, sizes: list, labels: list):

    color_config = ["-+", "-x", "-o"]
    for i in range(len(results)):
        plt.plot(sizes, results[i], color_config[i], label=labels[i])

    plt.xlabel("List sizes")
    plt.ylabel("Time in seconds")
    plt.title("Average time for 5 runs")
    plt.legend()
    plt.show()
