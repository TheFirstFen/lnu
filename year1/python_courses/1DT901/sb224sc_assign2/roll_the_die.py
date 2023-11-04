# roll_the_die.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022
from random import randint


def roll_the_die(N):
    stored_rolls = [0, 0, 0, 0, 0, 0]
    for i in range(N):
        die = randint(0, 5)
        stored_rolls[die] += 1

    most = max(stored_rolls)

    least = min(stored_rolls)

    difference = round(((most - least) / most) * 100, 2)

    print(f'For {N} rolls, the difference is {difference}%')


for i in [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480,
          40960, 81920, 163840, 327680, 655360, 1310720, 2621440, 5242880]:
    roll_the_die(i)
