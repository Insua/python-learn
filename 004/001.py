f = abs
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


x = -5
y = 6
f = abs
print(add(x, y, f))
