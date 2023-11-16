# random_numbers.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022
from random import randint


def random_numbers(N):
    for_average = 0
    current_value = 0
    minimum = 101
    maximum = 0
    print('Generated values: ', end='')
    for _ in range(N):
        current_value = randint(1, 100)
        for_average += current_value
        print(current_value, end=' ')
        if current_value < minimum:
            minimum = current_value
        elif current_value > maximum:
            maximum = current_value
    avg = round(for_average / N)
    print(
        f'\nAverage, min, and max are {avg}, {minimum}, and {maximum}')


N = -1
while N < 1:
    N = int(input('Enter number of integers to be generated: '))

random_numbers(N)
