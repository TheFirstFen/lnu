# Input
sum = float(input("Payment: "))
price = float(input("Cost: "))
# Calculation for change
change = round(sum - price)
"\n"
print("change:", change)



# Spliting the change by using module and //
a = change // 1000
b = change %1000 // 500
c = change %1000 %500 // 200
d = change %1000 %500 %200 // 100
e = change %1000 %500 %200 %100 // 50
f = change %1000 %500 %200 %100 %50 // 20
g = change %1000 %500 %200 %100 %50 %20 //10
h = change %1000 %500 %200 %100 %50 %20 %10 //5
i = change %1000 %500 %200 %100 %50 %20 %10 %5 //2
j = change %1000 %500 %200 %100 %50 %20 %10 %5 %2 //1

#Printing all different values
print("1000kr Bill: ",a)
print("500kr Bill: ",b)
print("200kr Bill: ",c)
print("100r Bill: ",d)
print("50kr Bill: ",e)
print("20kr Bill: ",f)
print("10kr Bill: ",g)
print("5kr Bill: ",h)
print("2kr Bill: ",i)