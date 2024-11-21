user_input = 11


for i in range(user_input-1, -1, -2):
    empty_space = " "*((i//2)+1)    # creates the empty space
    print(empty_space, "*"*(user_input-i))

# print("", "*"*(user_input+2))
for j in range(0, user_input+1, 2):
    empty_space = " "*((j//2)+1)
    print(empty_space, "*"*(user_input-j))
