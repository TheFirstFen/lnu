import random


def creat_random():
    seq = []  # Töm lista, random nr kommer attt läggas till här
    i = 0  # while counter
    while i < 100:
        i += 1
        n = random.randint(1, 200)
        seq.append(n)
    return different(seq)  # returna funktionen med listan i så den körs direkt 


def different(seq):
    uniqe = set(seq)  # använda mängd för att behålla unika tal
    uniqe = sorted(uniqe)  # sortera listan
    print(f"Different integers:\n{uniqe}")


creat_random()
