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
