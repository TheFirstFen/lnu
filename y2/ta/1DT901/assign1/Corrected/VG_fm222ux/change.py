#Input of price and payment
price = float(input("Price: "))
payment = int(input("Payment: "))

#Calculation and presentation of change
change = round(payment-price) 
print(f"\nChange: {change} kr")

#Calculation of amount bills and rest
tusen = change//1000 
rest1000 = change%1000 
fem_hundra= rest1000//500 
rest500 = rest1000%500 
tva_hundra = rest500//200 
rest200 = rest500%200 
hundra = rest200//100 
rest100 = rest200%100 
femtio = rest100//50 
rest50 = rest100%50 
tjugo = rest50//20
rest20= rest50%20
tio =rest20//10
rest10= rest20%10
fem = rest10//5
rest5 = rest10%5 
tva = rest5//2
rest2= rest5%2
en= rest2//1
rest1= rest2%1 

#Result
print(f"1000 kr bills: {tusen}")
print(f"500 kr bills: {fem_hundra}")
print(f"200 kr bills: {tva_hundra}")
print(f"100 kr bills: {hundra}")
print(f"50 kr bills: {femtio}")
print(f"20 kr bills: {tjugo}")
print(f"10 kr bills: {tio}")
print(f"5 kr bills: {fem}")
print(f"2 kr bills: {tva}")
print(f"1 kr bills: {en}")
















