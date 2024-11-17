import math


def Sx_y(x: list, y: list):
    return sum(x), sum(y)


def Sxx(x: list):
    summa = 0
    for i in x:
        summa += i**2
    return summa


def Sxy(x: list, y: list):
    summa = 0
    for i, j in zip(x, y):
        summa += (i*j)
    return summa


def log_values(x: list, y: list):
    # log(1) = 0 while log(0) = domain error
    log_x = [math.log(i) if i > 0 else math.log(1) for i in x]
    log_y = [math.log(i) for i in y]
    return log_x, log_y


def line_reg(log_x: list, log_y: list):

    xx = Sxx(log_x)
    xy = Sxy(log_x, log_y)
    s_x, s_y = Sx_y(log_x, log_y)
    n = len(log_x)

    numerator = (n * xx) - (s_x ** 2)
    k = ((n * xy) - (s_x * s_y)) / numerator
    m = ((s_y * xx) - (s_x * xy)) / numerator
    line_y = [k*x+m for x in log_x]
    return k, m, line_y


def linear_reg_run(size_lst: list, avg_times: dict, names: list):
    linear_results = {}

    for i in range(len(avg_times)):
        times = list(avg_times[i])
        log_x, log_y = log_values(size_lst, times)
        k, m, line_y = line_reg(log_x, log_y)
        rounded_k = round(k, 3)
        linear_label = f"{names[i]}: kx + m\nk = value {rounded_k}"
        linear_results[i] = [log_x, log_y, linear_label]
    return linear_results
