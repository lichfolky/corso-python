# Matrici, funzioni e librerie  

correzione acqua, acqua, fuochino, fuoco, oceano!
abs()

sommiamo un array
e poi facciamo massimo

sum(range(4))
sum([3,4,5])

max(3,4)
max(n1, n2, n3, ...)
Or:
max(iterable)

correzione cornicetta

max
- accetta un numero qualsiasi di parametri
- accetta un array


shallow copy [:] array

copy.copy(x)

    Return a shallow copy of x.

copy.deepcopy(x[, memo])


list(range(0, 5))

in

del

### funzioni

def hello():
    print("hello!")

def hello(name):
    print("hello", name)

def hello(name, surname):
    print("hello", name, surname)


parametri
chiamata

return

None

Scope variabile funzione

return multiple data


### librerie

import nomelibreria

from fibo import fib, fib2
from fibo import *


TDD test driven development










---

Default Argument Values con =


keyword arguments 

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


TDD test driven development

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)



https://docs.python.org/3/tutorial/modules.html

import fibo
fibo.fib(1000)

from fibo import fib, fib2

fib(500)

from fibo import *

fib(500)

---
import importlib; importlib.reload(modulename).

Executing modules as scripts

When you run a Python module with

python fibo.py <arguments>

the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

-
# File demo.py
import sys
print(sys.argv)

Here is the output from running python demo.py one two three at the command line:

['demo.py', 'one', 'two', 'three']



import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)



def foo(*args: expression, **kwargs: expression):


import fibo, sys

dir(fibo)
['__name__', 'fib', 'fib2']




annotations
str



seasons = ['Spring', 'Summer', 'Fall', 'Winter']

list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]