import random

# non chiamare il file random, altrimenti circular import
# random.seed(42) x croce

# chiedo utente scelta
scelta = input("testa o croce?\n")

# genero testa o croce
tiro = random.randint(0, 1)
if tiro == 1:
    print("TESTA!")
else:
    print("CROCE!")

# controllo se l'utente ha vinto
if (scelta == "testa" and tiro == 1) or (scelta == "croce" and tiro == 0):
    print("hai vinto!")
else:
    print("hai perso")
