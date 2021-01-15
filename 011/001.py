import re

m = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(m)

print(re.split(r'\s+', 'a b  c'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1), m.group(2))
