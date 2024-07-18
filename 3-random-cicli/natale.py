altezza = 6

i = 1
# per il numero in altezza di volte, incrementa i ogni volta
while i <= altezza:
    # stampa i volte il simbolo *
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print()
    i += 1


i = 1
# per il numero in altezza di volte, incrementa i ogni volta
while i <= altezza:
    # stampa i volte il simbolo *
    print("*" * i)
    i += 1
