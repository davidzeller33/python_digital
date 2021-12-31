#dictionary
my_dict={"google.com":"5.4.2.2","facebook.com":"9.6.4.8"}
print(my_dict)
my_dict.update({"goo.co.il":"5.5.5.5"})
print(my_dict)
print(len(my_dict))

print(my_dict["google.com"])
print(my_dict.values())

my_dict["google.com"]="8.8.8.8"
print(my_dict)


print("google.com" in my_dict)
print("google.com" in my_dict.values())