age = 20
if age > 18:
    print('your age is', age)
    print('adult')

age = 3
if age > 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

birth = input('birth:')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')

bmi = 80.2 / (1.7 * 1.7)
print(bmi)
