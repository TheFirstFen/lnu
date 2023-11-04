#read input
i = int(input('Please provide monthly income: '))


#computing taxes, rounding it off and presenting the result
if i<38000:
    t1 = i*0.3
    i1 = round(t1)
    print('Corresponding income tax: ',i1) 
elif i>=38000 and i<=50000:
    t2 = i*0.308
    i2 = round(t2, -2)
    print('Corresponding income tax: ', i2)
elif i> 50000:
    t3 = i*0.344
    i3 = round(t3, -2)
    print('Corresponding income tax: ', i3)