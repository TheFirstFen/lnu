# change_to_for.py
#
# Author: Samuel Berg
# Date: 01-Sep-2022

count = 0
sum = 0

while count < 100:
    sum = sum + count
    count = count + 1

print(sum)

#########################################################################

count = 0
sum = 0

for i in range(100):
    sum += count
    count += 1

print(sum)
