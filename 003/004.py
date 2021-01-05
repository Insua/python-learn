L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()
print(next(o))
print(next(o))
print(next(o))

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles():
    l = [1]
    yield l
    while True:
        new_l = []
        for k, v in enumerate(l):
            if k == 0:
                new_l.append(v)
            else:
                new_l.append(l[k - 1] + v)
        new_l.append(l[len(l) - 1])
        l = new_l
        yield l


for k, t in enumerate(triangles()):
    print(t)
    if k == 10:
        break
