class student:
    pass

student1 = student()
student2 = student()

student1.name = "Suryanshu"
student1.roll = 1001
student2.name = "shubham"
student2.roll = 1002

print(id(student1),id(student2))

help(student)

print(student1.name,student1.roll)
print(student2.name,student2.roll)

print(student1.__dict__)
print(student2.__dict__)


