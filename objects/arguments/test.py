class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

student1 = Student("Chase Opsahl", 25, "Male")
student2 = Student("Anna Opsahl", 25, "Female")

print(student1.name, student1.age, student1.gender)
print(student2.name, student2.age, student2.gender)
