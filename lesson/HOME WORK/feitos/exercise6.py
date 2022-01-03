'''
6. Write a Python program to find whether a given number (accept from
the user) is even or odd, print out an appropriate message to the user
'''

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even number".format(num))
else:
    print("{0} is Odd number".format(num))