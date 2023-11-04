#read input
d = float(input('Provide a three digit number: '))

#compute the sum of the number
a = d//100
d %= 100
b = d//10
d %= 10
c = d//1
d %= 1

#add everything
r = a + b + c   
s = round(r)    #round off

#present result
print('Sum of digits: ',s)