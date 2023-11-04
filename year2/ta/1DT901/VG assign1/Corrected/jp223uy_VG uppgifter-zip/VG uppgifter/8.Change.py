#Read input

p=float(input("Price:"))
P=int(input("Payment:"))


c=round(P-p)
#Compute

r=c%1000
print("Change:",r,"kr")

r=c//1000
print("1000kr Bills:",r)

r=c//500
print("500kr Bills:",r)

r=c//200//10
print("200kr Bills:",r)

r=c%100//20
print("100kr Bills:",r)

r=c%50//100
print("50kr Bills:",r)

r=c//20%2
print("20kr Bills:",r)

r=c%10//10
print("10kr Coins:",r)

r=c//5%2
print("5kr Coins:",r)

r=r%2
print("2kr Coins:",r)

r=r%1
print("1kr Coins:",r)

