# standard library

# arrange tha unique characters in alphabitical order
import reprlib
print(reprlib.repr(set('s#*ucali#$%')))

# wraps the list with particular width
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print(pprint.pprint(t, width=50))

# wraps the text with particular width
import textwrap
doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc,width=50))

import locale
print(locale.setlocale(locale.LC_ALL, "English_United States.1252"))

print("===================================================================")


#templating

# to replace the value in template
from string import Template
t = Template('$village folk with $$10 to $cause')
print(t.substitute(village = 'Athipatti', cause="personal usage"))

# to substitute the value as dictionary -> safe_substitute()
t = Template('Returns an amount of $50 to $people')
d = dict(people = "Athipatti village members")
print(t.safe_substitute(d))

print("===================================================================")

import time, os.path
"""photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    print(i, filename)
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))"""

print("===================================================================")


# multithreading

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print("THe main program is running in foreground")

background.join()
print("Main program waited until background was done.")

print("===================================================================")

import logging

logging.debug("debugging information")
logging.info('Informational message')
logging.warning('Warning:config file {0} not found'.format('server.conf'))
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

print("===================================================================")

from array import array
a = array('H', [40, 10, 70, 22])
print(sum(a))

print(a[0:2])

print("===================================================================")

from collections import deque
d = deque(['1', '2', '3', '4'])
d.append('5')
print('Particular', d.popleft())
print('Particular', d.pop())
print('new', d)

print("===================================================================")

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort_left(scores, (300, 'ruby'))
print(scores)
bisect.insort(scores, (350, 'ruby'))
print(scores)

print("===================================================================")

from heapq import heapify, heappop, heappush
data = [1,2,3,5,8,3,1,9,7,6]
heapify(data)
print(data)

heappush(data, -5)
print(data)

print([heappop(data) for i in range(3)])

print("===================================================================")

# Decimal Floating Point Arithmetic
# returns accurate decimal value with decimal floating point when compared with binary floating point

from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(0.70 * 1.05, 2))

print(Decimal('1.00') % Decimal('0.10'))
print(1.00 % 0.10)

print(sum([Decimal('0.1')]*10))
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))

print(sum([0.1]*10))
print(sum([0.1]*10) == 1.0)


getcontext().prec = 36
print(Decimal(1) / Decimal(7))