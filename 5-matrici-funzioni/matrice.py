matrice = [[1,0,0,1,5,5,3,2],[3,0,2,3],[4,1,0,0]]

# stampa classica 
for i in range(0,len(matrice)): # numero di righe
    for j in range(0, len(matrice[i])): # numero di colonne
        print(matrice[i][j])

# stampa moderna 
for riga in matrice: # numero di righe
    for numero in riga: # numero di colonne
        print(numero)
    
    
matrice = [[1,0,0,2],[3,0,2,3],[4,1,0,0]]

# diagonale
for i in range(0,len(matrice)):
    matrice[i][i] = 6

print(matrice)

# colonne
for i in range(0,len(matrice)):
    matrice[i][3] = 1
    
print(matrice)
