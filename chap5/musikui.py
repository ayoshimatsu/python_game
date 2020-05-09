import random
import datetime

ALP = ["A", "B", "C", "D", "E", "F", "G"]
r = random.choice(ALP)
alp = ""

for i in ALP:
    if i != r:
        alp = alp + i

print(alp)
st = datetime.datetime.now()
ans = input("What alphabet is not written? : ")
if ans == r:
    print("Correct!")
    et = datetime.datetime.now()
    print("{} Seconds elapsed.".format((et - st).seconds))
else:
    print("Wrong!")