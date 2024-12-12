name = input("Enter the name of the appliance: ")
cost = float(input("Enter the cost of the appliance: "))
warranty_cost = cost * 0.10 if cost > 1000 else cost * 0.05
total_cost = cost + warranty_cost
print(f"\nAppliance Name: {name}")
print(f"Cost of Appliance: ${cost:.2f}")
print(f"Cost of Warranty: ${warranty_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")