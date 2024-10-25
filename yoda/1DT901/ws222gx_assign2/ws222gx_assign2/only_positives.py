print("Enter positive integers. End by giving a negative integer.")
positive_number_lst = []
user_input = int(input("Integer 1: "))
count = 1

while user_input >= 0:
    count += 1
    positive_number_lst.append(user_input)
    user_input = int(input(f"Integer {count}: "))

print(f"Number of positive integers: {count-1}")
print("Positive numbers: ", end="")
for num in positive_number_lst:
    print(num, end=", ",)
