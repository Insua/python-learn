from functools import reduce


def f(x):
    return x * x


r = map(f, range(10))
print(list(r))

print(list(map(str, range(10))))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn1(x, y):
        return x * 10 + y

    def char2num1(s1):
        return DIGITS[s1]

    return reduce(fn1, map(char2num1, s))


print(str2int('34324'))


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('23423423423'))


def normalize(name):
    l = []
    for k, v in enumerate(name.lower()):
        if k == 0:
            l.append(v.upper())
        else:
            l.append(v)
    return ''.join(l)


print(normalize('fsdfsdfsfAAA'))


def prod(L):
    def multi(x, y):
        return x * y
    return reduce(multi, L)


print(prod([3, 5, 7, 9]))


def str2float(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    def str2integer(x, y):
        return x * 10 + y
    def str2decimal(x, y):
        return x * 0.1 + y
    s = s.split('.')
    return reduce(str2integer, map(char2num, s[0])) + reduce(str2decimal, map(char2num, reversed(s[1]))) / 10


print(str2float('123.456789'))
