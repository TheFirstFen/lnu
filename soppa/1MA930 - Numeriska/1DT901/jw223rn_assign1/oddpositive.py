from random import randint      #imports the randint command

rand = randint(-10,10)      #calculates a random number between -10, 10

#calculate if the number is negative, positive or zero.
if rand < 0:
    np = "negative"
elif rand > 0:
    np = "positive"
else:
    np = "neither positive nor negative"

#calculates whether the number is odd or even.
if (rand % 2) == 0:
    oe = "even"
else:
    oe = "odd"

print(f"The generated random number is {rand}")
print(f"{rand} is {oe} and {np}")


