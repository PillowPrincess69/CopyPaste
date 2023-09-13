import random

BOY = 0
GIRL = 1
rooms = [[BOY, BOY], [BOY, GIRL], [GIRL, GIRL], [GIRL, GIRL]]

N = 100000
count = 0
test = 0

BUSY_PROB = 0.1
while test < N:
    i = random.randint(0, 3)
    if GIRL not in rooms[i]:
        continue
    if BOY in rooms[i]:
        busy = random.uniform(0, 1)
        if busy <= BUSY_PROB:
            test += 1
            count += 1
    else:
        busy_total = 0
        busy1 = random.uniform(0, 1)
        busy2 = random.uniform(0, 1)
        if busy1 <= BUSY_PROB or busy2 <= BUSY_PROB:
            test += 1
print(count/N)
    
