######math: *   \ +  \ -  \
# **(elevado) \
# /(dividido)
#  //(dividi para numeros inteiros)
# % (traz a sobra da divisao de numeros inteiros)


num=int(input("enter a number with 4 digit: "))


print("Alafim=" + str(num//1000) + "\nMeot=" + str((num%1000)//100) + "\nAssarot=" + str((num%100)//10) + "\nAhadot=" + str(num%10))

