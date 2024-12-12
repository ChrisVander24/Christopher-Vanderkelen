print (Enter the item to be purchased)
item = input()
print ("Enter the quantity")
quantity = int(input())
if item == "10"or item=="55":
  unitprice = 1.00
else:
  if item =="99":
    unitprice = 2.00
  else:
  if item=="80"or item=="70":
    unitprice = 3.00
  else:
    unitprice = 5.00
price = quantity * unitprice
print ("The item to buy is", item,
      "\n The unit price is: $","{:.2f}".format(unitprice),
      "\n The price is: