# calculating the median of the list
def median(lst):
    lst = sorted(lst)
    length_of_lst = len(lst)

    # checks if the length of lst is odd
    if length_of_lst % 2 == 1:
        # If it's odd, grab the middle value by dividing the list length by 2
        median_calc = round(lst[length_of_lst // 2])

    else:
        # else it calculates the median as the average of the two middle values
        mid_left = lst[(length_of_lst // 2) - 1]
        mid_right = lst[(length_of_lst // 2)]
        median_calc = (mid_left + mid_right) / 2

    return round(median_calc)


# calculating the average of the list
def average(lst):
    return round(sum(lst) / len(lst))


# calculating the gap of the list
def gap(lst):
    return max(lst) - min(lst)


salry_input = input("Provide salaries: ")

# creating the list and putting all the salaries in the list
salary_lst_str = salry_input.split()
salary_lst = [int(num) for num in salary_lst_str]


# grabs and prints the values for: median, average and gap
print("Median:", (median(salary_lst)))
print("Average:", average(salary_lst))
print("Gap:", gap(salary_lst))
