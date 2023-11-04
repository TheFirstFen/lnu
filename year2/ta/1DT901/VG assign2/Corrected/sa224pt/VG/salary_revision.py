salaries = input("Provide salaries: ")

s_lst = []
median = 0
average = 0
gap = 0
sum = 0

# make the input string into a list
for i in salaries.split(" "):
    s_lst.append(int(i))
    sum += int(i)

# sort the list
s_lst.sort()

# check if list is even or odd to get the median
s_list_index = int(len(s_lst) / 2)
if len(s_lst) % 2 == 0:
    median = int((s_lst[s_list_index] + s_lst[s_list_index - 1])/2)
else:
    median = int(s_lst[s_list_index])

# get the average of the list
average = round(sum / len(s_lst))

# get the gap
gap = s_lst[-1] - s_lst[0]

print(f"Median: {median}\naverage: {average}\nGap: {gap}")
