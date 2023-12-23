import os
from math import sqrt


def mean(int_lst):
    summa = 0
    for i in range(0, len(int_lst)):
        summa += int_lst[i]
    medel = summa / (len(int_lst))

    return medel


def std(int_lst):
    summan = 0
    standardD = 0
    antal_heltal = len(int_lst)

    medelvarde = mean(int_lst)
    for i in range(0, antal_heltal - 1):
        summan += ((int_lst[i] - medelvarde) ** 2)

    standardD = sqrt(summan / (antal_heltal - 1))
    return standardD


def read_file_to_intlist(File_path):
    talstrangen = ''
    intList = []
    with open(File_path) as infile:
        content = infile.read()

    antal_heltal = len(content)
    for i in range(0, antal_heltal):
        if content[i] == '-' or content[i].isdigit():
            talstrangen += content[i]
        else:
            if len(talstrangen) > 0:
                intList.append(int(talstrangen))
                talstrangen = ''

    if len(talstrangen) > 0:
        intList.append(int(talstrangen))

    return intList


# program starts
path1 = os.getcwd() + '/data/file_10k_integers_A.txt'
path2 = os.getcwd() + '/data/file_10k_integers_B.txt'


print('Fil A')
intList = read_file_to_intlist(path1)
medelsum = round((mean(intList)), 1)
avvikelse = round((std(intList)), 1)

print('Mean:', medelsum, 'Standard deviation:', avvikelse)


print('\nFil B:')
intList2 = read_file_to_intlist(path2)
medelsuum2 = round((mean(intList2)), 1)
avvikelse2 = round((std(intList2)), 1)
print('Mean:', medelsuum2, 'Standard deviation:', avvikelse2)
