import random

pl_pos = 1
com_pos = 1

def banmen():
    print("-" * (pl_pos - 1) + "P" + "-" * (30 - pl_pos) + " :Goal")
    print("-" * (com_pos - 1) + "C" + "-" * (30 - com_pos) + " :Goal")

banmen()
print("Game start!!")

while True:
    input("Click Enter Key to advance your piece")
    pl_pos += random.randint(1, 6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("You win!")
        break

    input("Click Enter Key to advance CPU piece")
    com_pos += random.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("You lose!")
        break

