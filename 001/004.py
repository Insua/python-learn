d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

d['Jack'] = 90
print(d['Jack'])

d['Jack'] = 88
print(d['Jack'])

# print(d['Thomas'])

print('Thomas' in d)

print(d.get('Thomas'))

print(d.get('Thomas', -1))

d.pop('Bob')
print(d)

# key = [1, 2, 3]
# d[key] = 'a list'
# print(d)

s = {1, 2, 3}
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
print(a.replace('a', 'A'))
print(a)
