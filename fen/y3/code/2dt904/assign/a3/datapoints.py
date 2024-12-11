import numpy as np


def toPoint(x):
    y = x*.6 + 4*np.random.randn()
    weight = 1.01*x + .02*np.random.randn()
    return [x, y, weight]


def createDatapoints():
    x = list(range(1, 50))
    x = list(map(lambda val: val + np.random.randn()*3 - 1.5, x))
    return list(map(toPoint, x))
