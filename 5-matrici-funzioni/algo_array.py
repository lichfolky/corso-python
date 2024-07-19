def max(array):
    print("weilààà")
    massimo = 0
    for item in array:
        if massimo < item:
            massimo = item
    return massimo

def maxi(array):
    if len(array) == 0:
        return 0
    else:
        max(array)

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
