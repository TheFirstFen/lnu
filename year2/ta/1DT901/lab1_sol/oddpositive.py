import random

# Classify a random number [-10,10] as
# odd/even and positive/negative

n = random.randint(-10, 10)
print("The generated number is", n)

oddeven = "odd" if n % 2 == 1 else "even"

if n > 0:
    posneg = "positive"
elif n < 0:
    posneg = "negative"
else:
    posneg = "neither positive nor negative"

print(n, "is ", oddeven, " and ", posneg)
