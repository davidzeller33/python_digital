'''
1. Create a code that will ask for your marketing budget.
 Facebook campaign = 100ILS per day.
 Instagram campaign = 50ILS per day.
Ask him:
How long he wants the Facebook campaign will run.
How long he wants the Instagram campaign will run.
Then print to the screen the summary of the cost in ILS with tax (17%)
If it is more than his marketing budget, tell him how much to add, if not tell him "successfull
'''
num=int(input("Enter how much money do you have for marketing budget: "))
print("List of campaign prices(within Tax): \nFacebook: 100 ILS per day\nInstagram: 50 ILS per day")
a=int(input("How long do you wants the Facebook campaign wiil run?  "))
b=int(input("How long do you wants the Instagram campaign wiil run?  "))

cost=((((a*100)+(b*50))*1.17))



print("--------------\nCost of all campaign: " + str((a*100)+(b*50)) + " ILS\nTax(17%): " + str(((a*100)+(b*50))*0.17) + " ILS\nTotal cost of the campaign: " + str(cost) + " ILS\n------------")

budget= int(num-cost)

if budget==0 or budget>0:
    print("successful!!!")
else:
    print("Your need to add on your budget " + str(cost - num) + " ILS.")