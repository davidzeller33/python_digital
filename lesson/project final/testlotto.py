from random import randint as rnd

RANGE =  37
DRAWS = 6

def randomise():
    rands = []
    for i in range(DRAWS):
            number = rnd(1,RANGE)
            while number in rands:
                number = rnd(1,RANGE)
            rands.append(number)
    return rands

def drawing():
    draws = []
    for i in range(DRAWS):
        while True:
            try:
                number = int(input(f"Please give me a number from 1 to {RANGE}:"))
                if number < 1 or number > RANGE:
                    print("Give another number")
                elif number in draws:
                    print("number new please")
                else:
                    break
            except:
                print("Give an integer number !!")
        draws.append(number)
    return draws

rands = randomise()
rands.sort()
draws = drawing()
draws.sort()

hits = 0
hitlist = []

for draw in draws:
    if draw in rands:
        hits+=1
        hitlist.append(draw)

print(f"Random list: {rands}")
print(f"Drawing list: {draws}")
print(f"You hit {hits} times")
print(f"The hitlist: {hitlist}")

