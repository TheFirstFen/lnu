#Price and change display
price = 1950000
print("Price: ", price)
payment = float(input("Payment: "))
change = payment - price
print ("Change: ", change)

#Computing results
bill_Kilo = round(change) // 1000
change = change-bill_Kilo*1000
bill_halfKilo = round(change) // 500
change = change-bill_halfKilo*500
bill_2Hekta = round(change)//200
change = change-bill_2Hekta*200
bill_Hekta = round(change)//100
change = change-bill_Hekta*100
bill_halfHekta = round(change)//50
change = change-bill_halfHekta*50
bill_2Deca = round(change)//20
change = change-bill_2Deca*20
bill_Deca = round(change)//10
change = change-bill_Deca*10
bill_halfDeca = round(change)//5
change = change-bill_halfDeca*5
bill_2 = round(change)//2
change = change-bill_2*2
bill_1 = round(change)//1


#Display results
print (f"1000kr:  {bill_Kilo}")
print (f"500kr:   {bill_halfKilo}")
print (f"200kr:   {bill_2Hekta}")  
print (f"100kr:   {bill_Hekta}")
print (f"50kr:    {bill_halfHekta}")
print (f"20kr:    {bill_2Deca}")
print (f"10kr:    {bill_Deca}")
print (f"5kr:     {bill_halfDeca}")
print (f"2kr:     {bill_2}")
print (f"1kr:     {bill_1}")