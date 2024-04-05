import os

# en finktion som ska läsa


def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

# en finktion som ska skriva de en in fil


def write_file(lines, file_path):
    with open(file_path, "w") as file:
        file.writelines(lines)
    print("Text saved in file\n", output_path)


path = os.path.join(os.getcwd(), "mamma_mia.txt")
# här vissar jag hur mycker linje det innehåller
lst = read_file(path)
print(f"Read {len(lst)} lines from file\n {path}")
# Och har ska vissas en output fil
output_path = os.path.join(os.getcwd(), "output.txt")
write_file(lst, output_path)
