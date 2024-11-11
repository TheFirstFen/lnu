from random import randint

n = int(input("Enter number of integers to be generated: "))

inu = n
max = 0
min = 100
avn = 0

if n < 0:
    print("Please provide a positive integer.")
else:
    print("Generated numbers: ", end="")
    for i in range(0, 101):
        ranum = randint(1, 100)
        if n == 0:
            print(end="\n")
            print(f"Average, min, and max are {(avn / inu)}, {min}, and {max}")
            break
        else:
            print(ranum, end=" ")
            avn = avn + ranum
            if ranum > max and ranum < min:
                max = ranum
                min = ranum
            elif ranum > max:
                max = ranum
            elif ranum < min:
                min = ranum
            n += -1
