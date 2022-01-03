'''
 Write a Python program to accept a filename from the user and print
the extension of that.
Sample filename : abc.java
Output : java
'''

n=input("Please, insert a file name: ")
print("Your file type is: " + n.split(".",1)[1])