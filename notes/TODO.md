

### Pile e code
https://docs.python.org/3/tutorial/datastructures.html

### List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

nested list comprehension

[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

### lambda a, b: a+b.

- If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
print(f'C:\some\name') ???

- String literals 

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

- pyenv
- pip

## oggetti passaggio valore e referenza

- gui 
https://wxpython.org/
https://www.blog.pythonlibrary.org/books/python-201-intermediate-python/

- fare panda e numpy intro
- analizzare gli errori più comuni python


### dopo classi
- enum
- pikle
7.2.2. Saving structured data with json¶
https://docs.python.org/3/tutorial/inputoutput.html

### fine

- Executable Python Scripts 
x unix
https://docs.python.org/3/tutorial/appendix.html#tut-scripts

per win
https://www.blog.pythonlibrary.org/2021/05/27/pyinstaller-how-to-turn-your-python-code-into-an-exe-on-windows/


pacchetti

pacchetti
https://docs.python.org/3/tutorial/modules.html


sqlite3 ???
https://docs.python.org/3/library/sqlite3.html#module-sqlite3

---

import os

os.getcwd()      # Return the current working directory
'C:\\Python312'

os.chdir('/server/accesslogs')   # Change current working directory

os.system('mkdir today') 



sys.exit().


---
librerie standard
random
math
statistics

urllib.request for retrieving data from URLs 


    from urllib.request import urlopen

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:

    for line in response:

        line = line.decode()             # Convert bytes to a str

        if line.startswith('datetime'):

            print(line.rstrip())         # Remove trailing newline



---
### annotations 
https://peps.python.org/pep-0484/




Duck typing

try:
    iterator = iter(the_element)
except TypeError:
    # not iterable
else:
    # iterable

# for obj in iterator:
#     pass




my_small_program = '''print('ham')
print('sandwich')'''
>>> exec(my_small_program)