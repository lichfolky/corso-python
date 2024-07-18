# Date e timestamps, Dizionari e tuple  

import time
>>> t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
>>> print(time.asctime(t))
Sun Feb 23 10:30:48 2020


import time
>>> print(time.localtime())

----
# dates are easily constructed and formatted

from datetime import date

now = date.today()

now
datetime.date(2003, 12, 2)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# dates support calendar arithmetic

birthday = date(1964, 7, 31)

age = now - birthday

age.days
14368




tuple


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

_ è wildcard

case 401 | 403 | 404:
    return "Not allowed"


match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")



match with [a, b]



dizionari

funzioni con multiple values, tuples e dizionari

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

sets

https://docs.python.org/3/tutorial/datastructures.html

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():

    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):

    print(i, v)




tuple

    for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):

    print(item)


(1, 'sugar')
(2, 'spice')
(3, 'everything nice')


list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]


zip() in conjunction with the * operator can be used to unzip a list:
>>>

x = [1, 2, 3]

y = [4, 5, 6]

list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y))

x == list(x2) and y == list(y2)
True