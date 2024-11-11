import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

sizeAmount = np.array([100, 500, 1000, 2500, 5000, 7500, 10000])
time3sum = np.array([0.007715625, 0.108891459, 0.602767166, 9.167325667, 73.820756459, 252.517078708, 583.159775042])
time3sumcache = np.array([0.00195325, 0.017687792, 0.029005958, 0.189759417, 0.783339083, 1.701242208, 3.341058083])

def power_law(x, a, b):
    return a * x ** b

def computedBValue(time, size):
    logTime = np.log2(time)
    logSize = np.log2(size)

    b_val = ((logTime[6] - logTime[0]) / (logSize[6] - logSize[0]))
    return b_val

(aBrute, bBrute), _ = curve_fit(power_law, sizeAmount, time3sum)
(aCache, bCache), _ = curve_fit(power_law, sizeAmount, time3sumcache)


bCompBrute = computedBValue(time3sum, sizeAmount)
bCompCache = computedBValue(time3sumcache, sizeAmount)

aCompBrute = np.log2(time3sum[6]) - bCompBrute * np.log2(sizeAmount[6])
aCompCache = np.log2(time3sumcache[6]) - bCompCache * np.log2(sizeAmount[6])

print(f"A values:\nFitted: Brute; {aBrute} | Cache; {aCache}")
print(f"Computed: Brute; {aCompBrute} | Cache; {aCompCache}")

print(f"B values:\nFitted: Brute; {bBrute} | Cache; {bCache}")
print(f"Computed: Brute; {bCompBrute} | Cache; {bCompCache}")

plt.plot(sizeAmount, time3sum, 'bo', label='Bruteforce values')
plt.plot(sizeAmount, time3sumcache, 'yo', label='Cache values')

plt.plot(sizeAmount, power_law(sizeAmount, aBrute, bBrute), 'b-', label='Fitted-Bruteforce')
plt.plot(sizeAmount, power_law(sizeAmount, aCache, bCache), 'y-', label='Fitted-Cache')

plt.plot(sizeAmount, (sizeAmount * 2 ** (aCompBrute/bCompBrute)) ** bCompBrute, 'b-.', label='Computed-Bruteforce')
plt.plot(sizeAmount, (sizeAmount * 2 ** (aCompCache/bCompCache)) ** bCompCache, 'y-.', label='Computed-Cache')

plt.xlabel("Amount")
plt.ylabel("Time (s)")
plt.title("3Sum")
plt.legend()
plt.show()