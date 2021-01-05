def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())



f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)


print(f1, f2, f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


c = count()
c0 = c[0]
c1 = c[1]
c2 = c[2]

print(c0(), c1(), c2())


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def createCount():
    def _int():
        n = 1
        yield 1
        while True:
            n += 1
            yield n
    i = _int()

    def counter():
        return next(i)
    return counter


c = createCount()
print(c(), c(), c(), c(), c())
