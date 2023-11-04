
def is_positive_and_odd(n):
    return n>0 and n%2==1

# Program starts 
count = 0
n = int( input("Enter a positive and odd integer: ") )

while not is_positive_and_odd(n) and count < 4:
    print("Integer must be positive and odd. Try again!")
    n = int( input("Enter a positive and odd integer: ") )
    count += 1

if count < 5:
    print("Received positive odd number ", n)
else:
    print("Failed to read a positive and odd integer")    

