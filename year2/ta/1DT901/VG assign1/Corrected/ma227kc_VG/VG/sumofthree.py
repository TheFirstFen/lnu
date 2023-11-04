#Recieving data from user
number = (int(input("Provide a number of three digits: ")))

#computing
first_dig = number // 100
mid_dig = number // 10
mid_dig = mid_dig % 10
last_dig = number % 10

#displaying results
print ("The sum of the three digits = ", last_dig + mid_dig + first_dig)