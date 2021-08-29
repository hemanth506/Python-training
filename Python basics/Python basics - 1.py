print(2+2)

price = 100.50

print(r'C:\some\name')

print("""
    Hello every one                 How are you             I'm fine 
    Can you call me

""")


print(3 * "Um" + "Im")

print("Py" "thon3")

text = ('Hello my dear Hemanth raaj '
'can we have a word')

print(text)

prefix = "Py"
print(prefix + "thon")


word = 'Hemanth'
print(word[0])
print(word[-1])
print(word[0:2])
print(word[2:])
print(word[:2] + word[2:])


textlen = "hbhevkjeriuvhbjshsdvviuvjkiuwbvkehr"
print(len(textlen))


array = [2,67,43,5,7,90]
print(array[2:])
print(array[:])

print(array + [34,76,32,78,22,25])

array2 = [1,8,27,65,81,100]
print(4**3)
array2[3] = 4**3
print(array2)

array2.append(216)
array2.append(7 ** 3)
print(array2)


letters = ['a','b','c','d','e','f']
print(letters[2:5])
letters[2:5] = []
print(letters)
print(len(letters))

a = [1,3,5,7]
n = ['a','b','c','d']
z = [a + n]
print(z)
x = [a , n]
print(x)


# fibanocci series
a,b = 0,1
fib_list = []
while b < 1000:
    fib_list.append(b)
    print(b, end=', ')
    a,b = b , a+b

print("\n")
print(fib_list)

# --------------------------------------------------------------------------------

"""x = int(input('Enter integer'))

if x < 0:
    x = 0
    print("NEgative changed to zero")
elif x == 0:
    print("X in zero")
elif x < 10:
    print("x less than 10")
else:
    print("x is greater than 10")"""

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))


for w in words[:]:
    if len(w) > 6:
        words.insert(1,w)

print(words)

# range

for i in range(5,50,5):
    print(i)

print(range(10))

# prime number

for n in range(2,10):
    for i in range(2, n):
        if n % i == 0:
            print(n, "it is not a prime number")
            break
    else:
        print(n, "it is a prime")

for num in range(2, 10):
    if num%2 == 0:
        print("Found an even number",num)
        continue
    print("Found odd number",num)

def fib(n):
    a,b = 0,1
    while b < n:
        print(b, end='  ')
        a,b = b , a+b
    print()

fib(2000)
print(fib)
f = fib
f(100)




def cheeseshop(kind, *args, **kargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kargs:
        print(kw, ":", kargs[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           sketch="Cheese Shop Sketch")

# defaut argument values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes','Y','YES','Yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope','N','No'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('Do you really want to quit?')

i = 9

def foo(arg=i):
    print(arg)

i=8
foo()

def f(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f(2))
print(f(2))
print(f(2))


def concat(*args, sep = '/'):
    return sep.join(args)

print(concat('hemanth','ruchika','pooja'))


#lambda expression
def lam(n):
    return lambda c: c+n

fa = lam(36)
print(fa(2))

# documentation strings
def my_function(a=2):
    """hello every one.
    how are you"""
    return a**a

print(my_function.__doc__)


# function annotation
def f(ham: str, eggs: str = 'mammel') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:",ham," is ",eggs)

f('hemanth')



