
#Price
p = float(input("Price: "))

#Patment
P= float(input("Payment: "))

#Change
c = round(P-p)

#1000kr bills
c1000 = c// 1000
cr1000 = c % 1000

#500kr bills
c500 = cr1000// 500
cr500 = cr1000 % 500

#200kr bills
c200 = cr500 // 200
cr200 = cr500 % 200

#100kr bills
c100 = cr200//100
cr100 = cr200 % 100

#50 kr bills
c50 = cr100 // 50
cr50 = cr100 % 50

#20kr bills
c20 = cr50 // 20
cr20 = cr50 % 20

#10kr coin
c10 = cr20 // 10
cr10 = cr20 % 10

#5kr coin 
c5 = cr10 // 5
cr5 = cr10 % 5

#2kr coin 
c2 = cr5 // 2
cr2 = cr5 % 2

#1kr coin 
c1 = cr2

#print result
print("Change: ", c)
print(f""" 1000kr bills: {c1000}\n 500kr bills: {c500}\n 200kr bills: {c200}\n 100kr bills: {c100}\n 50kr bills: {c50} 
 20kr bills: {c20}\n 10kr coins: {c10}\n 5kr coins: {c5}\n 2kr coins: {c2}\n 1kr coins: {c1}""")