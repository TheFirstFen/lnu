import random 

gen_num = random.randint(-10, 10)
print("The generated number is", gen_num)
# checks if the number is positive or negative or neither
if (gen_num > 0):
    if gen_num % 2 == 0:
        print(gen_num, "is even and positive")
    else:
        print(gen_num, "is odd and positive")

elif (gen_num < 0):
    if gen_num % 2 == 0:
        print(gen_num, "is even and negative")
    else:
        print(gen_num, "is odd and negative")

else:
    print(gen_num, "is even and neither positive nor negative")
