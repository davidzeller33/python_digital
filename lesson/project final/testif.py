hits=int(input("HITS:"))
price=0
if hits == 6:
    price = price + 1000
elif hits == 5:
    price = price + 100
elif hits == 4:
    price = price + 40
elif hits == 3:
    price = price + 20
else:
    price = price

print(price)