total_gross_pay = 0
employee_count = 0
response = input("Do you want to continue? (Yes/No): ").strip().lower()

while response == 'yes':
    last_name = input("Enter employee's last name: ").strip()
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter rate of pay: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * rate_of_pay) + (overtime_hours * rate_of_pay * 1.5)
    else:
        gross_pay = hours_worked * rate_of_pay

    print(f"Employee Last Name: {last_name}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    total_gross_pay += gross_pay
    employee_count += 1
    response = input("Do you want to continue? (Yes/No): ").strip().lower()

print(f"\nTotal Gross Pay: ${total_gross_pay:.2f}")
print(f"Number of Employees: {employee_count}")

if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print(f"Average Pay: ${average_pay:.2f}")
else:
    print("No employees were processed.")