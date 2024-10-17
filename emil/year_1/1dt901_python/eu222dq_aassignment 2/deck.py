import random
card_values = ["2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ",
               "jack ", "queen ", "king ", "ace "]
card_colurs = ["of harts ", "of spades ", "of diamonds ", "of clubs "]

deck = []

for value in card_values:
    for colur in card_colurs:
        tmp = value + colur
        deck.append(tmp)

n1 = random.choice(deck)
n2 = random.choice(deck)
n3 = random.choice(deck)
n4 = random.choice(deck)
n5 = random.choice(deck)
print(f"{n1} \n{n2} \n{n3} \n{n4} \n{n5}")
