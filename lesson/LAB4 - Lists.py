my_list=["David",28,"david@",'053803']
print("my name is " + my_list[0] + "\nmy age is " + str(my_list[1]) + "\nmy mail is " + my_list[2] + "\nmy number is " + my_list[3])

my_list2=["172.16.16.14","10.10.3.69"]
print(my_list2)
'''
my_list3=['10.10.1.228', '172.16.160.148', '10.10.10.158']
my_list4=my_list2+my_list3
print(my_list4)
'''
my_list2.append("10.10.1.228")
my_list2.append("172.16.160.148")
my_list2.append("10.10.10.158")

#(172.16.160.148)(10.10.10.158)
my_list2.pop(2)
print(my_list2)
print("the nem length of my list is " + str(len(my_list2)))