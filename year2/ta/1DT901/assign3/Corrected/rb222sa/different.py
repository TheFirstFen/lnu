from random import randint
lst = []

for i in range(100):
    num = randint(1, 200)
    lst.append(num)


def different(lst):
    st = set()
    newlst = []
    for i in lst:
        st.add(i)
    for i in st:
        newlst.append(i)
    return sorted(newlst)


print(different(lst))
