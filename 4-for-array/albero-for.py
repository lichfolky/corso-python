altezza = 7
# per il numero in altezza di volte, incrementa i ogni volta
for i in range(1, altezza):
    # stampa i volte il simbolo *
    ramo_albero = " +" * i
    # chiamo il metodo delle stringhe center
    print(ramo_albero.center(20))
