def calculate_total(quantity, price):
  total=quantity*price
  if total>10000:
    total = total-(total*0.10)
  return total

eprice=0
loop = input("Do you want to run this program? Enter Yes or No ")
while loop =="Yes":
  quantity = int(input("Enter the quantity "))
  price = float(input("Enter the price "))
  totalcost=calculate_total(quantity,price)
  print("Quanitity purchased ", quantity, "Price per unit $", "{:.2f}",format(price), "Total is $", "{:.2f}".format(totalcost))
  eprice=eprice+totalcost
  loop = input("Do you want to run this program? Enter Yes or No ")
print("Total of all entries $", "{:.2f}".format(eprice))