from random import *
def craps():
    outcome = [2,3,7,11,12]
    house = [2,3,12]
    player = [7,11]
    x = 0
    y = 0
    while (x + y) not in outcome:
        x = randint(1,6)
        y = randint(1,6)
        roll = x + y
        if roll in house:
            return 0
        if roll in player:
            return 1
def manyCraps(n):
    total = 0
    for i in range(n):
        total += craps()
    return total/n
