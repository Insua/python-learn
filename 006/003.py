class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
try:
    print(bart.__name)
except AttributeError as e:
    print(e.args)

print(bart._Student__name)

bart = Student('Bart Simpson', 59)
print(bart.get_name())
bart.__name = 'New Name'
print(bart.__name)
print(bart.get_name())


class Student(object):

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ['male', 'female']:
            self.__gender = gender
        else:
            raise ValueError('bad gender')
