import random 
# funktion sort  
def count_occurrences(lst):
    c_ = {}
    for r in lst:         # for every element in the list
        if r in c_:
            c_[r] += 1
        else:
            c_[r] = 1
    
    return {k: v for k, v in sorted(c_.items())}

rand_num = [random.randint(1, 10) for _ in range(100)]
anser_cal = count_occurrences(rand_num)
 # sortera k  -v- par
for k, v in sorted(anser_cal.items()):
    print(k,"\t",v)


