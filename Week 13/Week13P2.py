class Student:
  def __init__(self, first, last, district, credits):
    self.first=first
    self.last=last
    self.dc=district
    self.credits=credits

  def tuition(self):
    if self.dc == "I":
      owed=self.credits*250
    else:
      owed=self.credits*500
    return owed

student1=Student ("Regan", "Myers","I",12)
student2=Student ("Test", "User","O",3)

print(student1.first, student1.last, student1.dc, student1.credits, "Student owes $ ",student1.tuition())
print(student2.first, student2.last, student2.dc, student2.credits, "Student owes $ ",student2.tuition())