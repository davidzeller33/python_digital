##"%.2F"  %


print("Now we calcute you marketing:\n\nPrices\n-----------\ntomatoes: 3 NIS\ncumcubers: 2 NIS\nCola: 5 NIS\nChicken: 20 NIS /KG\n--------------------")
Tomatoes=int(input("How many tomatoes do you want?: "))
Cumcubers=int(input("How many cumcubers do you want?: "))
Cola=int(input("How many colas do you want?: "))
Chicken=int(input("How many KG of chicken do you want?: "))
sumary=(Tomatoes*3)+(Cumcubers*2)+(Cola*5)+(Chicken*20)
print("\nYou have to pay without taxes " + str(sumary) + " NIS" )
print("You have to pay with taxes " + ("%.2F" % (1.17*sumary)) + " NIS" )