#while loops

#loops so acontece se a condicao eh valida
'''
num=int(input("enter a number: "))
while(num!=7):
    print(num*10)
    num=num-1

'''

from time import sleep
while(True):
    choice=int(input("We Have Some activities to do: \n1.Insert Number and ** it by 3 \n"
                 "2.Insert 4 IP in a list and print it \n"
                 "3.Insert 4 entries to a DNS_Dictionary and print it \n"
                 "4.Check if a string is Polindrom \n"
                 "Choose 1-4 to which activite do you want to do now: "))
    if choice==1:
        number=int(input("Insert a number: "))
        print("Your number ** 3 is : " + str(number**3))
    elif choice==2:
        IP_list=[]
        IP_list.append(input("Enter new IP: "))
        IP_list.append(input("Enter new IP: "))
        IP_list.append(input("Enter new IP: "))
        IP_list.append(input("Enter new IP: "))
        print("The new IP list is: \n----------\n" + str(IP_list))
    elif choice==3:
        DNS_Dictionary={}
        DNS_Dictionary.update({input("Enter a URL: "): (input("Enter IP: "))})
        DNS_Dictionary.update({input("Enter a URL: "): (input("Enter IP: "))})
        DNS_Dictionary.update({input("Enter a URL: "): (input("Enter IP: "))})
        DNS_Dictionary.update({input("Enter a URL: "): (input("Enter IP: "))})
        print("The new DNS list is: \n----------\n" + str(DNS_Dictionary))
    elif choice==4:
        string=input("Write a word to check if is Polindrom: ")
        if string==(string[::-1]):
            print("This is a word polindrom!")
        else:
            print("This isn't a Polindrom!")
    else:
        print("You need to choose a number between 1-4")
    exit=(input("Do you want to exit? y/n\n"))
    if(exit=="y" or exit=="yes"):
        break
    else:
        print("Welcome back!!!\n")



print("thank you, bye bye")




