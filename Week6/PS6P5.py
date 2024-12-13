total_discount = 0
response = input("Do you want to continue? (Yes/No): ").strip().lower()

while response == 'yes':
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price of item: "))

    extended_price = quantity * price
    discount_percent = 0.25 if extended_price > 10000 else 0.10
    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")

    total_discount += discount_amount

    response = input("Do you want to continue? (Yes/No): ").strip().lower()

print(f"\nTotal Discount Sum: ${total_discount:.2f}")