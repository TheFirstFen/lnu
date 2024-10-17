import random
noun = "a car ", "a house ", "a soda ", "a meal ", "a computer "
verb = "will drive ", "will paint ", "will drink ", "will eat ", "will touch "
pronoun = "I ", "You ", "It ", "We ", "They "
x = 0
while x < 10:
    random_p = random.choice(pronoun)
    print(random_p, end='')

    random_v = random.choice(verb)
    print(random_v, end='')

    random_n = random.choice(noun)
    print(random_n, "\n")
    random_sentence = random_p + random_v + random_n
    x += 1
