#lists
'''
my_list=[12,25,555,2.2,"david"]
print(my_list)

print("my name is " + my_list[4])
print(my_list*2)
my_list1=list("1234567")
print(my_list1)

my_string=''.join(my_list1)
print(my_string)

#split faz uma lista tudo junto se nao tiver espaco
my_list2=my_string.split()
print(my_list2)
#splitlines faz uma lista juntando tudo em cada linha separado
my_string1="my name is\ndavid"
my_list3=my_string1.splitlines()
print(my_list3)
'''
### len conta quantidade de digitos(em strings) ou de casas(em listas)
my_list=[12,25,555,2.2,"david"]
print("the length of my list is " + str(len(my_list)))

## append acrescenta algo no final
my_list.append(124)
print(my_list)
print("the nem length of my list is " + str(len(my_list)))

## insert acrescenta algo no lugar que eu escolher
my_list.insert(1,24)
print(my_list)
print("the nem length of my list is " + str(len(my_list)))

## pop apaga algo no lugar que eu escolher(se nao escolher apaga o ultimo)
my_list.pop(5)
print(my_list)
print("the nem length of my list is " + str(len(my_list)))














