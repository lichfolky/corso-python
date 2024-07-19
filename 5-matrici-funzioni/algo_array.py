def max(array):
    massimo = 0
    for item in array:
        if massimo < item:
            massimo = item
    return massimo

def min(array):
    minimo = array[0]
    for item in array:
        if minimo > item:
            minimo = item
    return minimo

def somma_array(array):
    somma = 0
    for item in array:
        somma += item
    return somma

def avg(array):
    return somma_array(array) / len(array)

def somma(*numeri):
    return somma_array(list(numeri))

'''
Cancella dall'array il primo elemento trovato uguale ad x
'''
def remove(array, x):
    for i in range(len(array)):
        if array[i] == x:
            del array[i]
            break
    return array

def reverse(array):
    return array[::-1]

'''
restituisce l'indice del primo elemento x trovato nell'array
'''
def index(array, x):
    return 0

def concatenate(array, array2):
    return 0

def join(array, sep):
    return 0

def split(array, sep):
    return 0

def count(array,x):
    return 0

def sort(array):
    return 0

def sum(array):
    return 0

def copy(array):
    return 0
