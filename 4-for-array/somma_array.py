prezzi = [344, 3, 33, 2, 367, 345, 889]
print(prezzi)

# accumulatore
somma_totale = 0
for prezzo in prezzi:
    somma_totale = somma_totale + prezzo

print(somma_totale)

## avg
media = somma_totale / len(prezzi)

print(media)