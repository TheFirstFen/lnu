#Read input
N = input("Provide a three digit number:")
N = int(N)

#Compute
N1 = (N//100)
N2 = (N%100//10)
N3 = (N%10)

#Present result
print(N1+N2+N3)