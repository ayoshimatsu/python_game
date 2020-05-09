import datetime
import random

print(datetime.date.today())
print(datetime.datetime.now())

d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)

jan = random.choice(["Stone", "Scissors", "Paper"])
print(jan)

cnt = 0
while True:
    r = random.randint(1, 100)
    #print(r)
    cnt += 1
    if r == 77:
        break

print(str(cnt) + " times until correct value was gotten.")