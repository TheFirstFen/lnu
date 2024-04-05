#inmatning av 'price' och 'payment'
pr = float(input('Price: '))                     
pay = float(input('Payment: '))       

# c = pengar som betalas tillbaks i mynt och sedlar (vaxelpengar)
c = pay - pr                        
roundC = round(c,0)

b = (((c % 1000) % 500) % 200)
a = (( b % 100) % 50) % 20

tenHundred = roundC // 1000                
fiveHundred = (roundC % 1000) // 500       
twoHundred = ((c % 1000) % 500) // 200
hundred = b // 100
fifty = ( b % 100) // 50    
twenty = (( b % 100) % 50) // 20
ten = a // 10
five = ( a % 10) // 5
two = (( a % 10) % 5) // 2
one = ((( a % 10) % 5) % 2) // 1

#avrundning 
rtenHund = round (tenHundred)
rfiveHund = round(fiveHundred)
rtwoHund = round(twoHundred)
rHund = round(hundred)
rfifty = round(fifty)
rtwenty = round(twenty)
rten = round(ten)
rfive = round(five)
rtwo = round(two)
rone = round(one)

print(' 1000 kr:', rtenHund, "\n", '500kr:', rfiveHund, "\n", '200kr:', rtwoHund, "\n", '100kr:', rHund)
print(' 50 kr:', rfifty, "\n", '20 kr:', rtwenty, "\n", 'tio kr:', rten, "\n", 'fem kr:', rfive)
print(' 2 kr:', rtwo, "\n", '1 kr:', rone)
