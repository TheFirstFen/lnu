import matplotlib.pyplot as plt
import numpy as np
import json


def plotUF():
    with open('./data/uf.json', 'r') as file:
        dataUF = json.load(file)

    with open('./data/quf.json', 'r') as file:
        dataQUF = json.load(file)

    with open('./data/wquf.json', 'r') as file:
        dataWQUF = json.load(file)

    with open('./data/pcwquf.json', 'r') as file:
        dataPCWQUF = json.load(file)

    unionSteps = np.arange(10_000, 100_000, 10_000)

    startSize = 100_000

    for size in range(len(dataUF)):
        plt.plot(unionSteps, convert_to_milliseconds(dataUF[size]), 'ro',
                 label='UF')
        plt.plot(unionSteps, convert_to_milliseconds(dataQUF[size]), 'go',
                 label='QUF')
        plt.plot(unionSteps, convert_to_milliseconds(dataWQUF[size]), 'bo',
                 label='WQUF')
        plt.plot(unionSteps, convert_to_milliseconds(dataPCWQUF[size]), 'yo',
                 label='PCWQUF')

        plt.xlabel('Steps')
        plt.ylabel('Time (ms)')
        plt.title(f"UnionFind data when size={startSize * (size + 1)}")

        plt.legend()

        plt.show()


def plot3Sum():
    with open("./data/Bruteforce.json", 'r') as file:
        dataBF = json.load(file)

    with open("./data/Two-Pointer.json", 'r') as file:
        dataTP = json.load(file)

    steps = np.arange(1_000, 11_000, 1_000)

    plt.plot(steps, convert_to_seconds(dataBF), 'ro', label='Bruteforce')
    plt.plot(steps, convert_to_seconds(dataTP), 'bo', label='Two-Pointer')

    plt.xlabel('Steps')
    plt.ylabel('Time (s)')
    plt.title('3Sum')

    plt.legend()

    plt.show()


def plot8():
    pass


def convert_to_milliseconds(lst: list) -> list:
    return np.array(lst) / 1e6


def convert_to_seconds(lst: list) -> list:
    return np.array(lst) / 1e9


plotUF()
plot3Sum()
# plot8()
