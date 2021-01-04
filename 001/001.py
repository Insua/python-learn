classmates = ["Michael", "Bob", "Tracy"]
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])

print(classmates[-1])

classmates.append("Adam")
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop(1)
print(classmates)

L = ["Apple", 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s), s)

classmates = ("Michael", "Bob", "Tracy")
print(classmates)

t = (1, 2)
print(t)

t = ()
print(t)

t = (1)
print(t)

t = (1, )
print(t)

t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
