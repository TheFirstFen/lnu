#read input
c = input('Enter a chess square identifier (e.g. e5): ')

#the variables
u = 'a, c, e, g'
d = 'b, d, f, h'
r = '7531'
l = '2468'

#formula for identifying the squares and presenting result
if len(c) == 2:
    if c[0] in u and c[1] in r:
        print(c,'is Black')
    elif c[0] in d and c[1] in l:
        print(c,'is Black')
    elif c[0] in d and c[1] in r:
        print(c,'is White')
    elif c[0] in u and c[1] in l:
        print(c,'is White')