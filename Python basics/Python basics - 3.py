# input and output
s = "Hello world"
print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + str(x) + ', and y is ' + str(y) + '...'
print(s)
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
hellos = str(hello)
print(hellos)

# repr

hellos = repr(hello)
print(hellos)

print(repr((x, y, ('spam', 'eggs'))))

#=======================================
# rjust

for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end = ' ')
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:5d}'.format(x,x*x,x*x*x))

# =====================================
# zfill

x = '12'.zfill(5)
print(x)

y = '-4.7'.zfill(6)
print(y)

print('3.14159265359'.zfill(5))

print('The basic format of {} in {} is this'.format('string','python'))

print("{0} is the elder and {1} is the youger".format("Hemanth","Harish"))

print("{1} is the elder and {0} is the youger".format("Harish","Hemanth"))

print("{Name} loves {food}".format(Name='Hemanth',food='Noodles'))

print("{0}'s son {Name} loves {food}".format('Latha',Name='Hemanth',food='Noodles'))


"""
!s -> string
!r -> repr
!a -> acsii
"""
content = "Pikachu"
print('{!s} is a comic character'.format(content))
print('{!r} is a comic character'.format(content))
print('{!a} is a comic character'.format(content))


import math
print('THe value is approx {0:.3f}'.format(math.pi))
print('THe value is approx {0:.5f}'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, value in table.items():
    print('{0:10}  ==>  {1:10}'.format(name,value))

print('Jack: {0[Jack]:d}  ==>  Dcab: {0[Dcab]:d}  ==>  Sjoerd: {0[Sjoerd]:d}'.format(table))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


f = open('workfile.txt', 'w+')

f.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed arcu nibh, facilisis quis interdum ac, efficitur vel eros.
 Pellentesque vehicula dictum tristique. Morbi tristique ut tellus fringilla semper. Integer tempor ultrices tincidunt.
  Proin consequat venenatis congue. Ut id semper ex, sit amet facilisis ligula. Morbi pellentesque tellus id porta rutrum.
   Pellentesque eu mattis sem. Ut gravida nulla id tempus cursus. 
   Duis vehicula quam sed sapien lobortis gravida vitae eu arcu.
    Fusce eu mauris urna.
 Sed cursus efficitur tellus, non tempor magna pretium venenatis. Ut aliquam condimentum magna quis efficitur.\n\nHello every one nice to meet you""")

with open('workfile.txt') as f:
    print(f.read())
    # f.write("Hello every one nice to meet you")

print("=======================================================")
with open('workfile.txt') as f:
    for i in f:
        print(i, end=' ')
    
f.close()

print(f.closed)


#=====================================================================================

import json
print(json.dumps([1,3,'dvsb']))

print("=" * 100)

#=====================================================================================

# Exceptions

# Zero division error
# print(10*(1/0))

# name error
# print(4 + spam*3)

# type error
# print('2' + 2)

"""flag =True
check = True
while flag:
    try:
        if check:
            x = int(input("Enter X number: "))
            if isinstance(x,int):
                print("It is an integer")
                flag = False

        a = int(input("Enter A number: "))
        b = str(input("Enter B number: "))
        print(a/b)
        flag = False
    except ValueError as vale:
        print("It is not an integer  -> ",vale)
        flag = True
    except ZeroDivisionError as zerod:
        print("Number cannot be divisible by zero  -> ", zerod)
        flag = True
        check = False
    except NameError as nameE:
        print("Invalid name  -> ", nameE)
        flag = True
    except TypeError as typeE:
        print("Invalid Type  -> ", typeE)
        flag = True
    finally:
        print("Executes every time")

"""
#=====================================================================================

import sys

try:
    f = open('workfile1.txt')
    s = f.readline()
    i = str(s.strip())
    print(i)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    print("closed")
    f.close()

print("=" * 100)

#=====================================================================================

try:
    print('Exception is raised -> start')
    raise NameError("Name error is raised")  # Raise Error
    print('Exception is raised -> end') # After raise nothing is executed
except NameError as e:
    print ("An exception of -> {0}".format(e))

print("=" * 100)

#=====================================================================================

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("accident occured, {0}".format(self.msg))

try:
    raise Accident("Crash between two vehicles")
except Accident as acc:
    acc.handle()

print("=" * 100)

#=====================================================================================

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [C, D, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

print("=" * 100)

#=====================================================================================

for line in open("workfile.txt"):
    print(line, end=" ")

print("=" * 100)


with open("workfile.txt") as f:
    for line in f:
        print(line, end=' ')
