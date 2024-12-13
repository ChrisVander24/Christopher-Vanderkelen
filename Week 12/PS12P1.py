howmany = int(input("How many numbers do you want to enter? "))
list=[]
#1
for i in range(0,howmany,1):
  num=int(input("Enter a number "))
  list.append(num)
print(list)
#2
list.insert(1,99)
print(list)
#3
if 99 in list:
  where= list.index(99)
  list[where] = 100
print(list)
#4
list2={500,600,700,800,900}
list.extend(list2)
print(list)
#5
list.remove(800)
print(list)
#6
list.pop(2)
print(list)
#7
grades = ["A", "B", "C", "A", "A", "C"]
#8
a_grades =grades.count("A")
print("There are " , a_grades, "A's")
#9
if "B" in grades:
  print("There is a B in the list at position" , grades.index("B"))
#10
if "F" in grades:
  print("There is a F in the list at position" , grades.index("F"))
else:
  print("There is no F in the list")
#11
list2.clear()
print(list2)
#12
del list2
#
#13
players =["Rizzo" , "Davis", "Baez" , "Happ", "Bryan"]
players.sort()
print(players)
#14
players2=players.copy()
print(players2)
players2.reverse()
print(players2)
