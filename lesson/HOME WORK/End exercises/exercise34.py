'''
34. Write a Python program to sum of two given integers. However, if the sum
is between 15 to 20 it will return 20.
'''

number1=int(input("Enter a number: "))
number2=int(input("Enter a number: "))
sum=number2+number1
if sum<20 and sum>15:
    print(20)
else:
    print(sum)