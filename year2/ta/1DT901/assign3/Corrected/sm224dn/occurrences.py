import random

# funktion som ska generara en slump massit tal 100 gånger från 1 till 10
def random_namburse():
    return [random.randint(1, 10) for x in range(100)]

# fontion som innehåller en lista som ska spara de nummer och räkna de 
def count_occurrences(lst):
    occurrences = {}
    for i in range(1, 11):
        occurrences[i] = lst.count(i)
    return occurrences

# här ska printa de i ordning hur mycket 1 or fick man 
number = random_namburse()
result = count_occurrences(number)
for i in range(1, 11):
    print(f"{i}: {result[i]}")
