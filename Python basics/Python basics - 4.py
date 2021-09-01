# class

def scope_test():
    def do_local():
        global spam
        spam = "local spam"
        print(spam)
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assign -> ", spam)
    do_nonlocal()
    print("After non local assign -> ", spam)
    do_global()
    print("After global assign -> ", spam)


scope_test()
print("It is global -> ", spam)



class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(5.2, 6.5)
print(x.r, x.i)


class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self,trick):
        self.tricks.append(trick)

d = Dog('Julie')
d.add_tricks("Jump higher")

e = Dog("Kot")
e.add_tricks("Roll over")


print(d.tricks)
print(e.tricks)


def f1(self, x, y):
    return max(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

obj1 = C()
print(obj1.f(5, 8))
print(obj1.g())


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

newbag = Bag()
newbag.add(56)
newbag.addtwice(78)
print(newbag.data)


print("= "*50)

s = [2,5,7,3,2,6,7]
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print("= "*50)


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('Hemanth')
for char in rev:
    print(char)

print("= "*50)

# Generators

def straight(data):
    for index in range(0, len(data)):
        yield data[index]

def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for char in reverse('golf'):
    print(char)


# ===========================================================================

# Standard library

import os
print(os.getcwd())  # get current directory

os.chdir('C:/Users/Welcome')
os.system('mkdir today')

print(dir(os))
# print(help(os))

import glob
print(glob.glob('*.py', recursive=False))


import sys
print(sys.argv)


# print(sys.stderr.write('Warning,...'))

replace = ('tea for too').replace('too', 'two')
print(replace)

print("= "*50)

# Math
import math
calc = math.cos(math.pi / 4)
print(calc)

print(math.log(1024, 2))

print("= "*50)

# random
import random
print(random.randrange(50))
print(random.randint(10,15))
print(random.choice(['apple', 'pear', 'banana','abc',154, 896]))
print(random.sample(range(100), 15))
print(random.random())   # random float

print("= "*50)

# statistics
import statistics
data = [10, 45, 86,89,2,4,98,1,5]
print(statistics.mean(data))
print(statistics.harmonic_mean(data))

data.sort()
print(data)
print(statistics.median(data))

print(statistics.variance(data))

print("= "*50)

# data and times
import datetime
now = datetime.date.today()
print(now)

print(now.strftime("%m-%d-%y - %d %b %y  is a %A on the %d day of %B"))


def days_of_birth(y,m,d):
    now = datetime.date.today()
    birthday = datetime.date(y, m, d)
    age = now - birthday
    return age.days

print(days_of_birth(1997, 11, 20))
print(days_of_birth(1998, 8, 27))
print(days_of_birth(1999, 2, 26))


import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))
print(t)

print(zlib.decompress(t))

print(zlib.crc32(s))

print("= "*50)

from timeit import Timer
print(Timer('t=a; a=b; b=t','a=1; b=2').timeit())


print("= "*50)


def average(values):
    return sum(values) / len(values)

import doctest
print(doctest.testmod())


