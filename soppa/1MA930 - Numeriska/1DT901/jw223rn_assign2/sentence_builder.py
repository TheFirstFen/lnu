from random import randint


def pronoun():
    ran = randint(1, 5)
    if ran == 1:
        return "It"
    elif ran == 2:
        return "They"
    elif ran == 3:
        return "You"
    elif ran == 4:
        return "I"
    else:
        return "We"


def verb():
    ran = randint(1, 5)
    if ran == 1:
        return "see"
    elif ran == 2:
        return "eat"
    elif ran == 3:
        return "pull"
    elif ran == 4:
        return "touch"
    else:
        return "feed"


def noun():
    ran = randint(1, 5)
    if ran == 1:
        return "tree"
    elif ran == 2:
        return "computer"
    elif ran == 3:
        return "house"
    elif ran == 4:
        return "car"
    else:
        return "dog"


for i in range(10):
    print(f"{pronoun()} will {verb()} a {noun()}")
