square = str(input("Enter a chess square identifier (e.g. e5): "))

chars = ["a","b","c","d","e","f","g","h"]
nums = ["1","2","3","4","5","6","7","8"]
result = [0,0]
i = 0

for i in range(7):
    if chars [i] in square:
        result[0] = i+1
    if nums [i] in square:
        result[1] = i+1
        
if (result[0]%2 == 0 and result[1]%2 == 0) or (result[0]%2 != 0 and result[1]%2 != 0):
    print(square + " is black")
else:
    print (square + " is white")