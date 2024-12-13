def get_unit_price(item):
  if item == 'A':
      return 10.00
  else:  
      return 20.00
def main():
      item = input("Enter the item (A or any other for B): ").strip().upper()
      quantity = int(input("Enter the quantity: "))
      if quantity < 0:
          print("Quantity must be a non-negative integer.")
          return
      unit_price = get_unit_price(item)
      extended_price = quantity * unit_price
      print(f"\nItem: {item}")
      print(f"Unit Price: ${unit_price:.2f}")
      print(f"Extended Price: ${extended_price:.2f}")
