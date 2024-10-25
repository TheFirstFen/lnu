a = int(input("Enter a number here: "))
b = int(input("Enter another number here: "))
c = int(input("Enter your last number here: "))

if a>b>c:
    print("{} is the largest number".format(a))
elif a<b<c:
    print("{} is the largest number".format(c))
else: 
    print("{} is the largest number".format(b))