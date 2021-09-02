# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    variable = "Ruchika"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
	
	# a class method to create a
	# Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
	
	# a static method to check if a
	# Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1997)

print(getattr(person1,'variable'))
print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(22))

print("=============================getattr()=================================")

class New:
    variable = "Hemanth"

    def __init__(self,name):
        self.name = name

new1 = New('Raaj')
print("getting the value", getattr(new1,'variable'))
print(new1.name)

print("Setting value")
setattr(new1, 'variable', 'Geeks4Geeks')
print("after setting the value", new1.variable)

print("=============================hasattr()=================================")

print ("Does name exist ? " + str(hasattr(new1, 'variable')))

print("=============================hash()=================================")

print ("The string hash value is : " + str(hash(getattr(new1,'variable'))))

print("=============================isinstance()=================================")

print(isinstance(new1, New))


print("=============================zip()=================================")


# initializing lists
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as set
mapped = list(mapped)
set_mapped = set(mapped)

print(len(mapped))
for i in range(0,len(mapped)):
    print(i, mapped[i])

print("As set")
for id, value in enumerate(set_mapped):
    print(id, value)

# printing resultant values
print ("The zipped result is : ",end="")
print (mapped)



