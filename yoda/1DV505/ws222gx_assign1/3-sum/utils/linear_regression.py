import math

def Sx_y(x, y):
    return sum(x), sum(y)


def Sxx(x):
    summa = 0
    for i in x:
        summa += i**2
    return summa


def Sxy(x, y):
    summa = 0
    for i, j in zip(x, y):
        summa += (i*j)
    return summa


def log_values(x, y):
    log_y = [math.log(i) for i in y]
    log_x = [math.log(i) for i in x]
    return log_x, log_y

def line_reg(log_x, log_y):
    
   
    xx = Sxx(log_x)
    xy = Sxy(log_x, log_y)
    s_x, s_y = Sx_y(log_x, log_y)
    n = len(log_x)

    numerator = (n * xx) - (s_x ** 2)
    k = ((n * xy) - (s_x * s_y)) / numerator
    m = ((s_y * xx) - (s_x * xy)) / numerator
    line_y = [k*x+m for x in log_x]
    return k, m, line_y
