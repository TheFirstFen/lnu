x = int(input("price:"))
y = int(input("payment:"))

# change, subbtrahera price med payment
n = int((y)-(x))

# 1000kr
a = int(1000)
# 628//1000= 0
a1 = n//a
# 628%1000= 628
a2 = n % a

# 500kr
b = int(500)
# 628//500= 1
b1 = a2//b
# 628%500= 128
b2 = a2 % b

# 200kr
c = int(200)
# 128//200= 0
c1 = b2//c
# 128%200= 128
c2 = b2 % c

# 100kr
d = int(100)
# 128//100= 1
d1 = c2//d
# 128%100= 28
d2 = c2 % d

# 50kr
e = int(50)
# 28//50= 0
e1 = d2//e
# #28%50= 28
e2 = d2 % e

# 20kr
f = int(20)
# 20//28= 1
f1 = e2//f
# 28%20= 8
f2 = e2 % f

# 10kr
g = int(10)
# 8//10= 0
g1 = f2//g
# 8%10= 8
g2 = f2 % g

# 5kr
h = int(5)
# 8//5= 1
h1 = g2//h
# 8%5= 3
h2 = g2 % h

# 2kr
i = int(2)
# 3//2= 1
i1 = h2//i
# 3%2= 1
i2 = h2 % i

# 1kr
j = int(1)
# 2//1= 1
j1 = i2//j
# 2%1= 0
j2 = i2 % j

print(f"""change: {n}
       1000kr bills: {a1}
       500kr bills: {b1}
       200kr bills: {c1}
       100kr bills: {d1}
       50kr bills: {e1}
       20kr bills: {f1}
       10kr coins: {g1}
       5kr coins: {h1}
       2kr coins: {i1}
       1kr coins: {j1}""")
