#Not done 
import random
x = random.randint(-10,10)
if x>0 and x%2==0: 
    print("{} is even and positive".format(x))
elif x>0 and x%2==1:
    print("{} is odd and positive".format(x))
elif x<0 and x%2==0:
    print("{} is even and negative".format(x))
elif x<0 and x%2==1:
    print("{} is odd and negative".format(x))
else: 
    print("0 is even and neither positive or negative")
