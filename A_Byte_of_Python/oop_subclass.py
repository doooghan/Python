# coding=UTF-8

class SchoolMemer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMemer: {})'.format(self.name))

    def tell(self):
        print('Name: "{}" Age "{}"'.format(self.name, self.age), end = ' ')


class Teacher(SchoolMemer):
    def __init__(self, name, age, salary):
        SchoolMemer.__init__(self,name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMemer.tell(self)
        print('Salary: "{}"'.format(self.salary))


class Student(SchoolMemer):
    def __init__(self, name, age, marks):
        SchoolMemer.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMemer.tell(self)
        print('Marks: "{}"'.format(self.marks))


teacher = Teacher('Mrs.123', 40, 30000)
student = Student('ddd', 20, 75)

print()

members = [teacher, student]
for member in members:
    member.tell()
