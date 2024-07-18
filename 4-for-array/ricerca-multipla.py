nomi = [
    "ezio",
    "beppe",
    "ayeye",
    "maria",
    "marco",
    "emilia",
    "anna",
    "ezio",
    "mattia",
    "beppe",
    "ayeye",
    "maria",
    "marco",
    "emilia",
]

trovati = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

nomi_trovati = []

for i in range(0, len(nomi)):
    if nomi[i][-1] == "a":
        print("TROVATO", nomi[i], "all'indice", i)
        trovati[i] = 1
        nomi_trovati.append(nomi[i])

print(trovati)
print(nomi_trovati)
