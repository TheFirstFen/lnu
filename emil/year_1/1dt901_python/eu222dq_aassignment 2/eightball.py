import random


lst = ["Ask again later", "As I see it, yes", "Concentrate and ask again",
       "Better not tell you now", "Very doubtful"]

while True:
    quest = str(input("Ask the magic 8-ball your question: "))
    if "Stop" == quest:
        break
    else:
        print("The magic 8-ball says: ", random.choice(lst))
