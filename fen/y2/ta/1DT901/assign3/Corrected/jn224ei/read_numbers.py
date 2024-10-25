import os


# Funktion som läser filen, tar fram alla värden och lägger in dem i en lista
def read(path):
    doc = open(path, "r", encoding="utf-8")
    numbers_ints = []
    numbers = doc.read()
    for char in numbers:
        if char not in allowed_chars:
            numbers = numbers.replace(char, " ")
    numbers_list = numbers.split()
    for n in numbers_list:
        numbers_ints.append(int(n))
    return numbers_ints


# Funktion som räknar ut medelvärde på alla värden i listan
def mean(lst):
    sum = 0
    for number in lst:
        sum += number
    return sum/len(lst)


# Funktion som räknar ut "standard deviation" beroende på värden i listan samt
# listans medelvärde
def std(lst):
    mean_number = mean(lst)
    new_list = []
    for number in lst:
        new_list.append((number-mean_number)**2)
    new_mean = mean(new_list)
    return new_mean**0.5


# Main program
allowed_chars = "1234567890- "
path = os.getcwd()
print(path)
input_file1 = 'data/file_10k_integers_A.txt'
input_file2 = 'data/file_10k_integers_B.txt'
numbers_list1 = read(input_file1)
numbers_list2 = read(input_file2)

print("Results for file A:")
mean1 = round(mean(numbers_list1), 1)
std1 = round(std(numbers_list1), 1)
print(f"mean = {mean1}, standard deviation = {std1}")

print()

print("Results for file B:")
mean2 = round(mean(numbers_list2), 1)
std2 = round(std(numbers_list2), 1)
print(f"mean = {mean2}, standard deviation = {std2}")
