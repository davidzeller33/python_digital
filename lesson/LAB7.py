from random import randint
from time import sleep
print("Welcome to our cube game: \nEach turn cost 3 ILS\n")
num=int(input("Enter how much money do you want to play: "))
turns=int(num//3)
print("\nYou have: " + str(num//3) + " turns\nYour change: " +str(num%3) + " ILS")
sleep(3)
price=0
for i in range(turns):
    print("---------------------\nRound number: " + str(i+1) + " :\n")

    print("Playing... ")
    sleep(3)
    num1=randint(1,6)
    num2=randint(1,6)

    print("1st cube: " + str(num1) + "\n2nd cube: " + str(num2))

    if num1==num2 and num1==3:
        price=price+1000
    elif num1==num2:
        price=price+100
    elif num2==2:
        price=price+40
    elif num1==1:
        price=price+20
    else:
        price=price

print("\nYou won: " + str(price) + " ILS")

print("\nThank you to play with us\nBye Bye")