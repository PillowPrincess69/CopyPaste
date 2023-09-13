import random

BOY = 0
GIRL = 1
rooms = [[BOY, BOY], [BOY, GIRL], [GIRL, GIRL], [GIRL, GIRL]]

N = 100000
count = 0
test = 0
while test < N:
    i = random.randint(0, 3)
    if GIRL not in rooms[i]:
        continue
    if BOY in rooms[i]:
        count += 1
    test += 1
print(count/N) 
