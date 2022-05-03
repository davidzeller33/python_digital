from random import randint
from time import sleep
'''
bet1 = int(input("Enter your first number between 1 and 37: "))
bet2 = int(input("Enter your second number between 1 and 37: "))
bet3 = int(input("Enter your third number between 1 and 37: "))
bet4 = int(input("Enter your four number between 1 and 37: "))
bet5 = int(input("Enter your five number between 1 and 37: "))
bet6 = int(input("Enter your six number between 1 and 37: "))
num1=random.randint(1,37)
'''
'''
from random import randint
from time import sleep
import random

lotterynumbers = []
for i in range (0,6):
    number = random.randint(1,37)
    while number in lotterynumbers:
        number = random.randint(1,37)
    lotterynumbers.append(number)
lotterynumbers.sort()
print(lotterynumbers)
'''

listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
result = checkifdup
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')