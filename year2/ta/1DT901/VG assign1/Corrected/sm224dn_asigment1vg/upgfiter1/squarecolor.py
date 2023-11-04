n= input("Enter a chess square identifier (e.g. e5):")

letter_a_to_h = {"a": 1, "b":2, "c":3,"d":4,"e":5,"f":6,"g":7,"h":8}


n1 = n[0]

n2 = int(n[1])

letter_number = letter_a_to_h[n1]


if (letter_number + n2)% 2 == 0:
    color="black"
else: 
    color= "white" 
print (f"{n} is {color}")