import random


# Funktion som gör om en lista till en mängd för att få bort dupletter
# Därefter görs det tillbaka till en lista som sorteras
def different(lst):
    new_set = set(lst)
    new_list = sorted(list(new_set))
    return new_list


# 100st random nummer
random_list = []
for num in range(100):
    random_list.append(random.randint(1, 200))

# Main program

sorted_list = different(random_list)
print("Different integers:")
print(sorted_list)
