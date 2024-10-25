# instructions:  Each square on a chess board in identified by a letter (a-h) and an integer (1-8). 
#They are typically refered to as c3 or f5. Write a program squarecolor.py that reads a square identifier (e.g. e5) 
#from the keyboard and prints the color (Black or White). Example execution:

a1 = input('Column (a-h): ')
a2 = int(input('Row (1-8): '))

if a1 == 'a':
    a1 = 1
    if (a1 + a2) % 2 == 0:
        print('a',  a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print('a', a2, 'is white')
elif a1 == 'b':
    a1 = 2
    if (a1 + a2) % 2 == 0:
        print('b', a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print('b', a2, 'is white')
elif a1 == 'c':
    a1 = 3
    if (a1 + a2) % 2 == 0:
        print('c' , a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print('c', a2, 'is white')
elif a1 == 'd':
    a1 = 4
    if (a1 + a2) % 2 == 0:
        print('d', a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print('d', a2, 'is white')
elif a1 == 'e':
    a1 = 5
    if (a1 + a2) % 2 == 0:
        print('e', a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print('e', a2, 'is white')
elif a1 == 'f':
    a1 = 6
    if (a1 + a2) % 2 == 0:
        print('f', a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print('f', a2, 'is white')
elif a1 == 'g':
    a1 = 7
    if (a1 + a2) % 2 == 0:
        print('g', a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print ('g', a2, 'is white')
elif a1 == 'h':
    a1 = 8
    if (a1 + a2) % 2 == 0:
        print('h', a2, 'is black')
    elif (a1 + a2) % 2 == 1:
        print ('h', a2, 'is white')
else:
    print('You need ')



#print(plats)
#if a < 3:
 #   print('Bra storlek pa ord:', plats)
#else:
 #   print('dålig storlek på ord')