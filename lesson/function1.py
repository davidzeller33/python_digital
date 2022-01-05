
'''
####
# function que nao recebe e nao devolve
def market():
    print("Now we calcute you marketing:\n\nPrices\n-----------\ntomatoes: 3 NIS\ncumcubers: 2 NIS\nCola: 5 NIS\nChicken: 20 NIS /KG\n--------------------")
    Tomatoes=int(input("How many tomatoes do you want?: "))
    Cumcubers=int(input("How many cumcubers do you want?: "))
    Cola=int(input("How many colas do you want?: "))
    Chicken=int(input("How many KG of chicken do you want?: "))
    sumary=(Tomatoes*3)+(Cumcubers*2)+(Cola*5)+(Chicken*20)
    print("\nYou have to pay without taxes " + str(sumary) + " NIS" )
    print("You have to pay with taxes " + ("%.2F" % (1.17*sumary)) + " NIS" )


market()
##################
# function que recebe e nao devolve
def calculating(x,y):
    print("your fisrt number is: " + str(x) + "\nyour second number is: " + str(y))
    print("Your nem number is: " + str(x+y))

calculating(2,5)
#####
# function que nao recebe e devolve
def calculating():
    num1=input("Enter a number: ")
    num2=input("Enter a number: ")
    print("your fisrt number is: " + str(num1) + "\nyour second number is: " + str(num2))
    sum=num1 + num2
    print("Your nem number is: " + str(sum))
    return sum

a=int(calculating()) + 35
print(a)
'''
# function que recebe e devolve
def calculating(x,y):

    print("your fisrt number is: " + str(x) + "\nyour second number is: " + str(y))
    sum=int(x) + int(y)
    print("Your nem number is: " + str(sum))
    return sum
num1=input("Enter a number: ")
num2=input("Enter a number: ")
a=int(calculating(num1,num2)) + 35
print(a)
