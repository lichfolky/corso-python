numero_segreto = 4
# loop infinito (per uscire da ciclo infinito ctrl + c, anche mac)
while True:
    numero = int(input("inserisci un numero:\n")) # converto in intero
    differenza = numero - numero_segreto 
    # abs, valore assoluto
    if differenza < 0:
        differenza = - differenza
        
    if differenza == 0:
        print("TROVATO!!!!!")
        break # esce dal ciclo
    else:
        if differenza < 3:
           print("fuoco!")
        else:
            if differenza < 6:
                print("fuochino!")
            else:
                if differenza < 9:
                    print("acqua!")
                else:
                    if differenza < 13:
                        print("oceano!")
                        
'''
    if differenza == 0:
        print("TROVATO!!!!!")
        break # esce dal ciclo
    elif differenza < 3:
           print("fuoco!")
        elif differenza < 6:
                print("fuochino!")
            elif differenza < 9:
                    print("acqua!")
                else:
                    if differenza < 13:
                        print("oceano!")
'''