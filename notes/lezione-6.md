## dizionari

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


## tuple

unpacking x, y, z = t
packing t = 12345, 54321, 'hello!'


tuple immutabili, meno adatte per conini cambi di dimensione
tipo buono per punti

for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

(1, 'sugar')
(2, 'spice')
(3, 'everything nice')

list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]


zip() in conjunction with the * operator can be used to unzip a list:

x = [1, 2, 3]

y = [4, 5, 6]

list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y))

x == list(x2) and y == list(y2)
True
## tuple


## match

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

