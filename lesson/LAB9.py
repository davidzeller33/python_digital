from random import randint
from time import sleep

def dogs():
    name=input("\nWhat is your dog name? ")
    age=int(input("What is his age? "))
    print("\nName dog: " + str(name) + "\nAge: " + str(age*7) + "\n")
def friends(x,y,z):
    list=[]
    list.append(x)
    list.append(y)
    list.append(z)
    friend = input("Which friend do you wanna know if is in the list? ")
    if friend in list:
        print("He is in the list ")
    else:
        print("he isnt in the list ")
def azzeret(x):
    sum=1
    for i in range(1, x+1):
        sum=sum*i
    print(sum)

def menu():
    while(True):
        print("Menu: \n1-Dogs details\n2-friends list\n3-N azzeret\n-----")
        choice=input("Choose a activite: ")
        if(choice =="1"):
            print(dogs())
        elif(choice=="2"):
            friends("david", "yoel", "jaco")
        elif(choice=="3"):
            number = int(input("Chose a number: "))
            azzeret(number)
        else:
            print("You need to enter only 1-3!!!")
            continue
        sleep(2)
        exit = input("Do you want to exit? yes/no\n")
        if exit == "y" or exit == "yes":
            print("Thank you and bye bye!!!")
            break
        else:
            print("Welcome Back!!!\n")

menu()
