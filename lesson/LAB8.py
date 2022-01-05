from time import sleep
from random import randint

while(True):
    choice=int(input("We Have Some activities to do: \n1.printing 100 numbers \n"
                     "2.Check if is FIBO \n"
                     "3.Randint numbers until we get 12 or we count 10 times \n"
                     "Choose 1-3 to which activite do you want to do now: "))
    if choice == 1:
        for i in range(1,101):

            print(i)

    elif choice == 2:
        list=[]
        for i in range(7):
            list.append(int(input("Enter a number: ")))

        boolean="True"

        for i in range(2,len(list)):
            if list[i]==list[i-1] + list[i-2]:
                continue
            else:
                boolean="False"
                break
        if boolean=="True":
            print("Its a FIBO\n")
        else:
            print("its isn`t a FIBO")
    elif choice==3:
        counter = 0
        num1 = randint(1, 12)
        while(num1!=12 and counter<11):
            num1 = randint(1, 12)
            print("\nCounter: " + str(counter) + "\nNumber: " + str(num1))
            counter=counter+1
    else:
        print("Enter 1-3 only!!!")
        continue
    exit = (input("\nDo you want to exit? y/n\n"))
    if (exit == "y" or exit == "yes"):
        print("\nThank you, bye bye")
        break
    else:
        print("\nWelcome back!!!\n")

