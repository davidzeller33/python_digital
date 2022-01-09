from time import sleep
IP_list = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"]
dns_list={"google.com":"1.1.1.1","facebook.com":"2.2.2.2","ynet.com":"3.3.3.3","yahoo.com":"4.4.4.4"}
def menu():
    while (True):
        choice=input('''
        Menu:
        a. IP System
        b. DNS System
        A or B? 
        ''')
        if choice=="a":
            choice2 = input('''
                        Menu IP System:
                        1 - Search for IP address from a list
                        2 - add IP to a list
                        3 - delete IP address from a list
                        4 - Print all te IPs to the screen
                        ----------------------
                        What do you want to do? 
                        ''')
            if choice2=="1":
                ip1()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice2=="2":
                ip2()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice2=="3":
                ip3()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice2=="4":
                ip4()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            else:
                print("please enter 1-4")
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
        elif choice=="b":
            choice3 = input('''
                    Menu DNS System:
                    1 - Search for URL in a dictionary
                    2 - add URL + IP to a dictionary
                    3 - delete URL from a dictionary
                    4 - Update the IP address of a specific URL
                    5 - Print all te URL:IP to the screen
                    ----------------------
                    What do you want to do? 
                    ''')
            if choice3=="1":
                dns1()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice3=="2":
                dns2()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice3=="3":
                dns3()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice3=="4":
                dns4()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            elif choice3=="5":
                dns5()
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
            else:
                print("please enter 1-5")
                exit = input("\nDo you want to exit? yes/no : ")
                if exit == "y" or exit == "yes":
                    print("Bye bye!!!")
                    break
        else:
            print("Enter a or b!!!")
            exit=input("\nDo you want to exit? yes/no : ")
            if exit=="y" or exit=="yes":
                print("Bye bye!!!")
                break



def ip1():
    search=input("Enter a IP: ")
    if search in IP_list:
        print("This IP is in the list!!!")
    else:
        print("This IP isn't in the list!!!")
def ip2():
    ipadd=input("Enter a IP: ")
    IP_list.append(ipadd)
    print("The ip was succesful added in the list")
    print(IP_list)
def ip3():
    print(IP_list)
    ipdel=input("Enter a ip do you want to delete: ")
    IP_list.remove(ipdel)
    sleep(2)
    print("Successuful delete\n" + str(IP_list))
def ip4():
    print(IP_list)
def dns1():
    search = input("Enter a URL: ")
    if search in dns_list:
        print("This URL is in the list!!!")
    else:
        print("This URL isn't in the list!!!")
def dns2():
    urladd = input("Enter a URL: ")
    ipadd = input("Enter a IP: ")
    dns_list[urladd]=ipadd
    sleep(2)
    print("Was succesful added in the list")
    print(dns_list)
def dns3():
    key=input("Enter a URL to delete: ")
    if key in dns_list:
        del dns_list[key]
        sleep(2)
        print("Succesful delete")
    else:
        sleep(2)
        print("This URL dont exist in your DNS list")
def dns4():
    urladd = input("Enter a URL do you want to change a IP: ")
    ipadd = input("Enter a new IP: ")
    dns_list[urladd] = ipadd
    print("Succesful update \n" + str(dns_list))
def dns5():
    print(dns_list)














def ip():
    choice = input('''
            Menu IP System:
            1 - Search for IP address from a list
            2 - add IP to a list
            3 - delete IP address from a list
            4 - Print all te IPs to the screen
            ----------------------
            What do you want to do? 
            ''')
    return choice

def dns():
    choice = input('''
        Menu DNS System:
        1 - Search for URL in a dictionary
        2 - add URL + IP to a dictionary
        3 - delete URL from a dictionary
        4 - Update the IP address of a specific URL
        5 - Print all te URL:IP to the screen
        ----------------------
        What do you want to do? 
        ''')
    return choice