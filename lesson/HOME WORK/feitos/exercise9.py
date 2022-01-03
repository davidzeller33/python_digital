'''
9. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

my_dictsample={0: 10, 1: 20}
print("old dict " + str(my_dictsample))
key_list=list(my_dictsample.keys())
val_list=list(my_dictsample.values())
newkey=((key_list[-1]+1))
newvalue=((val_list[-1]+10))
my_dictsample.update({newkey:newvalue})
print("new dict " + str(my_dictsample))