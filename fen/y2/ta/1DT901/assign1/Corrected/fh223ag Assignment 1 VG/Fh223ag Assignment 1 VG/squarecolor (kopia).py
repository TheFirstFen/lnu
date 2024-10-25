#Ask the user for a square
square = input("Enter a chess square identifier (e.g. e5): ")

#divide the entered square to different variables 
user_s = square[0]
user_i = int(square[1])

#create two lists based on if the letter has white at an odd or even number
white_even = ["a", "c", "e", "g"]
white_odd = ["b", "d", "f", "h"]


#a, c, e, g has black at odd numbers b, d, f, h has white at odd numbers. now find if number is even or odd and if its black or white
if(user_s in white_even and user_i % 2 == 0):
    print(f"\n{square} is White")
elif(user_s in white_even and user_i % 2 != 0):
    print(f"\n{square} is Black")

if(user_s in white_odd and user_i % 2 == 0):
    print(f"\n{square} is Black")
elif(user_s in white_odd and user_i % 2 != 0):
    print(f"\n{square} is White")