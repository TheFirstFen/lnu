import random
import math
picount = 0
for u in range(1, 4):
    n = 100**u

    #  places random points and adding if the radius to origo is less than 1
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        radius = math.sqrt(y**2 + x**2)
        if (radius <= 1):
            picount += 1

    #  approximate of pi
    piapprox = 4*picount/n
    error = math.pi-4*picount/n
    absoluteerror = abs(error)
    print("The approximate of pi is: ", piapprox, "when N is: ", n)
    print("The error was: ", absoluteerror)
    print()
