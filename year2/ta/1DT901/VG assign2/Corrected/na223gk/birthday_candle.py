# this are the known variables
max_age = 100 
one_box = 24

# ask for the age of the person
age = int(input("Enter the age of the person: "))


total_boxes = 0
total_candles = 0

# Loop through each year from the current age to age_limit
for year in range(age, max_age + 1):
    candles_needed = year  
    total_candles += candles_needed
    
# Remaining candles from other birthdays
    while candles_needed > 0:
        candles_needed -= one_box
        if candles_needed < 0:
            candles_needed = 0
        total_boxes += 1

#  Remaining candles after the 100th birthday
remaining_candles = total_candles - (max_age - age) 


print(f"Total boxes needed to buy: {total_boxes}")
print(f"Candles available after the 100th birthday: {remaining_candles}")
