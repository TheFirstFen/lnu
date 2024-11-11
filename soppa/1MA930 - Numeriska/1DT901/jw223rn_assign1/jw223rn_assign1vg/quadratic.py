import math                             #Imports square root from math library

#asks the user for values to be calculated
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

u_root = (b ** 2) - (4 * a * c)     #calculates whats under the square root

if a == 0 and b!= 0:                                        #checks if the value under the division is equal to zero
    print(f"There is one solution, namely {-(b/c)}")
elif u_root < 0:                                            #checks if the answer is imaginary
    print("There are no solutions")
elif u_root > 0:                                            #checks if there is two possible answers
    s1 = ((-b) + math.sqrt(u_root)) / (2*a)
    s2 = ((-b) - math.sqrt(u_root)) / (2*a)
    print(f"There are two solutions, namely {s1} and {s2}")
elif a == 0 and b == 0:                                     #if a and b equals to zero, the only solution is 0.0
    print("There is one solution, namely 0.0")
else:                                                       #if its not equal to one of the cases above, the square root equals to zero
    one_s = ((-b) + math.sqrt(u_root)) / (2*a)
    print(f"There is one solution, namely {one_s}")
    