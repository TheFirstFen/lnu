#read input
p = float(input('Price: '))
m = float(input('Payment: '))

#change
n = m - p
c = round(n)
print('Change: ', c, 'kr')

#compute change
b1000 = c//1000
c %= 1000
b500 = c//500
c %= 500
b200 = c//200
c %= 200
b100 = c//100
c %= 100
b50 = c//50
c %= 50
b20 = c//20
c %= 20
c10 = c//10
c %= 10
c5 = c//5
c %= 5
c2 = c//2
c %= 2
c1 = c//1
c %= 1

#present result
print('1000kr bills: ',b1000)
print(' 500kr bills: ',b500)
print(' 200kr bills: ',b200)
print(' 100kr bills: ',b100)
print('  50kr bills: ',b50)
print('  20kr bills: ',b20)
print('  10kr coins: ',c10)
print('   5kr coins: ',c5)
print('   2kr coins: ',c2)
print('   1kr coins: ',c1)
