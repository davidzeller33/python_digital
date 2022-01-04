#while loops

#loops so acontece se a condicao eh valida
'''
num=int(input("enter a number: "))
while(num!=7):
    print(num*10)
    num=num-1

'''

while(True):
    name=input("what your name: ")
    if(name=="david"):
        print("Hello david")
        break
    elif(name=="idan"):
        continue
    else:
        print("where is david? ")

    number=int(input("number: "))
    print(4*number)
print("bye bye")
