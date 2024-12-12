print ("Enter the amount of the CD")
amount = float(input())
print ("Enter the year")
year = int(input())
if amount>100000 and year == 5:
  interest = 0.06
else:
  if amount >= 50000 and year == 10:
    interest = 0.05
  else:
    if amount >= 50000 and year == 5:
      interest = 0.04
    else:
      interest = 0.02
firstint = amount * interest
print ("Amount of CD is $ ", amount,
      "\n The interesst rate is: $"."{:.2F}".format(interest).