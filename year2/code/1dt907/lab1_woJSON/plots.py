import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from math import log2
import json

# * Plotting of results


def plotUF():
    with open('./data/uf.json', 'r') as file:
        dataUF = json.load(file)

    # with open('./data/quf.json', 'r') as file:
    #    dataQUF = json.load(file)

    # with open('./data/wquf.json', 'r') as file:
    #    dataWQUF = json.load(file)

    with open('./data/pcwquf.json', 'r') as file:
        dataPCWQUF = json.load(file)

    steps = np.arange(10_000, 100_000, 10_000)

    startSize = 100_000

    for size in range(len(dataUF)):
        plt.plot(steps, convert_to_milliseconds(dataUF[size]), 'ro',
                 label='UF')
        # plt.plot(steps, convert_to_milliseconds(dataQUF[size]), 'go',
        #         label='QUF')
        # plt.plot(steps, convert_to_milliseconds(dataWQUF[size]), 'bo',
        #         label='WQUF')
        plt.plot(steps, convert_to_milliseconds(dataPCWQUF[size]), 'yo',
                 label='PCWQUF')

        plt.xlabel('# Unions')
        plt.ylabel('Time (ms)')
        plt.title(f"UnionFind: {startSize * (size + 1)} objects")

        plt.legend()

        plt.show()


def plot3Sum():
    with open('./data/Bruteforce.json', 'r') as file:
        dataBf = json.load(file)

    with open('./data/Two-Pointer.json', 'r') as file:
        dataTP = json.load(file)

    # with open('./data/Caching.json', 'r') as file:
    #    dataCa = json.load(file)

    steps = np.arange(1_000, 11_000, 1_000)

    (aBf, bBf), _ = curve_fit(powmod, steps, np.array(dataBf)/1e9)
    (aTP, bTP), _ = curve_fit(powmod, steps, np.array(dataTP)/1e9)
    # (aCa, bCa), _ = curve_fit(powmod, steps, np.array(dataCa)/1e9)

    BfSec = convert_to_seconds(dataBf)
    TPSec = convert_to_seconds(dataTP)
    # CaSec = convert_to_seconds(dataCa)

    bCBf = (log2(BfSec[8]) - log2(BfSec[0])) / \
        (log2(steps[8]) - log2(steps[0]))
    bCTP = (log2(TPSec[9]) - log2(TPSec[0])) / \
        (log2(steps[9]) - log2(steps[0]))
    # bCCa = (log2(CaSec[9]) - log2(CaSec[0])) / \
    #    (log2(steps[9]) - log2(steps[0]))

    cCBf = log2(BfSec[8]) - bCBf * log2(steps[8])
    cCTP = log2(TPSec[9]) - bCTP * log2(steps[9])
    # cCCa = log2(CaSec[9]) - bCCa * log2(steps[9])

    print("B values:")
    print("fitted", bBf, bTP)
    print("computed", bCBf, bCTP)

    print("\nC values:")
    print("fitted", aBf, aTP)
    print("computed", cCBf, cCTP)

    # Data points
    plt.plot(steps, BfSec, 'ro', label='Bruteforce')
    plt.plot(steps, TPSec, 'bo', label='Two-Pointer')
    # plt.plot(steps, CaSec, 'go', label='Caching')

    # Fitted curves
    plt.plot(steps, aBf * steps ** bBf, 'r-', label='Bruteforce-fitted')
    plt.plot(steps, aTP * steps ** bTP, 'b-', label='Two-Pointer-fitted')
    # plt.plot(steps, aCa * steps ** bCa, 'g-', label='Cached-fitted')

    # Computed
    plt.plot(steps, (steps * 2 ** (cCBf/bCBf)) **
             bCBf, 'b-', label='Bruteforce-computed')
    plt.plot(steps, (steps * 2 ** (cCTP/bCTP))**bCTP,
             'r-', label='Two-Pointer-computed')
    # plt.plot(steps, (steps * 2 ** (cCCa/bCCa)) **
    #         bCCa, 'g-', label='Caching-computed')

    plt.xlabel('# Objects')
    plt.ylabel('Time (s)')
    plt.title('3Sum')

    plt.legend()

    plt.show()


def convert_to_milliseconds(lst: list) -> list:
    return np.array(lst) / 1e6


def convert_to_seconds(lst: list) -> list:
    return np.array(lst) / 1e9


def powmod(x, a, b):
    return a * x ** b


# plotUF()
plot3Sum()
