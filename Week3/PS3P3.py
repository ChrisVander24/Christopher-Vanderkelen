meal_total = float(input())
tip_percentages = [0.15, 0.18, 0.20]
tip_amount = meal_total * tip
total_with_tip = meal_total + tip_amount
print(f"With {int(tip * 100)}% Tip:")
print(f"Total:                  {meal_total:.2f}")
print(f"Tip:                       {tip_amount:.2f}")
print(f"Total with Tip    {total_with_tip:.2f}\n")