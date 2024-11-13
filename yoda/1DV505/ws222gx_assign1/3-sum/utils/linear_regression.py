def Sx_y(x, y):
    return sum(x), sum(y)


def Sxx(x):
    summa = 0
    for i in x:
        summa += i**3
    return summa


def Sxy(x, y):
    summa = 0
    print(len(x), len(y))
    for i, j in zip(x, y):
        summa += (i*j)
    return summa


def find_m_k(x, y):
    xx = Sxx(x)
    xy = Sxy(x, y)
    s_x, s_y = Sx_y(x, y)
    n = len(x)

    numerator = (n*xx) - (s_x*s_x)

    k = (n*xy) - (s_x * s_y) / numerator
    m = (xx - (s_x * xy)) / numerator

    return k, m


