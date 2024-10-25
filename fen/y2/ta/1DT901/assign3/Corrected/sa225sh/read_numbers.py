import os


def read_files(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            file_content = file.read()
            file_name = file.name
            name_lst = file_name.split(R'\\\\')
            print(name_lst)
            if name_lst[0][-5] == "A":  # ifall nämnet av filen avslutas med A 
                return [int(x) for x in file_content.replace(',', ' ').split()]
            if name_lst[0][-5] == "B":  # ifall nämnet av filen avslutas med B
                return [int(x) for x in file_content.replace(':', ' ').split()]


def calc_mean(lst):
    length = len(lst)
    ans = sum(lst)
    return round((ans / length), 1)


def calc_std(lst):
    mean = calc_mean(lst)
    sqr_diff = [(mean - x) ** 2 for x in lst]
    mean_sqr = sum(sqr_diff) / len(lst)
    sqr_root = mean_sqr ** 0.5
    return round(sqr_root, 1)


def send_info(lst):
    for file_data in lst:
        if file_data:  # Check if the file data is not empty
            print(f"Mean: {calc_mean(file_data)}" +
                  f"Std: {calc_std(file_data)}")
            # Kalla på funktioner i print
        else:
            print("File data is empty or file not found")


path = os.getcwd() + "/data/file_10k_integers_A.txt"
file_1 = read_files(path)
path_2 = os.getcwd() + "/data/file_10k_integers_B.txt"
file_2 = read_files(path_2)
lst = [file_1, file_2]  # lista som innehåler data från file1, file2
send_info(lst)  # skickas till sendInfo för att beräknas
