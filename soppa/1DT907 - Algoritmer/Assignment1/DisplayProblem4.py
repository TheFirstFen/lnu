import matplotlib.pyplot as plt


def display_scatter(x_values, y_values_uf, y_values_quf, title="Graph", x_label="X-axis", y_label="Y-axis"):
    plt.scatter(x_values, y_values_uf, label="UF")
    plt.scatter(x_values, y_values_quf, label="QUF")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


unionAmount = [10000, 30000, 50000, 70000, 90000]
time10000uf = [0.443393792, 1.587515292, 2.795350875, 3.978732042, 5.271170125]
time10000quf = [0.011827, 0.240103125, 0.623315125, 0.948160917, 1.280912584]
time50000uf = [1.211975792, 3.719073125, 9.007373, 13.067200833, 23.524010125]
time50000quf = [3.10625E-4, 0.003783167, 0.65540725, 2.592249041, 5.064398084]
time100000uf = [2.326283417, 7.067276292, 11.811465875, 18.920086416, 29.57019025]
time100000quf = [3.52916E-4, 0.001128666, 0.001998958, 0.213242875, 1.576029541]

display_scatter(unionAmount, time10000uf, time10000quf, "10.000 elements", "Amount of unions", "Time (Seconds)")
display_scatter(unionAmount, time50000uf, time50000quf, "50.000 elements", "Amount of unions", "Time (Seconds)")
display_scatter(unionAmount, time100000uf, time100000quf, "100.000 elements", "Amount of unions", "Time (Seconds)")
