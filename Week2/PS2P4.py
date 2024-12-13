make = input()
model = input()
msrp = float(input())
discount_percent = float(input())

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print("Make:", make)
print("Model:", model)
print("MSRP: $", round(msrp, 2))
print("Discount Percent:", round(discount_percent * 100, 2), "%")
print("Amount off MSRP: $", round(amount_off, 2))
print("Discounted Price: $", round(discounted_price, 2))