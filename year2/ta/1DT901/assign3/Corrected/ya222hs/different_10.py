import random


# funktion returnerar sorterad lista
def different(lst):
    uniq_lst = sorted(set(lst))
# kovertera lista till set för tar bort dubletter
    return uniq_lst


random_value = random.sample(range(1, 200), 100)
# skapa en lista med 100 slumpmässiga mella 1 till 199
uniq_lst = different(random_value)  # kalla list genom funktionet
# printa de unika värden
print("Different integers:")
print(uniq_lst)
