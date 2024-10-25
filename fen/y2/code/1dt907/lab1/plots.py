import matplotlib.pyplot as plt
import numpy as np
import json

# * Plotting of results


def plotUF():
    with open('./data/uf.json', 'r') as file:
        dataUF = json.load(file)

    with open('./data/quf.json', 'r') as file:
        dataQUF = json.load(file)

    with open('./data/wquf.json', 'r') as file:
        dataWQUF = json.load(file)

    with open('./data/pcwquf.json', 'r') as file:
        dataPCWQUF = json.load(file)

    steps = np.arange(10_000, 100_000, 10_000)

    startSize = 100_000

    for size in range(len(dataUF)):
        plt.plot(steps, convert_to_milliseconds(dataUF[size]), 'ro',
                 label='UF')
        plt.plot(steps, convert_to_milliseconds(dataQUF[size]), 'go',
                 label='QUF')
        plt.plot(steps, convert_to_milliseconds(dataWQUF[size]), 'bo',
                 label='WQUF')
        plt.plot(steps, convert_to_milliseconds(dataPCWQUF[size]), 'yo',
                 label='PCWQUF')

        plt.xlabel('# Unions')
        plt.ylabel('Time (ms)')
        plt.title(f"UnionFind: {startSize * (size + 1)} objects")

        plt.legend()

        plt.show()


def plot3Sum():
    with open('./data/Bruteforce.json', 'r') as file:
        dataBF = json.load(file)

    with open('./data/Two-Pointer.json', 'r') as file:
        dataTP = json.load(file)

    with open('./data/Caching.json', 'r') as file:
        dataCa = json.load(file)

    steps = np.arange(1_000, 11_000, 1_000)

    plt.plot(steps, convert_to_seconds(dataBF), 'ro', label='Bruteforce')
    plt.plot(steps, convert_to_seconds(dataTP), 'bo', label='Two-Pointer')
    plt.plot(steps, convert_to_seconds(dataCa), 'go', label='Caching')

    plt.xlabel('# Objects')
    plt.ylabel('Time (s)')
    plt.title('3Sum')

    plt.legend()

    plt.show()


def plot8():
    with open('./data/Percolation.json', 'r') as file:
        data = json.load(file)

    print("Mean time taken: {:.4f}".format(np.mean(data) / 1e6))


def convert_to_milliseconds(lst: list) -> list:
    return np.array(lst) / 1e6


def convert_to_seconds(lst: list) -> list:
    return np.array(lst) / 1e9


plotUF()
plot3Sum()
# plot8()
