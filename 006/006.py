class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


class Student(object):
    name = 'Student'


s = Student()
print(s.name)

print(Student.name)
s.name = 'Michael'
print(s.name)

print(Student.name)

del s.name
print(s.name)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


a = Student('a')
b = Student('b')

print(Student.count)
