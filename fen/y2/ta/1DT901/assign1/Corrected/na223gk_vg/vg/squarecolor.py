var  = input("Enter a chess square identifier: ")

var_num = int(var[1])
alb = ["a","b","c","d","e","f","g","h"]
for i in range(1,9):
    final = ""
    if((i + var_num) % 2 == 0 ) :     
        final = var +" is White"
    else:
        final = var + " is Black"
    
print(final)
    







