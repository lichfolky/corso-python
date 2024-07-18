import random

seed = random.randint(1, 1000)
random.seed(seed)
print(seed)

somma = 0
tentativi = 10

# per tentativi numero di volte
i = 0
while i < tentativi:
    # sommo alla variabile somma un numero random tra 1 e 20 compresi
    somma = somma + random.randint(1, 20)
    i += 1

# divido la somma per in numero per tentativi
media = somma / tentativi
# ottengo il valore atteso (media) di un lancio di dado da 20
print("la media è:", media)


## ESERCIZIO: fai questa simulazione con 2 dadi da 6
