#Choose number
num = int(input("Provide a three digit number: "))

#Separate digits
dig3 = num%10
dig2 = (num//10)%10
dig1 = num//100

#Result
print(f"The sum of the 3 numbers are {dig1+dig2+dig3}")
