def read_file(path, sep):
    with open(path, "r") as file:
        data = file.readlines()
        numbers_string_list = ",".join(data).replace("\n", "").split(sep)
        cleaned_data = []
        for i in numbers_string_list:
            cleaned_data.append(int(i))
        return cleaned_data


def mean(data):
    return round((sum(data) / len(data)), 1)


def std(data):
    avg = mean(data)
    squared = []

    for i in data:
        sqr = (i - avg) ** 2
        squared.append(sqr)

    vari = sum(squared) / len(data)
    return round((vari ** 0.5), 1)


# the two data files
data_A = read_file("data/file_10k_integers_A.txt", ",")
data_B = read_file("data/file_10k_integers_B.txt", ":")

# result for 10k A
print("\nResults for file A:")
print(f"mean = {mean(data_A)}, standard deviation = {std(data_A)}\n")

# result for 10 k B
print("Results for file B:")
print(f"mean = {mean(data_B)}, standard deviation = {std(data_B)}\n")
