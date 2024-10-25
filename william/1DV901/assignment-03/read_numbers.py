# computes and cleans file
def compute_and_clean_file(seprator, file_char):
    folder_path = "./data"

    with open(folder_path+f"/file_10k_integers_{file_char}.txt", "r") as file:
        content = file.readlines()
    combination = ",".join(content).replace("\n", "").split(seprator)
    return [int(num) for num in combination]


# calculate avg
def average(lst):
    amount_of_numbers = len(lst)
    return round(sum(lst) / amount_of_numbers, 1)


# standard deviation calculation
def std(lst):
    avg = average(lst)
    length = len(lst)
    total = 0

    for num in lst:
        part = (num - avg)**2
        total += part
    variance = (1/length) * total
    deviation = round(variance ** 0.5, 1)
    return avg, deviation


char_file_dict = {"A": ",", "B": ":"}
for char in char_file_dict:
    print(f"\nResults for file  {char}:")
    mean, deviation = std(compute_and_clean_file(char_file_dict[char], char))
    print(f"mean = {mean}, standard deviation = {deviation}")
