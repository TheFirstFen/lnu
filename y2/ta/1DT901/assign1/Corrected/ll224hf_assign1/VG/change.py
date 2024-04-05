#Price: 372.38
#Payment: 1000
#
#Change: 628 kr
#1000kr bills: 0
# 500kr bills: 1
# 200kr bills: 0
# 100kr bills: 1
#  50kr bills: 0
#  20kr bills: 1
#  10kr coins: 0
#   5kr coins: 1
#   2kr coins: 1
#   1kr coins: 1

#fetch total price
pr = float(input("List total price: "))
#fetch total payment
pa = float(input("List the total payment: "))
#calculate change
c = pa - pr
#round to nearest krona
c = round(c)
#how many 1000kr bills
kr1000 = c//1000
#remove from total
c = c - kr1000*1000
#how many 500kr bills
kr500 = c//500
#remove from total
c = c -kr500*500
#how many 200kr bills
kr200 = c//200
#remove from total
c = c - kr200*200
#how many 100kr bills
kr100 = c//100
#remove from total
c = c - kr100*100
#how many 50kr bills
kr50 = c//50
#remove from total
c = c - kr50*50
#how many 20kr bills
kr20 = c//20
#remove from total
c = c - kr20*20
#how many 10kr coins
kr10 = c//10
#remove from total
c = c - kr10*10
#how many 5kr coins
kr5 = c//5
#remove from total
c = c - kr5*5
#how many 2kr coins
kr2 = c//2
#remove from total
c = c - kr2*2
#how many 1kr coins
kr1 = c//1
#remove from total
c = c - kr1*1

#print all results
print("Change:",pa-pr,"kr")
print("1000kr bills:",kr1000)
print(" 500kr bills:",kr500)
print(" 200kr bills:",kr200)
print(" 100kr bills:",kr100)
print("  50kr bills:",kr50)
print("  20kr bills:",kr20)
print("  10kr coins:",kr10)
print("   5kr coins:",kr5)
print("   2kr coins:",kr2)
print("   1kr coins:",kr1)