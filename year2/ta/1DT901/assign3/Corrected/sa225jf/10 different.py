import random as rnd 

def different(lst):
    lst = set()                     # place till unquie numbers
    for i in range(100):            #loop fram 0 to 99 and stop when arrive 100
        random_num = rnd.randint(1, 200 + 1)        #random choice many of numbers randomly  and different betwwen 1 to 200 ""
        lst.add(random_num)                    #add all numbers in random_num to lst "set"
    return list(lst)

ls_ = list
print("Different integers:", different(ls_))
