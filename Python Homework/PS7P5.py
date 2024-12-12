input_file = 'students.txt'

total_tuition = 0
student_count = 0

with open(input_file, 'r') as file:
    while True:
        last_name = file.readline().strip()
        if not last_name:
            break
        district_code = file.readline().strip()
        credits_taken = int(file.readline().strip())

        if district_code == 'I':
            cost_per_credit = 250.00
        elif district_code == 'O':
            cost_per_credit = 500.00
        else:
            continue

        tuition_owed = credits_taken * cost_per_credit
        print(f"{last_name} | Credits Taken: {credits_taken} | Tuition Owed: ${tuition_owed:.2f}")

        total_tuition += tuition_owed
        student_count += 1

print(f"\nTotal Tuition Owed: ${total_tuition:.2f}")
print(f"Number of Students: {student_count}")