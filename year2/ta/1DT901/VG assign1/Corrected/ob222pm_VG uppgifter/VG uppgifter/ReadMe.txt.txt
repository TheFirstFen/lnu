1. Sum of three:
To isolate the "first" number in the 3 digit integer i used integer division. Ex for the number n would be n//100. 
This removed the last 2 numbers. Ex 542 -> 5

For the second number i first used modulus on the 3 digit number, specifically n//100 to get rid of the first number instead of the last 2. Then to get rid of the last one i used integer division but used //10 intead of //100 since the first number already was removed. n%100//10.

For the last one i just used integer divion like the first number but did n//10 to only get the third number. 



2. Change
First i created inputs for both the price and the payment. Then to create the change i just did Change = payment - price.

In my solution i used my variable rest which was: rest = change%payment.
I used this variable to find out how many times the change would fit into firstly the 1000kr bill, then the 500kr bill and so on.

To find out how many times the 1000kr bill could go into the rest variable i used: b_1000 = rest // 1000. Then used the same formula for all the variables. Ex b_500 = rest // 500 etc, b_200 = rest // 200 etc.

Then i had to figure out how much money was left over after the modulus had been calculated so i could then use that to calculte how many 500kr bills could fit into the left over money. And then the same method for 200kr bills and so on. 

To do this i made the formula for rest after the 1000kr bills to be: rest = rest%1000. This then gave me the amount of money i would see how many times a 500kr bill could fit. 

Then i did the same thing for the rest of the solution. For the 500kr bill i then did: rest = rest%500. For the 200kr bill i then did: rest = rest%200 and then did this all the way down to the 1kr coins.



3. Tax
Firstly i made an input for the income you wanted to figure out the tax for. In my solution i used two variables, rest1 and rest2. I used rest1 for if the income was between 38000kr and 50000kr. I used it to differentiate the tax for under and over 38000kr. So rest1 would represent the amount of money that the income had overgone 38000kr (up to max 12000kr over to surpass 50000kr) Ex if the income was 45000kr then rest1 would be 7000kr. I then added the extra tax onto this.

I used rest2 in basically the same way. rest2 is the amount of money that surpasses 50000kr. Ex if income = 56000kr then rest2 = 6000kr. I then added the extra tax onto this amount aswell. 
If the income was over 50000 i also removed rest1 and replaced it with 12000 since this was the max amount rest1 could be , since if the income was over 50000 then rest1 would be at 12000kr anyway.


4. Square color

Not done.
