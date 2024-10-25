import math  #importing math to be able to use sqrt 
a = float(input("Enter a number: ")) # input from user 
b = float(input("Enter a number: ")) # input from user
c = float(input("Enter a number: ")) #input from user

if (b**2) > (4*a*c) and a != 0: #create a positive number under the sqrt
    x = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    y = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    print("There are two solution, namely {} and {}".format(x,y))
elif (b**2) < (4*a*c) and a != 0: # Negative number under sqrt
    print("There is no solution")
else:
    a == 0     #if a equals 0. only one solution can be made
    z = (-c/b) 
    print("There is one solution, namely {}".format(z))