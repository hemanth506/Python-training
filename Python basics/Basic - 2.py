print(5/2)

print(5//2)

print(+5)

print(abs(-5))



# __class__ method

class Product:
	def __init__(self):
		print("Instance Created")

	def __call__(self, a, b):
		print(a * b)

ans = Product()

# object is used as a function
# __call__ method will be called
ans(10, 20)

print("=================__base__========================")
# __base__ method
class X:
    pass
class A(X):
    pass
class B(A): 
    pass

# returns the base class 
print(A.__bases__)
print(B.__bases__)

print(__name__ == "__main__")




print("============================================================")

#template strings

from string import Template
s = Template('$who taught $what for $$20')
print(s.substitute(who='tim', what='kung pao'))

# text wrap
import textwrap

s = textwrap.shorten("Hello Hemanth raaj",width = 13, placeholder="...")
print(s)


