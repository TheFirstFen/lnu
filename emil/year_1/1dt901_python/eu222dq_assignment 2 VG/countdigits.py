# taking a input and storing it as num_str
num_str = str(input("Write a large number here: "))
# starting amount of even
even_amount = 0
# Starting amount of odd
odd_amount = 0
# starting amount of zeros
zero_amount = 0
# value that holeds the position in the string
i = 0

# looping as long as i is less than the input
while i < len(num_str):
    # checking if s is the inputed string
    for s in num_str:
        # when s is even we add a count to even and go on to the next value
        if s == '2' or s == '4' or s == '6' or s == '8':
            even_amount += 1
            i += 1
        # if s is zero ve add one to the count and goes on to the next value
        elif s == '0':
            zero_amount += 1
            i += 1
        # Otherwise we add one to odd and move to the next value
        else:
            odd_amount += 1
            i += 1

# We now print how many odd, even and zeros the input contained
print(f"Odd: {odd_amount} \nEven: {even_amount} \nZero: {zero_amount}")
