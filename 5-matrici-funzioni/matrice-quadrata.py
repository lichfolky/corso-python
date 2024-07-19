import modulo_matrici

'''
Dato un intero, genera una matrice quadrata di quelle
dimensioni.

Per esempio dato 4, genera:

1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

'''
num = int(input("inserisci numero: "))
matrice = []
conta = 1

for indice_riga in range(num):
    riga = []
    for indice_elemento in range(num):
        riga.append(conta)
        conta += 1
    matrice.append(riga)
    
modulo_matrici.stampa_matrice(matrice)