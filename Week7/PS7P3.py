f = open("salaries.txt", "r")
lastname = f.readline()
totalbonus=0
while lastname != "":
  salary = float(f.readline())
  if salary >= 100000:
    bonusrate = 0.20
  elif salary >= 50000:
    bonusrate = 0.15
  else:
    bonusrate = 0.10
  bonus = salary * bonusrate
  print(f'{lastname} salary is {salary:.2f} bonus is {bonus:.2f} bonus rate is {bonusrate:.2f}')
  totalbonus = totalbonus + bonus
  lastname = f.readline()
print("Total bonus paid is", totalbonus)