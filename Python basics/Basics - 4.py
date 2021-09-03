from difflib import SequenceMatcher
import difflib

str1 = "I like Pizza"
str2 = "I like icecream"

seq = SequenceMatcher(a = str1, b = str2)
print(seq.ratio())

print("-----------------------------------------------------")

from difflib import Differ
string1 = "I would like to order a pepperoni pizza"
string2 = "I would like to order a veggie burger"

str_lines1 = string1.splitlines()
str_lines2 = string2.splitlines()

# print(str_lines1)

d = difflib.Differ()
diff =  d.compare(str_lines1, str_lines2)

print("\n".join(diff))

print("-----------------------------------------------------")

from difflib import get_close_matches

print(get_close_matches('Hem', ['Harish', 'Latha', 'Prem', 'Hemanth', 'Hemnath', 'HemSai', 'sai']))

print("-----------------------------------------------------")

from textwrap import TextWrapper, shorten
  
value = """This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""
  
# set width to wrapper
wrapper = TextWrapper(width=50)

word_list = wrapper.wrap(text=value)
  
# Print each line.
for element in word_list:
    print(element)

print("-----------------------------------------------------")

wrapper = TextWrapper(width=75)
  
string = wrapper.fill(text=value)
  
print (string)

print("-----------------------------------------------------")

print(shorten("Hello world", width=10, placeholder="..."))

print("-----------------------------------------------------")

import calendar
yy = 2021
mm = 11
   
# display the calendar
print(calendar.month(yy, mm))

print("-----------------------------------------------------")

print (calendar.calendar(2018, 2, 1, 6))

print("-----------------------------------------------------")

obj = calendar.Calendar(firstweekday = 5)
 
# iterating with itermonthdates
for day in obj.itermonthdates(2018, 8):
    print(day)

print("-----------------------------------------------------")

print(calendar.leapdays(2016, 2022))






