'''
exercise 1
print("Net4U is the best place \n...in the world")
##############
exercise2
from datetime import datetime
now = datetime.datetime.now()
print("Current date and time : \n", now)

##########exercise 3
name=input("Tell me your first and last name: ")
b=' '.join(name[::-1])
print(b)

####exercise 4
 Write a Python program to accept a filename from the user and print
the extension of that.
Sample filename : abc.java
Output : java

####exercise 5
n=int(input("chose a number: "))
print(n + (n+n) + (n+n+n))

####exercise 6
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even number".format(num))
else:
    print("{0} is Odd number".format(num))


####exercise 7
####exercise 8
####exercise 9
my_dictsample={0: 10, 1: 20}
print("old dict " + str(my_dictsample))
key_list=list(my_dictsample.keys())
val_list=list(my_dictsample.values())
newkey=((key_list[-1]+1))
newvalue=((val_list[-1]+10))
my_dictsample.update({newkey:newvalue})
print("new dict " + str(my_dictsample))
'''
####exercise 10

