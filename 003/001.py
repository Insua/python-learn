L = ['Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])

L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])
print((0, 1, 2, 3, 4, 5)[:3])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


def trim(s):
    first = s[:1]
    last = s[len(s) - 1:]
    has_space = False
    if first == ' ':
        has_space= True
        s = s[1:]
    if last == ' ':
        has_space = True
        s = s[:len(s) - 1]
    if has_space:
        return trim(s)
    else:
        return s


print(trim("   ABCDEFGHI     "))
