# read input
i = int(input('Enter a large positive integer: '))


# decides wether its even, odd, zero and compute result
def d(n):
    e = 0
    z = 0
    o = 0
    n1 = str(n)

    for digits in n1:
        if digits == '0':
            z += 1
        elif int(digits) % 2 == 0:
            e += 1
        else:
            o += 1

    print('\nZeros: ', z)
    print('Odd: ', o)
    print('Even: ', e)


d(i)
