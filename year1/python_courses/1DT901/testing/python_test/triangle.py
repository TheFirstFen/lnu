# triangle.py
#
# Author: Samuel Berg
# 06-Oct-2022

N = int(input('Provide a positive integer: '))
if N < 0:
    print('N should have been positive')
else:
    for i in range(N + 1):
        print(' ' * (N - i) + '*' * i)


# Completed
