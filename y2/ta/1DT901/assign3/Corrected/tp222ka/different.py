import random


def different(lst):
    # set for storeing
    new_lst = set()
    for num in lst:
        new_lst.add(num)
    # convert to list and use sorted
    new_lst = sorted(list(new_lst))
    return new_lst


def main():
    rnd = []
    # 100 random num
    for i in range(100):
        rnd.append(random.randint(1, 200))
    # call different
    diff = different(rnd)
    print("Different integers:")
    print(diff)


# run the program
main()
