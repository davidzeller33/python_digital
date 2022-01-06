#r- read
#w- write
#a- append, acrescentar
#r+- read and write
#a+ append, acrescentar + read

'''
filename= "C:/Users/david/Desktop/test.txt"
file = open(filename,"r+")
print(file.read())
file.write("hello\nbye")
print(file.read())
file.close()


filename= "C:/Users/david/Desktop/test.txt"
file = open(filename,"r")
new_list=[]
new_list=file.read().splitlines()
print(new_list)
file.close()
for i in new_list:
    print(i)
#read only specific line

filename= "C:/Users/david/Desktop/test.txt"
file = open(filename,"r")
print(file.readlines(3))
'''

#create file
f=open("C:/Users/david/Desktop/test2.txt", "x")
f.close()













