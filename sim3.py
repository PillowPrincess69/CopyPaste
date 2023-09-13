import random

BOY = 0
GIRL = 1
BUSY_GIRL = 1

N = 100000
count = 0
test = 0

while test < N:
    people = [BOY, GIRL, GIRL, GIRL, GIRL, BUSY_GIRL]
    random.shuffle(people)
    rooms = [[BOY, BOY], [people[0], people[1]], [people[2], people[3]], [people[4], people[5]]]
    i = random.randint(0, 3)
    if BUSY_GIRL not in rooms[i]:
        continue
    test += 1
    if BOY in rooms[i]:
        count += 1
print(count/N) 
