'''
18. Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
'''

number1=int(input("Enter a number: "))
number2=int(input("Enter a number: "))
number3=int(input("Enter a number: "))
sum=number3+number2+number1
if number1==number3 and number2==number3:
    print(3*sum)
else:
    print(sum)