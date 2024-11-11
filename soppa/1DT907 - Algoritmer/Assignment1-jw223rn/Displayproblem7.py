import matplotlib.pyplot as plt


def display_scatter(x_values, y_values_uf, y_values_quf, title="Graph", x_label="X-axis", y_label="Y-axis"):
    plt.scatter(x_values, y_values_uf, label="Brute force")
    plt.scatter(x_values, y_values_quf, label="With cache")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


sizeAmount = [100, 500, 1000, 2500, 5000, 7500, 10000]
time3sum = [0.007715625, 0.108891459, 0.602767166, 9.167325667, 73.820756459, 252.517078708, 583.159775042]
time3sumcache = [0.00195325, 0.017687792, 0.029005958, 0.189759417, 0.783339083, 1.701242208, 3.341058083]


display_scatter(sizeAmount, time3sum, time3sumcache, "3sum", "Length", "Time (Seconds)")

