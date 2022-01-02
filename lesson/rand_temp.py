from random import randint
from time import sleep

print("Getting randomdly numbers: ")
sleep(3)
num1=randint(1,37)
num2=randint(1,37)

print("1st number: " + str(num1) + "\n2nd number: " + str(num2))

if num1==num2:
    print("\nYou won 100$!!! \n")
else:
    print("\nYou won 0$!!!\n")

print("Bye Bye")

