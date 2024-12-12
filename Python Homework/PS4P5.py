last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))
adjusted_gross_income = gross_income - (dependents * 12000)
tax_rate = 0.20 if adjusted_gross_income > 50000 else 0.10
income_tax = adjusted_gross_income * tax_rate
if income_tax < 0:
    income_tax = 100
print(f"\nLast Name: {last_name}")
print(f"Gross Income: ${gross_income:.2f}")
print(f"Number of Dependents: {dependents}")
print(f"Adjusted Gross Income: ${adjusted_gross_income:.2f}")
print(f"Income Tax: ${income_tax:.2f}")