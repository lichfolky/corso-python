
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

# Files


f = open('workfile', 'w', encoding="utf-8")

https://docs.python.org/3/tutorial/inputoutput.html

with open('workfile', encoding="utf-8") as f:

    read_data = f.read()

# We can check that the file has been automatically closed.

f.closed


criptazione romana
csv
html?
sostituisci parole


- # coding=utf-8




string literals




8.2. Exceptions¶
https://docs.python.org/3/tutorial/errors.html