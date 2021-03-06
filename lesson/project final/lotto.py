'''
Create a Lotto game:
 Puts in a list of 6 numbers, between 1-37, as in a real lottery.
 The numbers must not be repeated.
 Each game (row) in Lotto costs 3 ILS, Insert how much money do you have?
 Random 6 numbers – the winner's number.
 Then play few rounds (rows) as your budget can handle.
 On each round, random 6 numbers , between 1-37, and check if you won.
 In the end sum the entire prize from all rounds.

If you guess:
6 numbers = won 1M ILS
5 numbers = won 5000 ILS
4 numbers = won 100 ILS
3 numbers = won 10 ILS
'''

from random import randint
from time import sleep

print("Welcome to our Lotto: \nEach game cost 3 ILS\n")
num=int(input("Enter how much money do you want to play: "))
turns=int(num//3)
print("\nYou have: " + str(num//3) + " turns\nYour change: " +str(num%3) + " ILS")
sleep(3)
price=0
for i in range(turns):
    print("---------------------\nRound number: " + str(i+1) + " :\n")
    bet1=int("Enter six numbers between 1-37:\nFirst Number: ")
    bet2 = int("Second Number: ")
    bet3 = int("Third Number: ")
    bet4 = int("Four Number: ")
    bet5 = int("Five Number: ")
    bet6 = int("Six Number: ")
    betlist=[]
    betlist.append(bet1,bet2,bet3,bet4,bet5,bet6)
        def checkIfDuplicates_3(listOfElems):
            ''' Check if given list contains any duplicates '''
            for elem in listOfElems:
                if listOfElems.count(elem) > 1:
                    return True
            return False

        result = checkIfDuplicates_3(betlist)
        if result:
            print('Yes, list contains duplicates')
        else:
            print('No duplicates found in list')
    print("Playing... ")
    sleep(3)
    num1=randint(1,37)

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