matrice = [[1,0,0,2],[3,0,2,3],[4,1,0,0]]

# diagonale
for i in range(0,len(matrice)):
    matrice[i][i] = 6

print(matrice)

# colonne
for i in range(0,len(matrice)):
    matrice[i][3] = 1
    
print(matrice)
