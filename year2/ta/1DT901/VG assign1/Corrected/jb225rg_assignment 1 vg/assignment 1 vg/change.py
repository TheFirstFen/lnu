price= float(input("Price: ")) #input price

payment = float(input("Payment: ")) #input payment
                
change = payment - price #calculate change
round(change) #rounded of to whole kronor 
change = int(change) #chnge to int to gt rid of the decimals
print(f"\nchange: {change} kr") #print the change amount

thousend = change//1000 #calculation of amount of 1000kr bills in change
change = change % 1000 #remove the amount of money given in change in 1000kr bills

five_hundered = change//500 #calculation
change = change % 500  #remove given change

two_hundered = change//200 #calculation
change = change % 200 #gremove iven change

hundered = change//100 #calculation
change = change % 100  #remove given change

fifty = change//50 #calculation
change = change % 50 #remove given change

twenty = change//20 #calculation
change = change % 20 #remove given change

ten = change//10 #calculation
change = change % 10  #remove given change

five = change//5 #calculation
change = change % 5  #given change

two = change//2 #calculation
change = change % 2  #given change

one = change #the change that is still left is the 1kr change

#print out the amount of each bill/coin
print(f"1000kr bills: {thousend}\n 500kr bills: {five_hundered}\n 200kr bills: {two_hundered}\n 100ke bills: {hundered}\n"
       + f"  50kr bills: {fifty}\n  20kr bills: {twenty}\n  10kr coins: {ten}\n   5kr coins: {five}\n   2kr coins: {two}\n"
      + f"   1kr coins: {one}")

#there has to be a more efficiant way of calculating the change and remove the alreqdy given change 
#but this is what i came up with