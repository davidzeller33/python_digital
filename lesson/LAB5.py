my_dict={"omer":10000,"dvir":8000,"shasha":12000,"olga":7000,"shir":22000}

print("The summary is : " + str((my_dict["omer"])+(my_dict["shir"])))

my_dict.update({"david":str((my_dict["omer"])+(my_dict["shir"]))})
print(my_dict)

print(len(my_dict))

print("idan" in my_dict)



