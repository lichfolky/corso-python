
def stampa_matrice(matrix):
    for riga in matrix:
        for elemento in riga:
            print(elemento, end=" ")
        print()        
    print()
    
# stampa_matrice([[1,0,0], [8,0,2], [1,0,2]])
# stampa_matrice([[1,4,4], [8,5,2], [1,0,2]])