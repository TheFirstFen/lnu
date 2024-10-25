# Create a randomicer that randomes the numbers from 1-6
import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

rolles = 10

while rolles <= 5242880:
    for i in range(0, rolles + 1):
        ran_num = random.randint(1, 6)
        if ran_num == 1:
            one = one + 1
        elif ran_num == 2:
            two = two + 1
        elif ran_num == 3:
            three = three + 1
        elif ran_num == 4:
            four = four + 1
        elif ran_num == 5:
            five = five + 1
        else:
            six = six + 1
        if i == rolles:
            maximum = max(one, two, three, four, five, six)
            minimum = min(one, two, three, four, five, six)
            difference = ((maximum - minimum)/maximum)*100
            print(f"For {i} rolls, the difference is {difference}%")
            rolles *= 2
