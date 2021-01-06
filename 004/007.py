import functools
import time


def now():
    print('2021-1-5')


f = now
f()

print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2021-1-5')


now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2021-1-6')


now()
print(now.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2021-1-6')


now()
print(now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2021-1-6')


now()
print(now.__name__)


def metric(fn):
    def wrapper(*args, **kw):
        start = time.time() * 1000
        r = fn(*args, **kw)
        end = time.time() * 1000
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return r
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0001)
    return x + y


f = fast(11, 22)
print(f)
