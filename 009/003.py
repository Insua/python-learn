import os

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x'))

print(os.path.abspath('.'))
print(os.path.join('/home/insua/files', 'testdir'))
try:
    print(os.mkdir('/home/insua/files/testdir'))
except FileExistsError as e:
    print(e.args)
print(os.rmdir('/home/insua/files/testdir'))

print(os.path.split('/home/insua/files/test.txt'))
print(os.path.splitext('/home/insua/files/test.txt'))

# os.rename('/home/insua/files/test.txt', '/home/insua/files/test.py')

[print(x) for x in os.listdir('.') if os.path.isdir(x)]
[print(x) for x in os.listdir('./001') if os.path.isfile(x)]
