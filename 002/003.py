import math

from abs002 import my_abs
print(my_abs(-100))


def nop():
    pass


nop()


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


my_abs(-100)


def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


def quadratic(a, b, c):
    readical = math.sqrt(math.pow(b, 2) - 4 * a * c)
    return (readical - b) / 2 / a, (0 - b - readical) / 2 / a


print(quadratic(1, 2, 1))
