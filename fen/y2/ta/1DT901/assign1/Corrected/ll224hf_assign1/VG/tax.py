#Please provide monthly income: 32000           30% of all bellow 38000             30% = 0.3   30% at this
#Corresponding income tax:  9600                5% on all between 38000 and 50000   5% = 0.05   35% at this
#                                               5% on all above 50000                           40% at this
#Please provide monthly income: 46000
#Corresponding income tax:  14200
#
#Please provide monthly income: 79000
#Corresponding income tax:  27200

#make some spare variables for tax calcs
t30 = float(0)
t5_1 = float(0)
t5_2 = float(0)

#fetch monthly income value
mi = int(input("Please provide monthly income: "))

#check if greater than 38000
if mi > 0:
    if mi > 38000:
        mi = mi - 38000
        t30 = 11400
        #check if more or less than 18000
        if mi > 12000:
            #if more than 18000 the 18000 kr is taxed at 6300kr. then calculate the next sum
            mi = mi - 12000
            t5_1 = 4200
            #everything over 50000 is taxed at 40%
            t5_2 = mi * 0.4
        #if less than 18000 then just do tax noramally again
        else:
            t5_1 = mi*0.35
    else:
        t30 = mi*0.3
else:
    print("Your monthly income isn\'t positive! Cannot be taxed.")

#make new variable for total tax
t30 = round(t30,1)
t5_1 = round(t5_1)
t5_2 = round(t5_2,1)
total = t30 + t5_1 + t5_2   
print("Corresponding income tax: ",total)