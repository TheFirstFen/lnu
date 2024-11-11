from random import randint


count = 0
num = 10
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

while num <= 2621440:
    rand_num = randint(1, 6)
    if count == num:
        ma = max(one, two, three, four, five, six)
        mi = min(one, two, three, four, five, six)
        dif = ma - mi
        div = dif / ma
        perc = div * 100
        r_perc = round(perc, 2)
        print(f"For {num} rolls, the difference is {r_perc}%")
        num *= 2
    elif rand_num == 1:
        one += 1
        count += 1
    elif rand_num == 2:
        two += 1
        count += 1
    elif rand_num == 3:
        three += 1
        count += 1
    elif rand_num == 4:
        four += 1
        count += 1
    elif rand_num == 5:
        five += 1
        count += 1
    else:
        six += 1
        count += 1
