# __init__() method
# is an instance method
# is used to create and initializer the attributes during the object creation.

class student:
    """
            this is a class student to  manage student information
            """
    def __init__(self,name,roll,dpt):
        print(f"we are calling the initializer for {self}!")
        self.name = name # student1.name = "john"
        self.roll = roll # student1.roll = 1
        self.department = dpt


'''
    def study(self,n_hours):
        print(f"Student studies for {n_hours} hours a day")


    def sports(self,n_hours):
        print(f"Student sports for {n_hours} hours a day")
'''
student1 = student("john",1,'Science')


# object_name.attribute_name = value
student2 = student("marry",2,'Engineering')
print('===================================================')
print(f"name\troll\tdepartment")
print('===================================================')
print(student1.name,'\t',student1.roll,'\t',student1.department)
print(student2.name,'\t',student2.roll,'\t',student2.department)

print(student1.__dict__)
print(student2.__dict__)


"""
Instance variable/attribute are different for different objects
"""
print('====================================')
student1.grade = 'A'
# student2.grade = 'B'

print(student1.__dict__)
print(student2.__dict__)

student3 = student("harry",3,"Art")
print('===================================================')
print(student3.name,'\t',student3.roll,'\t',student3.department)
print(student3.__dict__)