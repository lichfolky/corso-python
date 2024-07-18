byte = "00000101"
reversed_byte = byte[::-1]
print(byte)
# contatore
somma = 0
# accumulatore
esponente = 0
for bit in reversed_byte:
    somma = somma + int(bit) * 2**esponente
    esponente += 1
print(somma)
