"""
print("Faccio qualcosa")
risposta = input("Vuoi continuare?, Si o no?\n")
while risposta != "si" and risposta != "no":
    risposta = input("Vuoi continuare?, Si o no?\n")

while risposta == "si":
    print("Faccio qualcosa")
    risposta = input("Vuoi continuare?, Si o no?\n")
    while risposta != "si" and risposta != "no":
        risposta = input("Vuoi continuare?, Si o no?\n")
"""

# risposta è uguale a si per poter esegure il ciclo almeno una volta
risposta = "si"
while risposta == "si":
    print("Faccio qualcosa")
    risposta = input("Vuoi continuare?, Si o no?\n")
    while risposta != "si" and risposta != "no":
        risposta = input("Vuoi continuare?, Si o no?\n")
