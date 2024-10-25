import math


def mean(lst):
    sum_value = sum(lst)
    length = len(lst)
    return sum_value / length


def std(lst):
    mean_value = mean(lst)
    sum_sqr_diff = sum((x - mean_value) ** 2 for x in lst)
    length = len(lst)
    return math.sqrt(sum_sqr_diff / length)


file_A = (
    '/Users/alaa/Desktop/Inledande Prgrammering/'
    'assignment-03/file_10k_integers_A.txt'
)
file_B = (
    '/Users/alaa/Desktop/Inledande Prgrammering/'
    'assignment-03/file_10k_integers_B.txt'
)

with open(file_A) as f:
    numbers_A = [int(x) for line in f for x in line.strip().split(',')]

print('Results for file A:')
mean_A = mean(numbers_A)
std_A = std(numbers_A)
print(f'mean = {mean_A:.1f}, standard deviation = {std_A:.1f}')

with open(file_B) as f:
    numbers_B = [int(x) for line in f for x in line.strip().split(':')]

print('Results for file B:')
mean_B = mean(numbers_B)
std_B = std(numbers_B)
print(f'mean = {mean_B:.1f}, standard deviation = {std_B:.1f}')
