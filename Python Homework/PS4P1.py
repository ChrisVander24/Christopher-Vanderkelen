Quantity = int(input("Enter the quantity of the item: "))
if Quantity >= 1000:
  UnitPrice = 3.00
else:
  UnitPrice = 5.00
ExtendedPrice = Quantity*UnitPrice
Tax = ExtendedPrice * 0.07
Total = ExtendedPrice + Tax
print(f"\nQuantity: {Quantity}")
print(f"UnitPrice: ${UnitPrice:.2f}")
print(f"ExtendedPrice: ${ExtendedPrice:.2f}")
print(f"Tax: ${Tax:.2f}")
print(f"Total: ${Total:.2f}")