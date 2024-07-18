tiri = [1, 19, 20, 11, 7, 3]

# contatore
successi = 0

# successo se > 10
for tiro in tiri:
    if tiro > 10:
        successi = successi + 1

print(successi)
