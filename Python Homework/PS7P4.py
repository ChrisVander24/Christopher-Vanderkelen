with open("items.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        item = lines[i]  
        quantity = int(lines[i + 1])  
        price = float(lines[i + 2]) 
        extended_price = quantity * price
        print(f"Item: {item}, Quantity: {quantity}, Price:     {price}, Extended Price: {extended_price}")
    total_extended_price = 0
    total_extended_price += extended_price
    average_order = total_extended_price / quantity if     quantity > 0 else 0

    print("\nSummary:")
    print(f"Total Extended Price: {total_extended_price}")
    print(f"Number of Orders: {quantity}")
    print(f"Average Order: {average_order}")