class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Micheal'))


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


print(Student('Micheal'))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a


for n in Fib():
    print(n)


class FibArr(Fib):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


print(FibArr()[50])


class FibSlice(FibArr):
    def __getitem__(self, n):
        if isinstance(n , int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print(FibSlice()[0:5])


class Student(object):
    def __init__(self):
        self.name = 'Micheal'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == "age":
            return lambda: 25
        raise AttributeError("Student object has no attribute %s" % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age())
try:
    print(s.xx)
except AttributeError as e:
    print(e.args)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Micheal')
s()


print(callable(Student('name')))
print(callable(Chain()))

print(callable(str), callable('str'))
