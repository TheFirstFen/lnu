from random import shuffle


def add_colour(x):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace"]
    cards = [n + x for n in cards]
    return cards


heart_cards = add_colour(" of Hearts")
club_cards = add_colour(" of Clubs")
spade_cards = add_colour(" of Spades")
diamond_cards = add_colour(" of Diamonds")

deck = heart_cards + club_cards + spade_cards + diamond_cards

shuffle(deck)

print("My hand:")
print(deck[0])
print(deck[1])
print(deck[2])
print(deck[3])
print(deck[4])
