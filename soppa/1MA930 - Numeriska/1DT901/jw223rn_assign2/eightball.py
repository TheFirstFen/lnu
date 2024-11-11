from random import randint

s = input("Ask the magic 8-ball your question: ")


def answer():
    ans = ["Ask again later", "As I see it, yes", "Concentrate and ask again",
           "Better not tell you know", "Very doubtful"]
    r = randint(0, 4)
    return ans[r]


while s != "stop":
    print(f"The magic 8-ball says: {answer()}")
    s = input("Ask the magic 8-ball your question: ")
