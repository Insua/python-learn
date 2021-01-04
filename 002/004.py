def power(x):
    return x * x


print(power(5), power(15))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 10), power(8))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

print(add_end())
print(add_end())


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
print(calc([1, 3, 5, 7]))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
print(calc())

nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, args=('a', 'b'), kw={'x': 99})
f2(1, 2, d=99, ext=None)


def product(*args):
    if len(args) == 0:
        raise TypeError
    p = 1
    for a in args:
        p *= a
    return p
