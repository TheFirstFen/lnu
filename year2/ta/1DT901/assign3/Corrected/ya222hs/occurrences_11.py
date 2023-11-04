import random


# Funktion som räknar antalet förekomster av varje värde i lista
def count_occurrences(lst):
    count = {}  # Ordbok för att lagra antal förekomster
    for i in lst:
        if i in count:
            count[i] += 1  # om värdet finns, öka räknaren
        else:
            count[i] = 1  # Lägg till värdet i ordboken med räknaren till 1
    return {key: value for key, value in sorted(count.items())}


# Skapar en lista med 100 slumpmässiga heltal mellan 1 och 10
ra_numbers = [random.randint(1, 10) for _ in range(100)]
answer = count_occurrences(ra_numbers)
# Skriver ut antalet förekomster av varje tal
for key, value in sorted(answer.items()):
    print(key, "\t", value)
