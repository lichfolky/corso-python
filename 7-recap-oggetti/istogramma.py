dati = [3, 4, 5, 5, 2]
'''
for dato in dati:
    for _ in range(0, dato):
        print("*", end="")
    print()
'''
for dato in dati:
    print(dato*"*")