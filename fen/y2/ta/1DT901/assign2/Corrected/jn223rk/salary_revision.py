def main():
    salaries = input("Provide salaries: ")
    salary_list = salaries.split(" ")
    # print(salary_list)
    for i in range(len(salary_list)):
        salary_list[i] = int(salary_list[i])
    # print(salary_list)
    salary_list.sort()
    # print(salary_list)

    salary_median = 0
    if len(salary_list) % 2 == 1:
        salary_median = salary_list[len(salary_list) // 2]
    elif len(salary_list) % 2 == 0:
        mid_1 = salary_list[len(salary_list) // 2]
        mid_2 = salary_list[len(salary_list) // 2 + 1]
        salary_median = mid_1 + mid_2
    # print(salary_median)
    print("\nMedian: {}".format(round(salary_median)))

    salary_average = sum(salary_list) / len(salary_list)
    # print(salary_average)
    print("Average: {}".format(round(salary_average)))

    salary_gap = ((salary_list[0] - salary_list[-1]) ** 2) ** (1 / 2)
    # print(salary_gap)
    print("Gap: {}".format(round(salary_gap)))


if __name__ == "__main__":
    main()
