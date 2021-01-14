with open('/home/insua/files/test.txt', 'r') as f:
    print(f.read())
    f.close()

with open('/home/insua/files/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('/home/insua/files/test.png', 'rb') as f:
    f.read()

with open('/home/insua/files/test.txt', 'w') as f:
    f.write('Hello, world!')


fpath = '/etc/ts.conf'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
