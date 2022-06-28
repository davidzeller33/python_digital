"falta colocar o premio e somar os premios das jogadas"
from random import randint as rnd
from time import sleep

RANGE =  37
DRAWS = 6
print("Welcome to our Lotto: \nEach game cost 3 ILS\n")
num=int(input("Enter how much money do you want to play: "))
turns=int(num//3)
print("\nYou have: " + str(num//3) + " turns\nYour change: " +str(num%3) + " ILS")
sleep(3)

for i in range(turns):
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
                        print("Its not a number between 1-37")
                    elif number in draws:
                        print("You already choose this number")
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

    print("Playing... ")
    sleep(5)
    print(f"Numbers lotto: {rands}")
    print(f"Your Numbers: {draws}")
    print(f"You hit {hits} numbers")
    print(f"The hitlist: {hitlist}")

