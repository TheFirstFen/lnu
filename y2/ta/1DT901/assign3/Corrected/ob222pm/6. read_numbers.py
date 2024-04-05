import os


def readfile(path):
    with open(path + "/data/file_10k_integers_A.txt", "r") as file:
        temp = file.readlines()
        lst1 = []
        num = ''
        for line in temp:
            line = line.replace(', ', ' ').replace('\n', ' ')
            for number in line:
                if ord(number) == 32:
                    lst1.append((int(num)))
                    num = ''
                else:
                    num += number

    with open(path + "/data/file_10k_integers_B.txt", "r") as file:
        temp = file.readlines()
        lst2 = []
        num = ''
        for line in temp:
            line = line.replace(':', ' ')
            for number in line:
                if ord(number) == 32:
                    lst2.append((int(num)))
                    num = ''
                else:
                    num += number

    return lst1, lst2


def mean(lst):
    sum = 0
    for num in lst:
        sum += num
    return round(sum / len(lst), 1)


def std(lst, mean):
    sum = 0
    for i in lst:
        i -= mean
        i = i ** 2
        sum += i
    return round(((sum/len(lst)) ** 0.5), 1)


path = os.getcwd()
lst1, lst2 = readfile(path)

mean1 = mean(lst1)
mean2 = mean(lst2)

print("Result for file A")
print(f"mean = {mean1}, standard deviation =", std(lst1, mean1))

print("\nResult for file B")
print(f"mean = {mean2}, standard deviation =", std(lst2, mean2))
