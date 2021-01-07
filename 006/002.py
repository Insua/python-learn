class Student(object):
    pass


bart = Student()
print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.score)


bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.age = 8
print(bart.age)

try:
    print(lisa.age)
except AttributeError as e:
    print(e.args)
