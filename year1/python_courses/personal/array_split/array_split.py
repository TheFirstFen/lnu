# array_split.py
#
# Author: Samuel Berg
# Date: 10-Sep-2019

def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = x

arr = [12, 10, 5, 6, 52 ,36]
n = len(arr)
splitPos = int(n / 2)

print(arr)

splitArr(arr, n, splitPos)

print(arr)
