# funktion för att beräkna medelvärde
def mean(lst):
    return sum(lst) / len(lst)


# funktion för att beräkna standard divition
def std(lst):
    avg = mean(lst)  # varjabel till funktionen medelvärde
    vac = sum([(xi - avg) ** 2 for xi in lst]) / (len(lst) - 1)
    return vac ** 0.5  # skrivit av hela beräkning till stand.dev.
# som är i länken i frågan


# Bereda filen A för att läsas
file = open("/data/file_10k_integers_A.txt", "r")
all = file.read().strip()
file.close()

# rensera allting i filen och föra in dem i de båda funktionerna
all = all.replace("\n", ",")
num = list(map(int, all.split(",")))  # lägga siffrorna i in lista
avg = mean(num)
std_dev = std(num)

# printa
print("Results for file A:")
print(f"mean = {avg:.2f}, standard deviation {std_dev:.2f}")

print()
# bereda filen B för att läsas
file = open("/data/file_10k_integers_B.txt", "r")
all = file.read().strip()
file.close()

# rensera allting i filen och föra in dem i de båda funktionerna
num = list(map(int, all.split(":")))
avg = mean(num)
std_dev = std(num)

# printa
print("Results for file B:")
print(f"mean = {avg:.2f}, standard deviation {std_dev:.2f}")
