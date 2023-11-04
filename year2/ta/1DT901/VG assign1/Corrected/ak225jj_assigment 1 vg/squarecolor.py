
#read input 
s = str(input("Enter a chess square identifier (e.g. e5): "))

#diffrent chess letters
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"

# a c e g
if s[0] == a or s[0] == c or s[0] == e or s[0] == g:
    if int(s[1]) % 2 == 0:
        print(s, "is White")
    elif int(s[1]) % 2 == 1:
        print(s, "is Black")

if s[0] == b or s[0] == d or s[0] == f or s[0] == h:
    if int(s[1]) % 2 == 0:
        print(s, "is Black")
    elif int(s[1]) % 2 == 1:
        print(s, "is White")
