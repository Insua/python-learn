import functools

print(int('12345'))
print(int('12345', base=8))


def int2(x, base=2):
    return int(x, base)


print(int2('10000000'))
print(int2('1010101'))

int2 = functools.partial(int, base=2)
print(int2('10000000'))
print(int2('1010101'))

max2 = functools.partial(max, 10)

print(max2(5, 6, 7))
