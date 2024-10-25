# Info from user
num = input("Enter a positive integer: ")
# Variables
ev = 0
odd = 0
zero = 0
if num.isdigit() is False:
    print("Please try inputting a number next time")
    exit()
# Computing
for i in range(len(num)):
    if int(num[i]) % 2 == 0 and int(num[i]) != 0:
        ev += 1
    elif int(num[i]) % 2 != 0:
        odd += 1
    else:
        zero += 1
# Displaying
print(" Even digits:", ev, "\n", "Odd digits:", odd, "\n", "Zeros:", zero)
