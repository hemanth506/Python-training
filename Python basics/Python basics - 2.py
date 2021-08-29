# data structures

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))

print(len(fruits))

print(fruits.count('tangerine'))

print(fruits.index('banana',5))



fruits.append('grapes')
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.pop()
print(fruits)

# list as queue
from collections import deque
queue = deque(['Eric','John','hemanth'])
queue.append('ruchika')
queue.append('harish')
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)

# list comprehension
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

squares = list(map(lambda x: x**3, range(10)))
print(squares)

squares = [x**4 for x in range(10)]
print(squares)


comp = [(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y ]
print(comp)

comp = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            comp.append((x,y))

print(comp)


vec = [-4, -2, 0, 2, 4]
oper = [x*2 for x in vec]
print(oper)

get_abs = [abs(x) for x in vec]
print(get_abs)

operate = [x*2 for x in vec if x >= 0]
print(operate)


words = ["  heman   th","      harish  ","Ruchika      "]
stripword = [word.strip() for word in words]
print(stripword)

# create a list of 2-tuples
twoTuple = [(x,x**2) for x in range(6)]
print(twoTuple)

vec = [[1,2,3],[4,5,6],[7,8,9]]
gen_vec = [num for elt in vec for num in elt]
print(gen_vec)

from math import pi
pipe = [abs(round(pi,i)) for i in range(1,5)]
print(pipe)


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)

trans = []
for x in range(4):
    trans_row = []
    for i in matrix:
        trans_row.append(i[x])
    trans.append(trans_row)

print(trans)

print(list(zip(*matrix)))

# delete statement
a = [-1,3,6,3,2,7,4,7,9]
print(a)

del a[5:]
print(a)

del a[0]
print(a)

del a

# tuple
t = 1234,567,"hemanth"
print(t)
w = t, 9876,5432
print(w)
u = t, (9876,5432)
print(u)

z = w , u
print(z)

empty = ()
len(empty)

double = ("hi")
print(type(double))
single = ("hello",)
print(type(single))

# reverse assignment
x,y,z = t
print(x)
print(y)
print(z)

# Sets -> eliminates duplicate values
crt_set = set()
sets = [1,4,7,2,9,6,4,2,1,6,3]
for i in sets:
    crt_set.add(i)

print(crt_set)

basket = {"orange","apple","banana","graph"}
print("cream" in basket)
print("apple" in basket)


a = set('abdhsdbaajkbjbvd')
b = set('plowe15evsbdawqd')
print(a) # unique letters in a 
print(a-b) # letters in a but not in b
print(b-a) # letters in b but not in a
print(a&b) # letters in both a and b
print(a|b) # letters in a or b or both
print(a^b) # letters in a or b and not in both

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


# dictionary
tele = {"hem":20111997, "har":26021999, "ruchi": 27081998}
print(tele)
print(tele['hem'])
tele['logi'] = 24081997
print(tele)
del tele['har']
tele['harish'] = 26021999
print(tele)

print(list(tele.keys()))
print(list(tele.values()))
print(sorted(tele.keys()))
print(tele)

def_dict = dict([('sale',15423),('profit',879546),('interest',4521)])
print(def_dict)


new_dict = {x: x**2 for x in range(5)}
print(new_dict)

print(dict(sape=4139, guido=4127, jack=4098))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key,value in knights.items():
    print(value)

# enumerate -> will generate index value as 0,1,2,3,...
for i, v in enumerate(knights.items()):
    print(i, v)

questions = ['name', 'Profession', 'favorite color']
answers = ['Hemanth', 'Software dev', 'blue']

for e, f in zip(questions, answers):
    print('What is your {0} It is {1}.'.format(e,f))


for i in reversed(range(1,10,2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for i in raw_data:
    if not math.isnan(i):
        filtered_data.append(i)
print(filtered_data)


string1, string2, string3 = 'Ruchika', 'Hemanth Raaj', ''
non_null = string1 or string2 or string3
print(non_null)