class Student(object):
    pass


s = Student()
s.score = 9999


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())

try:
    s.set_score(101)
except ValueError as e:
    print(e)


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


class Screen(object):
    def width(self, width):
        self.width = width

    def height(self, height):
        self.height = height

    @property
    def resolution(self):
        return self.height * self.width
