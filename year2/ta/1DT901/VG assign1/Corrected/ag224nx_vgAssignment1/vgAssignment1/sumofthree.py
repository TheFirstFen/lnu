#inmatning av talet
numbers = int( input('Provide a 3 digit number: '))     

#variablar for varje siffra i talet
a1 = int(numbers /100)                                  
a2 = int (( numbers % 100 ) // 10)     
a3 = int(numbers % 10)               

print ('Sum of digits:',a1 + a2 + a3)

