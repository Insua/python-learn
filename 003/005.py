from collections.abc import Iterator
from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

l = iter([1, 2, 3])
print(next(l))
print(next(l))
print(next(l))
