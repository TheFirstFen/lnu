import random as rd


# Returns sorted list of unique elements in lst
def different(lst):
    n_lst = []
    st = set()
    for num in lst:
        st.add(num)
    for num in st:
        n_lst.append(num)
    n_lst.sort()
    return n_lst


lst = []
# Creates 100 random numbers between 1 and 200 and appends to list
for n in range(100):
    n = rd.randint(1, 200)
    lst.append(n)

print("Different integers:")
print(different(lst))
