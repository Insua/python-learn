from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

print(isinstance('abs', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = max = L[0]
    for l in L:
        if l > max:
            max = l
        if l < min:
            min = l
    return min, max


print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7, 1, 3, 9, 5]))
