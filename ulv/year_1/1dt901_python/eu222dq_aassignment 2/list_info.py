import random

lista = []

for i in range(1, 101):
    n = random.randint(1, 10000)
    lista.append(n)

sum_list = sum(lista)
lenght_list = len(lista)

average_list = sum_list/lenght_list
lista.sort()

print(lista)
print("Maximal number in list: ", max(lista))

print("Minimal number in list", min(lista))

print("Average number in list: ", average_list)

print("Second largest value in list: ", lista[-2])
