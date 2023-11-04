import random

lst_ints = [random.randint(0, 200) for i in range(100)]  # random list


def different(lst):  # Function used to create the set and sort it
    st = set()
    for i in lst:
        st.add(i)
    return sorted(st)


set_different = different(lst_ints)
print(set_different, len(set_different))
