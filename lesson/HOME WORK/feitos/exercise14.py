'''
Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

my_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(my_list)
my_list.pop(0)
my_list.pop(4)
my_list.pop()
print(my_list)