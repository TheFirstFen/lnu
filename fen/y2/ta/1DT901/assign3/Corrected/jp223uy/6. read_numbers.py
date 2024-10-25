import os


def read_file(path):
    with open(path + "/data/file_10k_integers_A.txt", "r") as file:
        temp = file.readlines()  # Reading all lines
        lst1 = []
        num = ''
        for line in temp:
            line = line.replace(', ', ' ').replace(
                '\n', ' ')  # None wanted objects
            for number in line:  # check the new lst made
                if ord(number) == 32:  # 32 equals space
                    lst1.append((int(num)))  # Append with all numbers
                    num = ''
                else:
                    num += number

    with open(path + "/data/file_10k_integers_B.txt", "r") as file:
        temp = file.readlines()  # Read everything in file
        lst2 = []
        num = ''
        for line in temp:
            line = line.replace(':', ' ')  # Replace : with space
            for number in line:  # For loop on previous loop
                if ord(number) == 32:
                    lst2.append((int(num)))
                    num = ''
                else:
                    num += number

    return lst1, lst2  # return the 2 new made lists


def mean(lst):  # Get the average
    sum = 0
    for num in lst:
        sum += num
    return round(sum / len(lst), 1)


def std(lst, mean):
    sum = 0
    for i in lst:  # Explenation found on internet, converted to python
        i -= mean
        i = i ** 2
        sum += i
    return round(((sum/len(lst))) ** 0.5, 1)  # Square root


# Program starts
path = os.getcwd()  # Current
lst1, lst2 = read_file(path)

mean1 = mean(lst1)
mean2 = mean(lst2)

print("Results for file A:")
print(f"Mean =  {mean1}, standard deviation =", std(lst1, mean1))

print("\nResults for file B:")
print(f"Mean =  {mean2}, standard deviation =", std(lst2, mean2))
