# read input
inc = int(input("Please provide monthly income: "))

rest1 = inc % 38000
rest2 = inc % 50000

# check amount of tax, present result
if inc < 38000:
    print ("Corresponding income tax:", round(inc*0.3))

elif inc > 38000 and inc <= 50000:
    print ("Corresponding income tax:", round(inc*0.3 + rest1*0.05))

else:
    print ("Corresponding income tax:", round(inc*0.3 + 12000*0.05 + rest2*0.1))