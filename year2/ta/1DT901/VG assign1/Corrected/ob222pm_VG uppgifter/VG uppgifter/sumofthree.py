# read input
n = int(input ("Provide a three digit number: "))

# compute, first number
fn = n//100
# second number
sn = n%100//10
# third number
tn = n%10

# present result 
print (fn + sn + tn)